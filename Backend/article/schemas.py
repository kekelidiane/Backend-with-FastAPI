from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime


class ArticleCreate(BaseModel):
    id_article: int
    title: str
    author: str
    content: str
    source: Optional[str] = None
    date: Optional[datetime] = None

    class Config:
        from_attributes = True

class ArticleUpdate(BaseModel):
    title: Optional[str] = None
    author: Optional[str] = None
    content: Optional[str] = None
    source: Optional[str] = None
    date: Optional[datetime] = None

    class Config:
        from_attributes = True
