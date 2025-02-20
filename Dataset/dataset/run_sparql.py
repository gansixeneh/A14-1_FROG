from rdflib import Graph
import json

from FROG.few_shots import LEGAL_GENERATE_SPARQL_FEW_SHOTS, LEGAL_EXTRACT_ENTITY_FEW_SHOTS

# Load the RDF graph
graph = Graph()
graph.parse('dataset/io/data-lex2kg.ttl')
    
result = graph.query("""
        select ?x where {?x lex2kg-o:merujuk ?y . ?y lex2kg-o:disahkanDi "Jogjakarta" . }            
""")

print(len(result))