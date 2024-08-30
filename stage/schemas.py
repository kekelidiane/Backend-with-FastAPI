from datetime import datetime
from pydantic import BaseModel
from typing import Optional


class Stage(BaseModel):
    post = str
    date_begin: Optional[datetime] = datetime.now()
    date_end: Optional[datetime] = datetime.now()
    duration = int
    domain = str
    entreprise = str
    remuneration_salary = float
    stage_type = str

    class Config:
        from_attributes = True

class StageCreate(BaseModel):
    post = str
    date_begin: Optional[datetime] = datetime.now()
    date_end: Optional[datetime] = datetime.now()
    duration = int
    domain = str
    entreprise = str
    remuneration_salary = float
    stage_type = str

    class Config:
        from_attributes = True

class StageUpdate(BaseModel):
    post: Optional[str] = None
    date_begin: Optional[datetime] = datetime.now()
    date_end: Optional[datetime] = datetime.now()
    duration: Optional[int] = None
    domain: Optional[str] = None
    entreprise: Optional[str] = None
    remuneration_salary: Optional[float] = None
    stage_type: Optional[str] = None

    class Config:
        from_attributes = True
