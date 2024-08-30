from datetime import datetime
from pydantic import BaseModel
from typing import Optional


class Innovation(BaseModel):
    name: str
    innovation_type: str
    date: Optional[datetime] = datetime.now()
    description: str

    class Config:
        from_attributes = True

class InnovationCreate(BaseModel):
    name: str
    innovation_type: str
    date: Optional[datetime] = datetime.now()
    description: str

    class Config:
        from_attributes = True

class InnovationUpdate(BaseModel):
    name: Optional[str] = None
    innovation_type: Optional[str] = None
    date: Optional[datetime] = datetime.now()
    description: Optional[str] = None

    class Config:
        from_attributes = True
