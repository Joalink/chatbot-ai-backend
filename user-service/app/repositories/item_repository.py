from typing import Optional
from sqlmodel.ext.asyncio.session import AsyncSession
from sqlmodel import select
from app.models.item import Item

class ItemRepository:
    def __init__(self, db: AsyncSession):
        self.db = db

    async def get_item_by_id(self, item_id: int) -> Optional[Item]:
        statement = select(Item).where(Item.id == item_id)
        result = await self.db.execute(statement=statement)
        return result.scalar_one_or_none()

    async def create_item(self, item_data: dict) -> Item:
        item = Item(**item_data)
        self.db.add(item)
        await self.db.commit()
        await self.db.refresh(item)
        return item