import warnings
from util import get_next_variable, is_dbpedia_entity_iri, is_wikidata_entity_iri, replace_prefix_dbpedia, replace_prefix_wikidata
from llm import chat_model
from typing import List
import validators
from SPARQLWrapper import SPARQLWrapper, JSON
from rdflib import Graph
from rdflib.namespace import RDF
import random
from rdflib import Literal
import re
from tqdm import tqdm
from timeout import timeout
import pandas as pd
import os

warnings.filterwarnings("ignore")

class QADatasetGenerator:
  def __init__(self, source: str, excluded_props: List[str], timeout = 40, classes_file: str = "dataset\io\classes_allowed.txt"):
    self.source = source
    self.is_api = validators.url(source)
    self.excluded_props = excluded_props
    self.wrapper = None if not self.is_api else SPARQLWrapper(self.source,
                   agent="Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11")
    self.timeout = timeout
    self.classes_file = classes_file
    self.graph = None
    if not self.is_api:
      self.graph = Graph()
      self.graph.parse(source)

  def write_to_file(self, dataset_name: str, amount: int, category: str, count: bool):
    # count can be used with simple only
    if count and category.startswith("complex"):
      raise ValueError("Count for complex queries is not supported")
    
    questions, queries = self.generate(amount, category, count)
    df = {
      "question": questions,
      "query": queries
    }
    df = pd.DataFrame(df)
    status = "count" if count else "normal"

    directory = f'dataset\io\{dataset_name}'
    if not os.path.exists(directory):
      os.makedirs(directory)

    df.to_json(f'{directory}\{category}_{amount}_{status}.json', orient='records', indent=4)
    print("Finished writing dataset")

    
  def generate(self, amount: int, category: str, count: bool):
    questions = []
    queries = []
    for _ in tqdm(range(amount)):
      while True:
        try:
          with timeout(self.timeout):
            cat = category.split("_")
            question, query = "", ""
            if cat[0] == "simple":
              if count:
                question, query = self.generate_count(cat[1])
              else:
                question, query = self.generate_simple(cat[1])
              break
            elif cat[0] == "complex":
              question, query = self.generate_complex(cat[1])
              break
            if query in queries:
              raise ValueError()
        except TimeoutError:
          print("Timeout, repeating")
          continue
        except ValueError:
          print("Duplicate query, repeating")
          continue
        except Exception as e:
          print(f"Error: {e}")
          continue
      question, query = question.strip(), query.strip()
      questions.append(question)
      queries.append(query)
    return questions, queries

  def __refine_question(self, mapping, query):
    mapping_in_sentence = ""
    for uri, label in mapping.items():
      if "dbpedia" in self.source:
        pref = replace_prefix_dbpedia(uri)
        if pref in query:
          mapping_in_sentence += f"{pref} has human-readable name '{label}'\n"
      elif "wikidata" in self.source:
        pref = replace_prefix_wikidata(uri)
        if pref in query:
          mapping_in_sentence += f"{pref} has human-readable name '{label}'\n"
      else:
        if uri in query:
          mapping_in_sentence += f"{uri} has human-readable name '{label}'\n"

    prompt = f"""Having a SPARQL query:
{query}
Where:
{mapping_in_sentence}
Transform the SPARQL query to a natural language question.
Output just the transformed question
    """
    result = chat_model.invoke(prompt).content
    if "Here" in result:
      matched = re.search(r'"(.*?)"', result, re.DOTALL)
      if matched:
        return matched.group(1)
      else:
        return result
    return result

  def __get_label(self, entity):
    if self.is_api:
      if "wikidata" in self.source:
        if "wikidata" in entity:
          entity = entity.split("/")[-1]
          entity = f"wd:{entity}"
          query = f"""
            select ?lit {{
              {entity} rdfs:label ?lit .
              filter (lang(?lit) = 'en')
            }}
          """
          self.wrapper.setQuery(query)
          self.wrapper.setReturnFormat(JSON)
          results = self.wrapper.query().convert()['results']['bindings'][0]['lit']['value']
          return results
        else:
          return entity
      else:
        # dbpedia
        query = f"""
            select ?lit {{
              <{entity}> rdfs:label ?lit .
              filter (lang(?lit) = 'en')
            }}
          """
        self.wrapper.setQuery(query)
        self.wrapper.setReturnFormat(JSON)
        results = self.wrapper.query().convert()['results']['bindings'][0]['lit']['value']
        return results
    else:
      try:
        query = f"""
          select ?lit {{
            <{entity}> rdfs:label ?lit .
          }}
        """
        result = list(self.graph.query(query))[0][0].toPython()
      except:
        # if literal
        result = entity.toPython()
      return result

  def __filter_prop_query(self):
    _filter = [f"contains(str(?p), '{uri}') = false" for uri in self.excluded_props]
    return " && ".join(_filter)

  def __random_walk(self, entity):
    filter_prop = self.__filter_prop_query()
    query = f"""
          select ?p ?o {{
            <{entity}> ?p ?o .
            filter (
              {filter_prop}
            )
          }}
          """
    if self.is_api:
      # wikidata, dbpedia is way too huge we can't query like this below
      self.wrapper.setQuery(query)
      self.wrapper.setReturnFormat(JSON)
      results = self.wrapper.query().convert()['results']['bindings']
      tuples = []
      for tup in results:
        tmp_p = tup['p']['value']
        tmp_o = tup['o']['value']
        tuples.append((entity, tmp_p, tmp_o))
      return random.choice(tuples)
    else:
      res = list(self.graph.query(query))
      choice = list(random.choice(res))
      choice.insert(0, entity)
      return tuple(choice)

  def __get_one_triple(self, subject = None):
    start_given = subject != None
    err = True
    while err:
      try:
        if not start_given:
          subject = self.__random_pick_entity()
        triple = self.__random_walk(subject)
        if self.is_api:
          if "wikidata" in self.source:
            while "P31" in triple[1] or not triple[1].startswith("http://www.wikidata.org/prop/direct") \
              or triple[2].startswith("http://www.wikidata.org/entity/statement/") or (validators.url(triple[2]) and not is_wikidata_entity_iri(triple[2])):
                triple = self.__random_walk(subject)
            err = False
          else:
            # for dbpedia
            while not triple[1].startswith("http://dbpedia.org/ontology/") or "wiki" in triple[1]:
              triple = self.__random_walk(subject)
            err = False
        else:
          err = False
      except Exception as e:
        pass
    return triple

  def __concat_str_with_datatype(self, prop, o):
    query = f"select ?range {{ <{prop}> rdfs:range ?range . }}"
    mapping = {
        "http://www.w3.org/2001/XMLSchema#": "xsd:",
        "http://dbpedia.org/datatype/": "dbd:"
    }
    if "dbpedia" in self.source:
      self.wrapper.setQuery(query)
      self.wrapper.setReturnFormat(JSON)
      datatype = self.wrapper.query().convert()['results']
      datatype = datatype['bindings'][0]['range']['value']
      for k, v in mapping.items():
        tmp = datatype.replace(k, v)
        if tmp == "xsd:string":
          return f"'{o}'"
        datatype = tmp
      return f"'{o}'^^{datatype}"
    elif "wikidata" in self.source:
      # manual match because there is no rdfs:range
      datetime_pattern = r"^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}Z$"
      if bool(re.fullmatch(datetime_pattern, o)):
        return f'"{o}"^^xsd:dateTime'
      else:
        return f'"{o}"'
    else:
      datatype = list(self.graph.query(query))[0][0]
      for k, v in mapping.items():
        tmp = datatype.replace(k, v)
        if tmp == "xsd:string":
          return f"'{o}'"
        datatype = tmp
      return f"'{o}'^^{datatype}"

  def __is_no_property(self, entity):
    if isinstance(entity, Literal):
      return True
    try:
      self.__random_walk(entity)
      return False
    except IndexError:
      return True

  def generate_count(self, category):
    # this uses simple pattern only
    mapping, answer = self.generate_simple(category, return_question=False)
    new_answer = answer.replace("?x", "(count(?x) as ?cnt)", 1)
    question = self.__refine_question(mapping, new_answer)
    return question, new_answer

  def generate_simple(self, category, return_question = True):
    # one triple pattern
    # supports only a b ?x
    triple = self.__get_one_triple()
    if "wikidata" in self.source:
      while not triple[1].split("/")[-1].startswith("P"):
        triple = self.__get_one_triple()
    query_uri = "select ?x {{ <{s}> <{p}> ?x . }}"
    query_prefix = "select ?x {{ {s} {p} ?x . }}"
    query_prefix_reverse = "select ?x {{ ?x {p} {o} . }}"
    query_uri_reverse = "select ?x {{ ?x <{p}> {o} . }}"

    if self.is_api:
      if "wikidata" in self.source:
        if is_wikidata_entity_iri(triple[2]):
          s, p, o = self.__get_label(triple[0]), self.__get_label(triple[1]), self.__get_label(triple[2])
          s_pref, p_pref, o_pref = triple[0].split("/")[-1], triple[1].split("/")[-1], triple[2].split("/")[-1]
          s_pref, p_pref, o_pref = f"wd:{s_pref}", f"wdt:{p_pref}", f"wd:{o_pref}"
        else:
          s, p, o = self.__get_label(triple[0]), self.__get_label(triple[1]), triple[2]
          s_pref, p_pref = triple[0].split("/")[-1], triple[1].split("/")[-1]
          s_pref, p_pref, o_pref = f"wd:{s_pref}", f"wdt:{p_pref}", self.__concat_str_with_datatype(triple[1], o)
        mapping = {s_pref: s, p_pref: p, o_pref: o}
        if category == "1":
          answer = query_prefix.format(s=s_pref, p=p_pref, o=o_pref)
        else:
          answer = query_prefix_reverse.format(s=s_pref, p=p_pref, o=o_pref)
        if return_question:
          refined_question = self.__refine_question(mapping, answer)
          return refined_question, answer
        else:
          return mapping, answer
      else:
        if "dbpedia" in triple[2]:
          # entity
          s, p, o = self.__get_label(triple[0]), self.__get_label(triple[1]), self.__get_label(triple[2])
          s_pref, p_pref, o_pref = replace_prefix_dbpedia(triple[0]), replace_prefix_dbpedia(triple[1]), replace_prefix_dbpedia(triple[2])
        else:
          s, p, o = self.__get_label(triple[0]), self.__get_label(triple[1]), triple[2]
          s_pref, p_pref, o_pref = replace_prefix_dbpedia(triple[0]), replace_prefix_dbpedia(triple[1]), self.__concat_str_with_datatype(triple[1], triple[2])
        mapping = {s_pref: s, p_pref: p, o_pref: o}
        if category == "1":
          answer = query_prefix.format(s=s_pref, p=p_pref, o=o_pref)
        else:
          answer = query_prefix_reverse.format(s=s_pref, p=p_pref, o=o_pref)
        if return_question:
          refined_question = self.__refine_question(mapping, answer)
          return refined_question, answer
        else:
          return mapping, answer
    else:
      if not isinstance(triple[2], Literal):
        s, p, o = self.__get_label(triple[0]), self.__get_label(triple[1]), self.__get_label(triple[2])
      else:
        s, p, o = self.__get_label(triple[0]), self.__get_label(triple[1]), triple[2].toPython()
      mapping = {triple[0]: s, triple[1]: p, triple[2]: o}
      if category == "1":
        answer = query_uri.format(s=triple[0], p=triple[1], o=triple[2])
      else:
        if not isinstance(triple[2], Literal):
          answer = query_uri_reverse.format(s=triple[0], p=triple[1], o=f"<{triple[2]}>")
        else:
          answer = query_uri_reverse.format(s=triple[0], p=triple[1], o=f"{self.__concat_str_with_datatype(triple[1], triple[2])}")
      if return_question:
        refined_question = self.__refine_question(mapping, answer)
        return refined_question, answer
      else:
        return mapping, answer

  def generate_complex(self, category, max_triples = 3):
    starting_triple = self.__get_one_triple()
    depth = random.choice([i for i in range(2, max_triples)])

    if category == '1':
      # pattern: ?x y z ; a b .
      subject = starting_triple[0]
      triples = set()
      triples.add(starting_triple)
      while len(triples) <= depth:
        triple = self.__get_one_triple(subject)
        if self.is_api:
          if is_wikidata_entity_iri(triple[-1]):
            triples.add(triple)
          else:
            # dbpedia
            pref_repr = replace_prefix_dbpedia(triple[-1])
            if pref_repr.startswith("dbo:") or pref_repr.startswith("dbr:"):
              triples.add(triple)
        else:
          triples.add(triple)

      if self.is_api:
        if "wikidata" in self.source:
          triple_pattern = []
          for (_, p, o) in triples:
            tmp_p = p.split("/")[-1]
            tmp_p = f"wdt:{tmp_p}"
            if not is_wikidata_entity_iri(o):
              triple_pattern.append(f"?x {tmp_p} '{o}'")
            else:
              tmp_o = o.split("/")[-1]
              tmp_o = f"wd:{tmp_o}"
              triple_pattern.append(f"?x {tmp_p} {tmp_o}")
        else:
          # dbpedia
          triple_pattern = []
          for (_, p, o) in triples:
            if is_dbpedia_entity_iri(o):
              tmp_p, tmp_o = replace_prefix_dbpedia(p), replace_prefix_dbpedia(o)
              triple_pattern.append(f"?x {tmp_p} {tmp_o}")
            else:
              tmp_p = replace_prefix_dbpedia(p)
              triple_pattern.append(f"?x {tmp_p} '{o}'")
      else:
        triple_pattern = [
            f"?x <{p}> '{o}'" if isinstance(o, Literal) else f"?x <{p}> <{o}>"
            for (_, p, o) in triples
        ]
      triple_pattern = " . ".join(triple_pattern) + " ."
      query = f"select ?x {{ {triple_pattern} }}"
      mapping = {}
      for (_, p, o) in triples:
        if is_wikidata_entity_iri(o) or is_dbpedia_entity_iri(o):
          p_label, o_label = self.__get_label(p), self.__get_label(o)
        else:
          p_label, o_label = self.__get_label(p), o
        mapping[p] = p_label
        mapping[o] = o_label
      refined_question = self.__refine_question(mapping, query)
      return refined_question, query

    elif category == '2':
      # pattern: ?x a ?y . ?y b c .
      # make sure to prevent object as literal and make sure the object has at least one property
      # excluding the properties mentioned in exclude list
      # kadang ada yg tidak ketemu match, harus repeat
      if not self.is_api:
        # search such that the first triple is not literal as the object
        while self.__is_no_property(starting_triple[2]):
          starting_triple = self.__get_one_triple()
      else:
        # assume that the depth is quite good
        if "wikidata" in self.source:
          while not is_wikidata_entity_iri(starting_triple[2]):
            starting_triple = self.__get_one_triple()
        else:
          # dbpedia
          while not is_dbpedia_entity_iri(starting_triple[2]):
            starting_triple = self.__get_one_triple()
      triples = []
      triples.append(starting_triple)

      if self.is_api:
        if "wikidata" in self.source:
          # no literal for easiness of searching
          while len(triples) <= depth:
            triple = self.__get_one_triple(triples[-1][2])
            while not is_wikidata_entity_iri(triple[2]):
              triple = self.__get_one_triple(triples[-1][2])
            triples.append(triple)
        else:
          #dbpedia
          while len(triples) <= depth:
            triple = self.__get_one_triple(triples[-1][2])
            while not is_dbpedia_entity_iri(triple[2]):
              triple = self.__get_one_triple(triples[-1][2])
            triples.append(triple)
      else:
        triple = starting_triple
        while len(triples) < depth and not isinstance(triple[2], Literal):
          triple = self.__get_one_triple(triples[-1][2])
          triples.append(triple)

      triple_pattern = []
      curr_var = "x"
      if not self.is_api:
        for i in range(len(triples)):
          p = triples[i][1]
          o = triples[i][2]
          if i == len(triples) - 1:
            triple_pattern.append(f"?{curr_var} <{p}> '{o}'" if isinstance(o, Literal) else f"?{curr_var} <{p}> <{o}>")
          else:
            triple_pattern.append(f"?{curr_var} <{p}> ?{get_next_variable(curr_var)}")
          curr_var = get_next_variable(curr_var)
        triple_pattern = " . ".join(triple_pattern) + " ."
      else:
        if "wikidata" in self.source:
          for i in range(len(triples)):
            prop = triples[i][1].split("/")[-1]
            prop = "wdt:" + prop
            if i == len(triples) - 1:
              obj = triples[i][2]
              obj = f"'{obj}'" if not is_wikidata_entity_iri(obj) else "wd:" + obj.split("/")[-1]
              triple_pattern.append(f"?{curr_var} {prop} {obj}")
            else:
              triple_pattern.append(f"?{curr_var} {prop} ?{get_next_variable(curr_var)}")
            curr_var = get_next_variable(curr_var)
          triple_pattern = " . ".join(triple_pattern) + " ."
        else:
          for i in range(len(triples)):
            if i == len(triples) - 1:
              obj = triples[i][2]
              if is_dbpedia_entity_iri(obj):
                obj = replace_prefix_dbpedia(obj)
              else:
                obj = f"'{obj}'"
              triple_pattern.append(f"?{curr_var} {replace_prefix_dbpedia(triples[i][1])} {obj}")
            else:
              triple_pattern.append(f"?{curr_var} {replace_prefix_dbpedia(triples[i][1])} ?{get_next_variable(curr_var)}")
            curr_var = get_next_variable(curr_var)
          triple_pattern = " . ".join(triple_pattern) + " ."
      query = f"select ?x {{ {triple_pattern} }}"
      mapping = {}
      for i in range(len(triples)):
        s, p, o = triples[i]
        p_label, o_label = self.__get_label(p), self.__get_label(o)
        mapping[p] = p_label
        mapping[o] = o_label
      refined_question = self.__refine_question(mapping, query)
      return refined_question, query

  def __random_pick_entity(self):
    if self.is_api:
      # cannot for loop and pick one here
      # we have to pick some predefined entities
      with open(self.classes_file, 'r') as f:
        category = f.read()
      provider = "dbp" if "dbpedia" in self.source else "wd"
      cleaned = category.strip().split("\n")
      options = []
      for row in cleaned:
        opt = row.split("\t")
        if provider == "dbp":
          options.append(opt[1].strip())
        else:
          options.append(opt[0].strip())
      picked = random.choice(options)
      if provider == "dbp":
        query_amount = f"""
        select (count(?s) as ?cnt) {{
          ?s a {picked} .
        }}
        """
        query = """
          select ?s {{
            ?s a {picked} .
          }} offset {offset} limit 1
          """
      else:
        query_amount = f"""
        select (count(?s) as ?cnt) {{
          ?s wdt:P31 {picked} .
        }}
        """
        query = """
          select ?s {{
            ?s wdt:P31 {picked} .
          }} offset {offset} limit 1
        """
      self.wrapper.setQuery(query_amount)
      self.wrapper.setReturnFormat(JSON)
      num = self.wrapper.query().convert()['results']['bindings'][0]['cnt']['value']

      self.wrapper.setQuery(query.format(picked=picked, offset=random.randint(0, int(num) - 1)))
      self.wrapper.setReturnFormat(JSON)
      result = self.wrapper.query().convert()['results']['bindings'][0]['s']['value']

      return result
    else:
      candidates = set()
      for (s, p, _) in self.graph:
        if p == RDF['type']:
          candidates.add(s)
      entity = random.choice(list(candidates))
      return entity