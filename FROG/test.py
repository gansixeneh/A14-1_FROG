import os
from dotenv import load_dotenv

load_dotenv()

# Check if the token is loaded
print("Hugging Face Token:", os.getenv("HF_TOKEN"))