from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from app.schemas.item import ItemCreate, ItemResponse
from app.services.item import create_item, get_items
from app.core.database import get_session

router = APIRouter()

@router.post("/", response_model=ItemResponse)
async def create_new_item(item: ItemCreate, db: AsyncSession = Depends(get_session)):
    return await create_item(db, item)

@router.get("/", response_model=list[ItemResponse])
async def list_items(db: AsyncSession = Depends(get_session)):
    return await get_items(db)