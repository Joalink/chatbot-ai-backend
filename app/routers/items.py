from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
# from models.item import Item
from app.schemas.item import ItemCreate, ItemResponse
from app.crud.item import get_items, get_item, create_item, update_item, delete_item
from app.config.db import SessionLocal

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.get("/", response_model=list[ItemResponse])
def read_items(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return get_items(db, skip, limit)

@router.get("/{item_id}", response_model=ItemResponse)
def read_item(item_id: int, db: Session = Depends(get_db)):
    db_item = get_item((db, item_id))
    if db_item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return db_item

@router.post("/", response_model=ItemResponse)
def create_item(item: ItemCreate, db: Session = Depends(get_db)):
    return create_item(db, item)

@router.put("/{item_id}", response_model=ItemResponse)
def update_item(item_id: int, item: ItemCreate, db: Session = Depends(get_db)):
    db_item = update_item(db, item_id, item)
    if db_item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return db_item

@router.delete("/{item_id}", response_model=ItemResponse)
def delete_item(item_id: int, db: Session = Depends(get_db)):
    db_item = delete_item(db, item_id)
    if db_item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return db_item