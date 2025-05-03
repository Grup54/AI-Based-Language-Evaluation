import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv('GEMINI_API_KEY')
genai.configure(api_key=api_key)


# Model listesini al
models = genai.list_models()
for model in models:
    print(f"Model Name: {model.name}")
