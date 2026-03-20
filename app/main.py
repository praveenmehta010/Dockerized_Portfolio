from fastapi import FastAPI
from config.mongo_db_connection import projects

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get('/project/{title}')
def get_project_by_title(title : str):
    # Manual testing
    # Query for a Project that has the title 'Back to the Future'
    query = { "title": title }
    project = projects.find_one(query)
    print(project)
    