from rag import LegalGraphRAG

# Options:
# - Qwen/Qwen2.5-7B-Instruct
# - Qwen/Qwen2.5-3B-Instruct
# - deepseek-ai/DeepSeek-R1-Distill-Qwen-1.5B
# - TinyLlama/TinyLlama_v1.1
# - meta-llama/Llama-3.2-1B-Instruct
# - Qwen/Qwen2.5-1.5B-Instruct

rag_engine = LegalGraphRAG(
    model_name="Qwen/Qwen2.5-3B-Instruct",
    max_new_tokens=300,
    print_output=True,
    use_local_model=True,
    use_local_weaviate_client=False,
    device="mps:0",
)

# response = rag_engine.chat(
#     "Apa teks dari UU tahun 2004 no 6 pasal 4 versi 2 Maret 2004 ayat 4?",
#     use_cot=False, try_threshold=5, verbose=False
# )
# print(response)