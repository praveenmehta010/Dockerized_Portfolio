from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from routes.my_routes import routes

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"))
app.include_router(routes)