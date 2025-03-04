from rdflib import Graph, Literal


graph = Graph()
graph.parse("data-lex2kg.ttl")

property_uri = "https://example.org/lex2kg/ontology/disahkanDi"

incorrect_literals = {"Jakart", "Jakar", "Jakarta,", "D", "Djakarta"}

for subj, pred, obj in graph:
    if pred.endswith(property_uri) and isinstance(obj, Literal):
        if obj.value in incorrect_literals:
            graph.remove((subj, pred, obj))
            graph.add((subj, pred, Literal("Jakarta")))


graph.serialize(destination="modified_data-lex2kg.ttl", format="turtle")

print("Modifications completed and saved to modified_data-lex2kg.ttl")
