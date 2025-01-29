import warnings
from util import get_next_variable, is_dbpedia_entity_iri, is_wikidata_entity_iri, replace_prefix_dbpedia, replace_prefix_wikidata
from llm import chat_model
from typing import List
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
  def __init__(self, source: str, excluded_props: List[str], timeout = 40):
    self.source = source
    self.excluded_props = excluded_props
    self.timeout = timeout
    self.graph = None
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
    print(prompt)
    result = chat_model.invoke(prompt).content
    if "Here" in result:
      matched = re.search(r'"(.*?)"', result, re.DOTALL)
      if matched:
        return matched.group(1)
      else:
        return result
    return result

  def __get_label(self, entity):
      try:
        query = f"""
          select ?lit {{
            <{entity}> rdfs:label ?lit .
          }}
        """
        result = list(self.graph.query(query))[0][0].toPython()
        return result
      except:
        # if literal
        result = entity.toPython()
        if type(result) is str:
          return result
        elif type(result) is int:
          return f"{result}^^xsd:integer"

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
    query_uri = "select ?x {{ <{s}> <{p}> ?x . }}"
    query_uri_reverse = "select ?x {{ ?x <{p}> {o} . }}"

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
        triples.add(triple)

      triple_pattern = []
      for (_, p, o) in triples:
        if isinstance(o, Literal):
          result = o.toPython()
          if type(result) is str:
            triple_pattern.append(f"?x <{p}> '{o}'")
          elif type(result) is int:
            triple_pattern.append(f"?x <{p}> '{o}'^^xsd:integer")
        else:
          triple_pattern.append(f"?x <{p}> <{o}>")

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
      # search such that the first triple is not literal as the object
      while self.__is_no_property(starting_triple[2]):
        starting_triple = self.__get_one_triple()
      triples = []
      triples.append(starting_triple)

      triple = starting_triple
      while len(triples) < depth and not isinstance(triple[2], Literal):
        triple = self.__get_one_triple(triples[-1][2])
        triples.append(triple)

      triple_pattern = []
      curr_var = "x"
      for i in range(len(triples)):
        p = triples[i][1]
        o = triples[i][2]
        if i == len(triples) - 1:
          if isinstance(o, Literal):
            result = o.toPython()
            if isinstance(result, str):
              triple_pattern.append(f"?{curr_var} <{p}> '{o}'")
            elif isinstance(result, int):
              triple_pattern.append(f"?{curr_var} <{p}> '{o}'^^xsd:integer")
          else:
            triple_pattern.append(f"?{curr_var} <{p}> <{o}>")
        else:
          triple_pattern.append(f"?{curr_var} <{p}> ?{get_next_variable(curr_var)}")
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
    candidates = set()
    for (s, p, _) in self.graph:
      if p == RDF['type']:
        candidates.add(s)
    entity = random.choice(list(candidates))
    return entity