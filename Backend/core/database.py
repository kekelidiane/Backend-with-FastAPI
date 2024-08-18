from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker
from pydantic_settings import BaseSettings
import os

class Settings(BaseSettings):
    DATABASE_URL: str = os.getenv("DATABASE_URL", "postgresql+asyncpg://diane:dianePg19@localhost/siteDB")

settings = Settings()

DATABASE_URL = settings.DATABASE_URL

# Création de l'engine asynchrone
engine = create_async_engine(DATABASE_URL, echo=True)

# Configuration de sessionmaker pour les sessions asynchrones
SessionLocal = sessionmaker(
    bind=engine,
    class_=AsyncSession,
    expire_on_commit=False
)

# Fonction pour obtenir la session de base de données
async def get_db():
    async with SessionLocal() as session:
        try:
            yield session
        finally:
            await session.close()
            print("Good job. Connexion réussie !!!")

'''
# Exemple d'utilisation dans une fonction asynchrone
async def example_usage():
    async for db in get_db():
        pass
'''