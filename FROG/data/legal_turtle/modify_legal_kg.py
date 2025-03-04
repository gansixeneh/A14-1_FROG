from rdflib import Graph, Literal, URIRef


graph = Graph()
graph.parse("data-lex2kg.ttl")


for subj, pred, obj in graph:
    # Fix inconsistent city names on lex2kg-o:disahkanDi
    if pred.endswith("disahkanDi") and isinstance(obj, Literal):
        incorrect_literals = {"Jakart", "Jakar", "Jakarta,", "D", "Djakarta"}
        if obj.value in incorrect_literals:
            graph.remove((subj, pred, obj))
            graph.add((subj, pred, Literal("Jakarta")))

    # Remove unnecessary /text suffix on lex2kg-o:merujuk
    if isinstance(subj, URIRef) and subj.endswith("/text"):
        new_subj = URIRef(str(subj).replace("/text", ""))
        graph.remove((subj, pred, obj))
        graph.add((new_subj, pred, obj))

    # Remove all triples with lex2kg-o:bagianDari
    if pred.endswith("bagianDari"):
        graph.remove((subj, pred, obj))

graph.serialize(destination="modified_data-lex2kg.ttl", format="turtle")

print("Modifications completed and saved to modified_data-lex2kg.ttl")
