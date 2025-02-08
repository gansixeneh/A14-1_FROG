from rag import LegalGraphRAG

# Options:
# - Qwen/Qwen2.5-7B-Instruct
# - Qwen/Qwen2.5-3B-Instruct
# - deepseek-ai/DeepSeek-R1-Distill-Qwen-1.5B

rag_engine = LegalGraphRAG(
    model_name="Qwen/Qwen2.5-3B-Instruct",
    max_new_tokens=300,
    print_output=True,
    use_local_model=True,
    use_local_weaviate_client=False,
)

response = rag_engine.chat(
    "Apa teks dari UU tahun 2004 no 6 pasal 4 versi 2 Maret 2004 ayat 4?",
    use_cot=False, try_threshold=5
)
print(response)