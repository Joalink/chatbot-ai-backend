from fastapi import FastAPI
from app.database.session import init_db
from app.routers import items

app = FastAPI()

@app.on_event("startup")
async def on_startup():
    await init_db()

app.include_router(items.router)

@app.get("/")
def root():
    return {"message": "Hello, FastAPI!"}