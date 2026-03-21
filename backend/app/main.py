from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from app.routes.my_routes import routes

app = FastAPI()

app.include_router(routes)