from urllib import request
from fastapi import FastAPI
from fastapi.responses import HTMLResponse          # Macht eine rückgabe im HTml format möglich
from fastapi.templating import Jinja2Templates   # fast api klasse die den dynamischen änderung von html Datein ermöglicht 
from starlette.requests import Request             # Klasse um HTTP zu ermöglichen 
import random
import string

app = FastAPI()
templates = Jinja2Templates(directory="templates")                          #Erstellen der Instanz für Jinja2

def password_generator(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(length))                #Passwort generator
    return password

@app.get("/generate-password", response_class=HTMLResponse)
async def generate_password(length: int = 12):
    password = password_generator(length)
    return templates.TemplateResponse("passwort.html", {"request":request, "password": password})