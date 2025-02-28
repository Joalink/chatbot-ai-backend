from pydantic import BaseModel

class ItemCreate(BaseModel):
    name: str
    description: str = None
    price: float
    tax: float = None

class ItemResponse(BaseModel):
    id: int
    name: str
    description: str = None
    price: float
    tax: float = None

    class Config:
        from_attributes = True
