from fastapi import FastAPI
from app.routers import items
from app.config.db import Base, engine

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Mi first APP")

app.include_router(items.router, prefix="/items", tags=["items"])