from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import requests
import os
from dotenv import load_dotenv

# Load environment variables from the .env file (if present)
load_dotenv()

BACKEND_URL = os.getenv("BACKEND_URL")
PROFILE_IMAGE_URL = os.getenv("PROFILE_IMAGE_URL")

app = FastAPI()

app.mount("/static", StaticFiles(directory="app/static"), name="static")

templates = Jinja2Templates(directory="app/templates")

@app.get("/", response_class=HTMLResponse)
async def read_item(request: Request):
    response = requests.get(f"{BACKEND_URL}:7000/get-projects")
    projects = response.json()
    return templates.TemplateResponse(
        request=request, name="index.html",
        # Pass the data to the template in a context dictionary
        context={"projects": projects, "PROFILE_IMAGE_URL" : PROFILE_IMAGE_URL}
    )


@app.post("/contact")
async def contact(request: Request):
    data = await request.json()
    requests.post(
        f"{BACKEND_URL}:7000/contact",
        json=data
    )