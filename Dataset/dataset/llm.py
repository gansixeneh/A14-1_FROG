import os
from langchain_community.llms import HuggingFaceHub
from langchain_huggingface import ChatHuggingFace
import warnings
from dotenv import load_dotenv

load_dotenv()

warnings.filterwarnings("ignore")

token = os.getenv('HF_TOKEN')

model_kwargs = {
    "device": False,
    "max_new_tokens": 1500,
    "return_full_text": False,
}

llm = HuggingFaceHub(repo_id="Qwen/Qwen2.5-3B-Instruct", model_kwargs=model_kwargs, huggingfacehub_api_token=token)
chat_model = ChatHuggingFace(llm=llm)

