from rdflib import Graph

# Load the RDF graph
graph = Graph()
graph.parse('dataset/io/data-lex2kg.ttl')

# Run the SPARQL query
query_result = graph.query("""
    SELECT DISTINCT ?a  WHERE {
    ?b lex2kg-o:jenisVersi ?a .
}

""")

# Print the results
for row in query_result:
    print(row)
