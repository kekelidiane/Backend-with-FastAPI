from datetime import datetime
from pydantic import BaseModel
from typing import Optional


class Program(BaseModel):
    name: str
    date_begin: Optional[datetime] = datetime.now()
    date_end: Optional[datetime] = datetime.now()
    duration: int
    program_type: str
    partners: str
    description: str

    class Config:
        from_attributes = True

class ProgramCreate(BaseModel):
    name: str
    date_begin: Optional[datetime] = datetime.now()
    date_end: Optional[datetime] = datetime.now()
    duration: int
    program_type: str
    partners: str
    description: str

    class Config:
        from_attributes = True

class ProgramUpdate(BaseModel):
    name: Optional[str] = None
    date_begin: Optional[datetime] = datetime.now()
    date_end: Optional[datetime] = datetime.now()
    duration: Optional[int] = None
    program_type: Optional[str] = None
    partners: Optional[str] = None
    description: Optional[str] = None

    class Config:
        from_attributes = True
