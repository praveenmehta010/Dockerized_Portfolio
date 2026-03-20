from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from models.contact import Contact
from config.mongo_db_connection import contacts

routes = APIRouter()
templates = Jinja2Templates(directory="templates")
    

@routes.get("/", response_class=HTMLResponse)
async def read_item(request: Request):
    return templates.TemplateResponse(
        request=request, name="index.html"
    )

@routes.post('/contact', status_code=201)
def add_product(contactDetails : Contact):
    contacts.insert_one(dict(contactDetails))