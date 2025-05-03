# services/gemini_api.py
import google.generativeai as genai
import ast

import json
import os
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv('GEMINI_API_KEY')
genai.configure(api_key=api_key)


def generate_mcq_questions(language: str, level: str) -> list:
    prompt = f"""
    Generate exactly 15 multiple-choice questions for a {language} language proficiency test at level {level}.

Each question should be a dictionary with these keys:
- 'question': a string,
- 'options': a list of 4 strings (multiple choices),
- 'correct_answer': one of the options (the correct one).



Respond ONLY with a valid JSON array.
- The array must start with [ and end with ]
- Do NOT include any variable names (e.g., do not write 'questions = ...')
- Do NOT include any Markdown, explanation, or code formatting

Example format:
[
  {{
    "question": "What is the capital of France?",
    "options": ["Paris", "London", "Berlin", "Madrid"],
    "correct_answer": 'Paris'
  }},
  ...
]
"""
    model = genai.GenerativeModel("models/gemini-1.5-pro")
    response = model.generate_content(prompt)



    try:
        questions = json.loads(response.text)
        return questions
    except json.JSONDecodeError as e:
        print("JSON parsing error:", e)
        print("Raw response:\n", response.text)
        return []


def generate_mcq_questions_personalized(language: str, level: str, user_question_answer_data: list) -> list:
    prompt = f"""
  You are an intelligent language tutor creating a personalized {language} language proficiency test at level {level}.

  The user has previously answered 15 questions. Below are the original questions, the correct answers, and the user's responses:

  Questions and answers:
  {json.dumps([
        {
            "question": q["question"],
            "options": q["options"],
            "correct_answer": q["correct_answer"],
            "user_answer": q["user_answer"]
        } for q in user_question_answer_data
    ], indent=2)}

  Based on this information:

Identify which types of questions or grammar areas the user struggles with.
Create exactly 15 new multiple-choice questions that are similar in level but focus more on the concepts the user got wrong.
Each question must have:
'question': a string
'options': a list of 4 strings
'correct_answer': one of the options

  Respond ONLY with a valid JSON array.

The array must start with [ and end with ]
Do NOT include any variable names
Do NOT include any Markdown or explanation

  Example format:
  [
    {{
      "question": "What is the capital of France?",
      "options": ["Paris", "London", "Berlin", "Madrid"],
      "correct_answer": "Paris"
    }},
    ...
  ]
  """
    model = genai.GenerativeModel("models/gemini-1.5-pro")
    response = model.generate_content(prompt)

    try:
        questions = json.loads(response.text)
        return questions
    except json.JSONDecodeError as e:
        print("JSON parsing error:", e)
        print("Raw response:\n", response.text)
        return []