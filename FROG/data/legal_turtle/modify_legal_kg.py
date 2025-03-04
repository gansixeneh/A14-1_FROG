from rdflib import Graph, Literal, URIRef, Namespace
import datetime


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
    if isinstance(subj, URIRef) and subj.endswith("/text") and pred.endswith("merujuk"):
        new_subj = URIRef(str(subj).replace("/text", ""))
        graph.remove((subj, pred, obj))
        graph.add((new_subj, pred, obj))

    # Remove all triples with lex2kg-o:bagianDari
    if pred.endswith("bagianDari"):
        graph.remove((subj, pred, obj))

    if pred.endswith("jabatanPengesah"):
        if obj.value == "Diundangkan di Jakarta":
            new_obj = Literal('MENTERI HUKUM DAN HAK AZASI MANUSIA REPUBLIK INDONESIA')
        elif obj.value == "WAKIL PRESIDEN REPUBLIK INDONESIA,":
            new_obj = Literal("WAKIL PRESIDEN REPUBLIK INDONESIA")
        else:
            new_obj = Literal("PRESIDEN REPUBLIK INDONESIA")
            
        graph.remove((subj, pred, obj))
        graph.add((subj, pred, new_obj))

lex2kg_o = Namespace("https://example.org/lex2kg/ontology/")


# Connect entities directly without using the "daftar" entity
def connect_triples(p: str):
    property_uri = URIRef(str(lex2kg_o) + p)
    for s, _, o in graph.triples((None, property_uri, None)):
        graph.remove((s, property_uri, o))
        new_s = URIRef(str(s).replace(f"/{p}", ""))
        graph.add((new_s, property_uri, o))

    property_uri = URIRef(f"{lex2kg_o}daftar{p.capitalize()}")
    for s, _, o in graph.triples((None, property_uri, None)):
        graph.remove((s, property_uri, o))


connect_triples("ayat")
connect_triples("bab")
connect_triples("bagian")
connect_triples("huruf")
connect_triples("paragraf")

# Find entities that appear only as subjects in type declarations
candidates_for_removal = set()
non_removable_entities = set()
a_label = "http://www.w3.org/1999/02/22-rdf-syntax-ns#type"

for s, p, o in graph:
    if p == URIRef(a_label):
        candidates_for_removal.add(s)
    else:
        non_removable_entities.add(s)
        non_removable_entities.add(o)

candidates_for_removal -= non_removable_entities
for entity in candidates_for_removal:
    graph.remove((entity, None, None))

print(f"Removed {len(candidates_for_removal)} entities.")


graph.serialize(destination="modified_data-lex2kg.ttl", format="turtle")

print("Modifications completed and saved to modified_data-lex2kg.ttl")
