from rdflib import Graph
import rdflib

# Load RDF data from file
g = Graph()
g.parse("io/data-lex2kg.ttl", format="turtle")  # Replace with your actual file name

# Extract distinct properties and entities
properties = set()
entities = set()

for s, p, o in g:
    entities.add(s)  # Subjects are entities
    properties.add(p)  # Predicates are properties
    if isinstance(o, rdflib.URIRef):  # Objects can also be entities if they are URIs
        entities.add(o)

# Save to a file
output_file = "io/rdf_output.txt"

with open(output_file, "w", encoding="utf-8") as f:
    f.write("Distinct Properties:\n")
    f.write("\n".join(sorted(str(p) for p in properties)) + "\n\n")

    f.write("Distinct Entities:\n")
    f.write("\n".join(sorted(str(e) for e in entities)) + "\n")

print(f"Output saved to {output_file}")
