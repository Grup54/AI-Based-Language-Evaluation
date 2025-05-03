# main.py
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from routers import home, test, personalize
from dotenv import load_dotenv
load_dotenv()


app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

app.include_router(home.router)
app.include_router(test.router)
app.include_router(personalize.router)
