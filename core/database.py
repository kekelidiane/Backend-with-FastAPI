from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker
from pydantic_settings import BaseSettings
import os
from dotenv import load_dotenv
from gino import Gino

load_dotenv()       # Charger les variables d'environnement du fichier .env

db = Gino()     # Initialiser la base de données avec Gino

class Settings(BaseSettings):
    DATABASE_URL = os.getenv("DATABASE_URL")        # Accéder aux variables d'environnement

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
