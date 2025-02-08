from rag import LegalGraphRAG

rag_engine = LegalGraphRAG(
    model_name="Qwen/Qwen2.5-3B-Instruct",
    max_new_tokens=1500,
    use_local_model=False,
    use_local_weaviate_client=False,
)

response = rag_engine.chat(
    "Apa teks dari UU tahun 2004 no 6 pasal 4 versi 2 Maret 2004 ayat 4?",
    verbose=1, use_cot=True, try_threshold=5
)
print(response)