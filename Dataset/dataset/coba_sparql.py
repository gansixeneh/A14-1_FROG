from rdflib import Graph

# Load the RDF graph
graph = Graph()
graph.parse('dataset/io/data-lex2kg.ttl')

# Run the SPARQL query
query_result = graph.query("""
    SELECT DISTINCT ?o WHERE {
    ?s ?p ?o .
    FILTER(
        STR(?p) = "https://example.org/lex2kg/ontology/yurisdiksi"
    )
}
LIMIT 10


""")

# Print the results
for row in query_result:
    print(row)
