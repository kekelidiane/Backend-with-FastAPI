from datetime import datetime
from pydantic import BaseModel
from typing import Optional


class Event(BaseModel):
    title = str
    date_begin: Optional[datetime] = datetime.now()
    date_end: Optional[datetime] = datetime.now()
    duration = int
    location = str
    partners = str
    description = str
    participants = str

    class Config:
        from_attributes = True

class EventCreate(BaseModel):
    title = str
    date_begin: Optional[datetime] = datetime.now()
    date_end: Optional[datetime] = datetime.now()
    duration = int
    location = str
    partners = str
    description = str
    participants = str

    class Config:
        from_attributes = True

class EventUpdate(BaseModel):
    title: Optional[str] = None
    date_begin: Optional[datetime] = datetime.now()
    date_end: Optional[datetime] = datetime.now()
    duration: Optional[int] = None
    location: Optional[str] = None
    partners: Optional[str] = None
    description: Optional[str] = None
    participants: Optional[str] = None

    class Config:
        from_attributes = True
