from rdflib import Graph
import json

from FROG.few_shots import LEGAL_GENERATE_SPARQL_FEW_SHOTS, LEGAL_EXTRACT_ENTITY_FEW_SHOTS
from FROG.utils.helper import fix_query_spacing

# Load the RDF graph
graph = Graph()
graph.parse('dataset/io/data-lex2kg.ttl')
    
    
# query = "SELECT?referencedLaw WHERE { <https://example.org/lex2kg/uu/2018/6/pasal/0093/versi/20180807> lex2kg-o:merujuk?referencedLaw. }"
query = "SELECT?x WHERE {?x lex2kg-o:jenisVersi \"penyisipan\"^^xsd:string ; lex2kg-o:disahkanPada \"2020-11-02\"^^xsd:date. }"
query = fix_query_spacing(query)
print(query)

result = graph.query(query)

print(len(result))