from sqlmodel import SQLModel

class ItemCreate(SQLModel):
    name: str
    description: str = None
    price: float

class ItemResponse(ItemCreate):
    id: int