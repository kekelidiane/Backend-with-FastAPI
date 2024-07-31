from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from pydantic_settings import BaseSettings
import os

class Settings(BaseSettings):

    DATABASE_URL: str = os.getenv("DATABASE_URL", "postgresql+asyncpg://diane:dianePg19@localhost/siteDB")

settings = Settings()

DATABASE_URL = settings.DATABASE_URL

try:
    engine = create_async_engine(DATABASE_URL)
    SessionLocal = sessionmaker(
        bind=engine,
        class_=AsyncSession,
        expire_on_commit=False
    )

    Base = declarative_base()

    async def get_db():
        db = SessionLocal()
        try:
            yield db
        finally:
            print("Good job. Connexion réussie !!!")
            await db.close()


except Exception as e:
    print(f"Erreur de connexion : {e}")

async def init_db():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
