from fastapi import APIRouter, Request
from fastapi.responses import RedirectResponse
from fastapi.templating import Jinja2Templates
from services.gemini_api import generate_mcq_questions
from services.gemini_api import generate_mcq_questions_personalized
router = APIRouter()

templates = Jinja2Templates(directory="templates")


@router.post("/test")
async def get_test(request: Request):
    form_data = await request.form()
    print(form_data)
    language = form_data.get("language","English")
    level = form_data.get("level", "A1")
    questions = generate_mcq_questions(language, level)
    print(questions)
    request.app.state.questions = questions
    request.app.state.language = language
    request.app.state.level = level
    return templates.TemplateResponse("test.html", {
        "request": request,
        "language": language,
        "level": level,
        "questions": questions
    })


@router.post("/submit_test")
async def submit_test(request: Request):
    form_data = await request.form()

    # Get user answers
    user_answers = [form_data.get(f"q{i}") for i in range(0, 15)]

    # Combine questions with user answers and correct answers
    question_answer_data = [
        {
            "question": question['question'],
            "options": question['options'],
            "user_answer": user_answers[i],
            "correct_answer": question['correct_answer'],
        }
        for i, question in enumerate(request.app.state.questions)
    ]
    request.app.state.question_answer_data = question_answer_data
    score = sum(1 for q in question_answer_data if q["user_answer"] == q["correct_answer"])

    return templates.TemplateResponse("result.html", {
        "request": request,
        "score": score,
        "total": len(question_answer_data),
        "language": request.app.state.language,
        "level": request.app.state.level,
        "question_answer_data": question_answer_data,
    })