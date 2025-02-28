from sqlalchemy import Column, Integer, String, Float
from app.config.db import Base

# from pydantic import BaseModel

class Item(Base):
    __tablename__ = "items"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    description = Column(String, index=True)
    price = Column(Float)
    tax = Column(Float, nullable=True)