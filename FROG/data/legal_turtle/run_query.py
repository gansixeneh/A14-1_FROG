from rdflib import Graph
import json

graph = Graph()
graph.parse('data-lex2kg.ttl')

query = "select distinct ?x { ?a lex2kg-o:disahkanOleh ?x . }"

result = graph.query(query)

for x in result:
    print(x)