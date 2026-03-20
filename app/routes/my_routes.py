from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from models.contact import Contact
# from models.project import Project
from config.mongo_db_connection import contacts, projects

routes = APIRouter()
templates = Jinja2Templates(directory="templates")

def fetch_projects():
    docs = list(projects.find({}))
    # print(docs)
    return docs

@routes.get("/", response_class=HTMLResponse)
async def read_item(request: Request):
    # Fetch the projects data
    projects = fetch_projects()
    return templates.TemplateResponse(
        request=request, name="index.html",
        # Pass the data to the template in a context dictionary
        context={"projects": projects}
    )
    
    

@routes.post('/contact', status_code=201)
def add_product(contactDetails : Contact):
    contacts.insert_one(dict(contactDetails))