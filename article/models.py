from datetime import datetime
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class Article(Base):
    __tablename__ = "articles"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    author = Column(String)
    content = Column(String)
    source = Column(String)
    date = Column(DateTime, default=datetime.now(), onupdate=datetime.now)
    # visuals = Column(String)  # Stocker comme str et gérer la conversion dans la sérialisation
