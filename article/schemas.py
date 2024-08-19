from pydantic import BaseModel
from typing import Optional
from datetime import datetime


class ArticleCreate(BaseModel):
    title: str
    author: str
    content: str
    source: Optional[str] = "Unknown"
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
