from fastapi import APIRouter
from fastapi.responses import HTMLResponse
from app.models.contact import Contact
from app.config.mongo_db_connection import contacts, projects

routes = APIRouter()

@routes.get("/", response_class=HTMLResponse)
async def start():
    return "Server is running"


@routes.get("/get-projects")
async def get_Projects():
    # Fetch the projects data
    projects_data = list(projects.find({}))

    for project in projects_data:
        project["_id"] = str(project["_id"])
    
    return projects_data
    

@routes.post('/contact', status_code=201)
def add_product(contactDetails : Contact):
    contacts.insert_one(dict(contactDetails))