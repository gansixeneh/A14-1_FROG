from rdflib import Graph

# Load the RDF graph
graph = Graph()
graph.parse('dataset/io/data-lex2kg.ttl')

# Run the SPARQL query
query_result = graph.query("""
    SELECT ?p ?q WHERE {
    ?s ?p ?o .
    BIND(STR(?p) AS ?q)
    FILTER(
        STR(?p) = "https://example.org/lex2kg/ontology/paragraf" ||
        STR(?p) = "https://example.org/lex2kg/ontology/ayat"
    )
}
LIMIT 10


""")

# Print the results
for row in query_result:
    print(f"p: {row.p}, q: {row.q}")
