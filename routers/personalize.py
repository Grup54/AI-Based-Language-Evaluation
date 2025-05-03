from fastapi import APIRouter, Request
from fastapi.responses import RedirectResponse
from fastapi.templating import Jinja2Templates
from services.gemini_api import generate_mcq_questions
from services.gemini_api import generate_mcq_questions_personalized
router = APIRouter()

templates = Jinja2Templates(directory="templates")

@router.get("/personalized_test")
async def personalized_test(request: Request):
    user_question_answer_data = request.app.state.question_answer_data

    questions = generate_mcq_questions_personalized(request.app.state.language, request.app.state.level, user_question_answer_data)
    print(questions)
    request.app.state.questions = questions
    return templates.TemplateResponse("test.html", {
        "request": request,
        "language": request.app.state.language,
        "level": request.app.state.level,
        "questions": questions
    })