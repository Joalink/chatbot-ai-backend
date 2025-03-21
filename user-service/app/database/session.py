import os
from dotenv import load_dotenv
from sqlmodel import SQLModel, create_engine
from sqlalchemy.ext.asyncio import AsyncSession, AsyncEngine, async_sessionmaker

load_dotenv()
DATABASE_URL = os.getenv("DATABASE_URL")

engine = AsyncEngine(create_engine(DATABASE_URL, echo=True, future=True))

async def init_db():
    async with engine.begin() as conn:
        await conn.run_sync(SQLModel.metadata.create_all)

async_session = async_sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)

async def get_session():
    async with async_session() as session:
        yield session