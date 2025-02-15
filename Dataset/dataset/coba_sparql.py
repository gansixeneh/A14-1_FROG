from rdflib import Graph
import json

from FROG.few_shots import LEGAL_GENERATE_SPARQL_FEW_SHOTS

# Load the RDF graph
graph = Graph()
graph.parse('dataset/io/data-lex2kg.ttl')

with open('dataset/io/train.json') as f:
    json_data = json.load(f)

# Run the SPARQL query
legal_queries = {entry["input"]: entry["output"]["sparql"] for entry in LEGAL_GENERATE_SPARQL_FEW_SHOTS}

def execute_query(query):
    result = graph.query(query)
    return sorted([str(row[0]) for row in result])

# Compare results
for i in range(8):
    question = json_data["question"][str(i)]
    json_sparql = json_data["query"][str(i)]

    legal_sparql = legal_queries.get(question, None)

    print(f"Query {i}: {question}")
    print(f"Executing JSON SPARQL Query...")
    json_result = execute_query(json_sparql)
    print(f"JSON Result: {json_result}")

    if legal_sparql:
        print(f"Executing LEGAL SPARQL Query...")
        legal_result = execute_query(legal_sparql)
        print(f"LEGAL Result: {legal_result}")

        if json_result == legal_result:
            print("✅ Results MATCH")
        else:
            print("❌ Results MISMATCH")
    else:
        print("ℹ️ No LEGAL_GENERATE_SPARQL_FEW_SHOTS query for this question.")

    print("-" * 80)