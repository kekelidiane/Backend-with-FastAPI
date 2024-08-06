from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker
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

    async def get_db():
        try:
            db = SessionLocal()
            yield db
        finally:
            print("Good job. Connexion réussie !!!")
            await db.close()


except Exception as e:
    print(f"Erreur de connexion : {e}")

