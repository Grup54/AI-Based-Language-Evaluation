# services/test_generator.py
from services.gemini_api import generate_mcq_questions

def generate_test(language: str, level: str):
    return generate_mcq_questions(language, level)

def generate_personalized_test(language: str, level: str):
    # Later you can enhance this to analyze user's previous results
    return generate_test(language, level)
