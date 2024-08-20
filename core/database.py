from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker
from pydantic_settings import BaseSettings
import os

class Settings(BaseSettings):
    DATABASE_URL: str = os.getenv("DATABASE_URL", "postgresql+asyncpg://diane:dianePg19@localhost/siteDB")

settings = Settings()

DATABASE_URL = settings.DATABASE_URL

engine = create_async_engine(DATABASE_URL)  # Création de l'engine asynchrone

SessionLocal = sessionmaker(    # Configuration de sessionmaker pour les sessions asynchrones
    autocommit=False,
    autoflush=False,
    bind=engine,
    class_=AsyncSession,
    expire_on_commit=False
)

async def get_db(): # Fonction pour obtenir la session de base de données
        async with SessionLocal() as db:
            try:
                yield db
            finally:
                await db.close()
