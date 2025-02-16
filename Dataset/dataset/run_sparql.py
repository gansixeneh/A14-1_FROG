from rdflib import Graph
import json

from FROG.few_shots import LEGAL_GENERATE_SPARQL_FEW_SHOTS, LEGAL_EXTRACT_ENTITY_FEW_SHOTS

# Load the RDF graph
graph = Graph()
graph.parse('dataset/io/data-lex2kg.ttl')
    
result = graph.query("""
        select ?x { ?x lex2kg-o:mengubah ?law . ?law lex2kg-o:tanggal '2011-07-20'^^xsd:date . }             
""")

print(len(result))