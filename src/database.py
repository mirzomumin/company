from typing import AsyncGenerator
from sqlalchemy.ext.asyncio import (
    async_sessionmaker,
    create_async_engine,
    AsyncSession,
    AsyncAttrs,
)
from sqlalchemy.orm import DeclarativeBase
from src.config import settings
from src.utils.mixins import AuditColumns, UUIDPrimaryKey


async_engine = create_async_engine(
    settings.DB_URL,
    pool_timeout=30,
    pool_recycle=1800,
    pool_size=10,
    max_overflow=5,
)
SessionLocal = async_sessionmaker(autocommit=False, autoflush=False, bind=async_engine)


async def get_session() -> AsyncGenerator[AsyncSession, None]:
    async with SessionLocal() as session:
        yield session


class Base(DeclarativeBase, AsyncAttrs, AuditColumns, UUIDPrimaryKey):
    pass
