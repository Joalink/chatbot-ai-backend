from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from app.models.item import Item
from app.schemas.item import ItemCreate

async def create_item(db: AsyncSession, item_data: ItemCreate):
    new_item = Item(**item_data.dict())
    db.add(new_item)
    await db.commit()
    await db.refresh(new_item)
    return new_item

async def get_items(db: AsyncSession):
    result = await db.execute(select(Item))
    return result.scalars().all()
