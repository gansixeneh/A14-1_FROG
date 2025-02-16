from rdflib import Graph
import json

from FROG.few_shots import LEGAL_GENERATE_SPARQL_FEW_SHOTS, LEGAL_EXTRACT_ENTITY_FEW_SHOTS

# Load the RDF graph
graph = Graph()
graph.parse('dataset/io/data-lex2kg.ttl')

with open('dataset/io/final_dataset/legal_train.json') as f:
    json_data = json.load(f)

extract_inputs = {entry["input"] for entry in LEGAL_EXTRACT_ENTITY_FEW_SHOTS}
generate_inputs = {entry["input"] for entry in LEGAL_GENERATE_SPARQL_FEW_SHOTS}

# Find differences
missing_in_generate = extract_inputs - generate_inputs
missing_in_extract = generate_inputs - extract_inputs

if not missing_in_generate and not missing_in_extract:
    print("✅ All inputs match between LEGAL_EXTRACT_ENTITY_FEW_SHOTS and LEGAL_GENERATE_SPARQL_FEW_SHOTS.")
else:
    print("⚠️ Differences found:")
    if missing_in_generate:
        print(f"Missing in LEGAL_GENERATE_SPARQL_FEW_SHOTS: {missing_in_generate}")
    if missing_in_extract:
        print(f"Missing in LEGAL_EXTRACT_ENTITY_FEW_SHOTS: {missing_in_extract}")

# Run the SPARQL query
legal_queries = {
    entry["input"]: json.loads(entry["output"])["sparql"] 
    if isinstance(entry["output"], str) else entry["output"]["sparql"]
    for entry in LEGAL_GENERATE_SPARQL_FEW_SHOTS
}


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
    # print(f"JSON Result: {json_result}")

    if legal_sparql:
        print(f"Executing LEGAL SPARQL Query...")
        legal_result = execute_query(legal_sparql)
        # print(f"LEGAL Result: {legal_result}")

        if json_result == legal_result:
            print("✅ Results MATCH")
            print(len(json_result))
        else:
            print("❌ Results MISMATCH")
    else:
        print("ℹ️ No LEGAL_GENERATE_SPARQL_FEW_SHOTS query for this question.")

    print("-" * 80)

with open('dataset/io/final_dataset/legal_test.json') as f:
    json_data_test = json.load(f)

# Test queries
for i in range(40):
    question = json_data_test["question"][str(i)]
    json_sparql = json_data_test["query"][str(i)]
    
    print(f"Query {i}: {question}")
    print(f"Executing JSON SPARQL Query...")
    json_result = execute_query(json_sparql)
    
    print(len(json_result))
    if len(json_result) == 0:
        print("❌ No query output")
    
    print("-" * 80)
    