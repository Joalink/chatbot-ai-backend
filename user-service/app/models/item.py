from sqlmodel import SQLModel, Field

class Item(SQLModel, table=True):
    id: int = Field(default=None, nullable=False, primary_key=True)
    name: str
    description: str = None
    price: float