from fastapi import FastAPI, Request, Form, Response
from fastapi.templating import Jinja2Templates
from fastapi.encoders import jsonable_encoder
import uvicorn
import os
from dotenv import load_dotenv

app = FastAPI()

templates = Jinja2Templates(directory='template')

@app.get('/')
async def index(request : Request):
    return templates.TemplateResponse('index.html' ,{'request': request})

@app.post('/get_answer')
async def get_answer(request:Request, questions: str=Form(...)):
    pass