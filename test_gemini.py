# test_gemini.py
from services.gemini_api import generate_mcq_questions
from dotenv import load_dotenv
import os
import google.generativeai as genai

load_dotenv()  # .env dosyasını yükler
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

if __name__ == "__main__":
    language = "English"
    level = "B1"

    questions = generate_mcq_questions(language, level)

    for i, q in enumerate(questions, start=1):
        print(f"\nQuestion {i}: {q['question']}")
        for opt in q['options']:
            print(f" - {opt}")
