from fastapi import APIRouter, Request, Form
from fastapi.templating import Jinja2Templates
from services.test_generator import generate_personalized_test
from fastapi.responses import HTMLResponse

router = APIRouter()
templates = Jinja2Templates(directory="templates")

@router.post("/test/personalized", response_class=HTMLResponse)
async def personalized_test(request: Request):
    # Placeholder: Generate test based on weaknesses
    questions = generate_personalized_test("English", "B1")
    return templates.TemplateResponse("test.html", {"request": request, "questions": questions, "language": "English", "level": "B1"})
