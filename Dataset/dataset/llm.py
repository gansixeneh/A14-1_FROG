import os
from langchain_community.llms import HuggingFaceHub
from langchain_huggingface import ChatHuggingFace
import warnings
from dotenv import load_dotenv
from transformers import AutoTokenizer, AutoModelForCausalLM, pipeline
from langchain_huggingface.llms import HuggingFacePipeline

load_dotenv()

warnings.filterwarnings("ignore")

HF_TOKEN = os.getenv('HF_TOKEN')

# model_kwargs = {
#     "device": False,
#     "max_new_tokens": 1500,
#     "return_full_text": False,
# }

# llm = HuggingFaceHub(repo_id="Qwen/Qwen2.5-3B-Instruct", model_kwargs=model_kwargs, huggingfacehub_api_token=token)
# chat_model = ChatHuggingFace(llm=llm)

model_name = "Qwen/Qwen2.5-3B-Instruct"

tokenizer = AutoTokenizer.from_pretrained(model_name, token=HF_TOKEN)
model = AutoModelForCausalLM.from_pretrained(model_name, token=HF_TOKEN)

pipe = pipeline(
    "text-generation",
    model=model,
    tokenizer=tokenizer,
    device_map="auto",
    max_new_tokens=1500,
    return_full_text=False,
)
llm = HuggingFacePipeline(pipeline=pipe)
chat_model = ChatHuggingFace(llm=llm)
                