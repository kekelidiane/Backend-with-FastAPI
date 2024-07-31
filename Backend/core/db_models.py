from sqlalchemy import Column, Integer, String, DateTime
from .database import Base

class Table_Article(Base):
    __tablename__ = "articles"
    id = Column(Integer, primary_key=True, index=True)
    id_article = Column(String, unique=True, index=True)
    author = Column(String)
    content = Column(String)
    source = Column(String)
    title = Column(String)
    date = Column(DateTime)
    visuals = Column(String)  # Stocker comme str et gérer la conversion dans la sérialisation
