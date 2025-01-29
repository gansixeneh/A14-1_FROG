from utils.api import DBPediaAPI
from verbalization.base import BaseVerbalization


class DBPediaVerbalization(BaseVerbalization):
    PO_TEMPLATE = """
select ?p ?o ?sLabel ?pLabel ?oLabel where {{
  <{entity}> ?p ?o .
  FILTER (
    strstarts(str(?p), "http://dbpedia.org/ontology/")
    && !contains(str(?p), "wiki")
    && (strstarts(str(?o), "http://dbpedia.org/") || isLiteral(?o))
    && ?p != <http://dbpedia.org/ontology/abstract>
  )
  FILTER (
    !isLiteral(?o) || (isLiteral(?o) && (lang(?o) = "en" || lang(?o) = ""))
  )
  
  OPTIONAL {{
    <{entity}> rdfs:label ?sLabel .
    FILTER(lang(?sLabel) = "en")
  }}
  
  OPTIONAL {{
    ?p rdfs:label ?pLabel .
    FILTER(lang(?pLabel) = "en")
  }}
  
  OPTIONAL {{
    ?o rdfs:label ?oLabel .
    FILTER(lang(?oLabel) = "en")
  }}
}}
"""
    SP_TEMPLATE = """
select ?s ?p ?sLabel ?pLabel ?oLabel where {{
  ?s ?p <{entity}> .
  FILTER (
    strstarts(str(?p), "http://dbpedia.org/ontology/")
    && !contains(str(?p), "wiki")
  )
  
  OPTIONAL {{
    ?s rdfs:label ?sLabel .
    FILTER(lang(?sLabel) = "en")
  }}
  
  OPTIONAL {{
    ?p rdfs:label ?pLabel .
    FILTER(lang(?pLabel) = "en")
  }}
  
  OPTIONAL {{
    <{entity}> rdfs:label ?oLabel .
    FILTER(lang(?oLabel) = "en")
  }}
}}
"""

    def __init__(
        self,
        model_name="jinaai/jina-embeddings-v3",
        model_kwargs={"trust_remote_code": True},
        query_model_encode_kwargs={},
        passage_model_encode_kwargs={},
    ) -> None:
        super().__init__(
            model_name,
            model_kwargs,
            query_model_encode_kwargs,
            passage_model_encode_kwargs,
        )
        self.api = DBPediaAPI()
