from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from app.database.session import get_session
from app.schemas.item import ItemCreate, ItemResponse
from app.services.item_service import ItemService
from app.repositories.item_repository import ItemRepository


router = APIRouter(prefix="/items")

@router.get("/{item_id}")
async def get_item(item_id: int, db: AsyncSession = Depends(get_session)):
    item_repository = ItemRepository(db)
    item_service = ItemService(item_repository)
    item = await item_service.get_item(item_id)

    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    return item

@router.post("/", response_model=ItemResponse)
async def create_new_item(item_data: ItemCreate, db: AsyncSession = Depends(get_session)):
    item_repository = ItemRepository(db)
    item_service = ItemService(item_repository)
    return await item_service.create_item(item_data)
