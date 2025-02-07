from rdflib import Graph, URIRef, Namespace


def simplify_kg(input_file, output_file):

    g = Graph()
    g.parse(input_file, format="turtle")

    LEX2KG_O = Namespace("https://example.org/lex2kg/ontology/")

    daftar_pasal_nodes = set(g.subjects(predicate=LEX2KG_O.pasal))

    new_triples = []
    to_remove = []

    for daftar_pasal in daftar_pasal_nodes:
        for bab in g.subjects(predicate=LEX2KG_O.daftarPasal, object=daftar_pasal):
            for pasal in g.objects(subject=daftar_pasal, predicate=LEX2KG_O.pasal):
                new_triples.append((bab, LEX2KG_O.pasal, pasal))

        to_remove.extend(g.triples((daftar_pasal, None, None)))
        to_remove.extend(g.triples((None, None, daftar_pasal)))

    for triple in to_remove:
        g.remove(triple)

    for triple in new_triples:
        g.add(triple)

    g.serialize(destination=output_file, format="turtle")
    print(f"Modified KG saved to {output_file}")


simplify_kg("io/data-lex2kg.ttl", "io/data-lex2kg-modified-v1.ttl")
