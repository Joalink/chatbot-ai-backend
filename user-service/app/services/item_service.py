from app.repositories.item_repository import ItemRepository, Item
from typing import Optional
from app.schemas.item import ItemCreate, ItemResponse

class ItemService:
    def __init__(self, item_repository: ItemRepository):
        self.item_repository = item_repository

    async def get_item(self, item_id: int) -> Optional[Item]:
        return await self.item_repository.get_item_by_id(item_id)

    async def create_item(self, item_data: ItemCreate) -> Item:
        item_dict = item_data.dict()
        return await self.item_repository.create_item(item_dict)