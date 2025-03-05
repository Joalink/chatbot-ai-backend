from fastapi import FastAPI
from app.core.database import init_db
from app.api.v1.endpoints import items

app = FastAPI()

@app.on_event("startup")
def on_startup():
    init_db()

app.include_router(items.router, prefix="/items", tags=["items"])

@app.get("/")
def root():
    return {"message": "Hello, FastAPI!"}