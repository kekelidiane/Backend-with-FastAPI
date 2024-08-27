from pydantic import BaseModel
from typing import Optional


class Club(BaseModel):
    name: str
    domain: str
    responsible: str
    description: str

    class Config:
        from_attributes = True

class ClubCreate(BaseModel):
    name: str
    domain: str
    responsible: str
    description: Optional[str] = "Azerty uiop"

    class Config:
        from_attributes = True

class ClubUpdate(BaseModel):
    name: Optional[str] = None
    domain: Optional[str] = None
    responsible: Optional[str] = None
    description: Optional[str] = None

    class Config:
        from_attributes = True
