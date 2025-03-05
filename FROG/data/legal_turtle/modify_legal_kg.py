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
    
    # Correct jabatanPengesah literals
    if pred.endswith("jabatanPengesah"):
        if obj.value == "Diundangkan di Jakarta":
            new_obj = Literal('Menteri Hukum dan Hak Azasi Manusia Republik Indonesia')
        elif obj.value == "WAKIL PRESIDEN REPUBLIK INDONESIA,":
            new_obj = Literal("Wakil Presiden Republik Indonesia")
        else:
            new_obj = Literal("Presiden Republik Indonesia")
            
        graph.remove((subj, pred, obj))
        graph.add((subj, pred, new_obj))
    
    # Correct disahkanOleh literals
    if pred.endswith("disahkanOleh"):
        mapping = {
            "JOKO WIDODO": "Joko Widodo",
            "DR. H. SUSILO BAMBANG YUDHOYONO": "DR. H. Susilo Bambang Yudhoyono",
            "DR.H. SUSILO BAMBANG YUDHOYONO": "DR. H. Susilo Bambang Yudhoyono",
            "MEGAWATI SOEKARNOPUTRI": "Megawati Soekarnoputri",
            "MEGAWATI SOEFKARNOPUTRI": "Megawati Soekarnoputri",
            "MEGAWATI SOEKARNOP UTRI": "Megawati Soekarnoputri",
            "ABDURRAHMAN WAHID": "Abdurrahman Wahid",
            "BACHARUDDIN JUSUF HABIBIE": "Bacharuddin Jusuf Habibie",
            "BACHRUDDIN JUSUF HABIBIE": "Bacharuddin Jusuf Habibie",
            "SOEHARTO": "Soeharto",
            "S0EHARTO": "Soeharto",
            "SOEHARTO.": "Soeharto",
            "SOEHAR TO": "Soeharto",
            "JENDERAL TNI": "Jenderal TNI",
            "JENDERAL TNI.": "Jenderal TNI",
            "JENDERAL TNI .": "Jenderal TNI",
            "JENDERAL T.N.I.": "Jenderal TNI",
            "JENDERAL - TNI": "Jenderal TNI",
            "Jenderal TNI": "Jenderal TNI",
            "Jenderal T NI": "Jenderal TNI",
            "SUKARNO": "Soekarno",
            "SUKARNO.": "Soekarno",
            "SOEKARNO": "Soekarno",
            "SOEKARNO.": "Soekarno",
            "PERDANA MENTERI,": "Soekarno",
            "MOHAMMAD HATTA": "Mohammad Hatta",
            "ASSAAT.": "Assaat",
            "ASSAAT": "Assaat",
            "MENTERI HUKUM DAN HAK AZASI MANUSIA": "Hamid Awaludin",
            "Diundangkan": "unknown",
            "Diundangkan di Jakarta": "unknown",
            "ttd.": "unknown",
            "ttd": "unknown",
            "LEMBARAN NEGARA REPUBLIK INDONESIA TAHUN 2003 NOMOR 155": "unknown",
            "LEMBARAN NEGARA REPUBLIK INDONESIA TAHUN 2003 NOMOR 153": "unknown",
            "LEMBARAN NEGARA REPUBLIK INDONESIA TAHUN 2003 NOMOR 115": "unknown",
        }
           
        graph.remove((subj, pred, obj))
        graph.add((subj, pred, Literal(mapping[obj.value])))

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
