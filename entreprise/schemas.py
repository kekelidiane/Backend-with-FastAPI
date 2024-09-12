from datetime import datetime
from pydantic import BaseModel, EmailStr
from typing import Optional


class Entreprise(BaseModel):
    name: str
    domain: str
    mail: EmailStr
    address:str
    site: str
    description: str
    partnership_type: str
    partnership_date: Optional[datetime] = datetime.now()

    class Config:
        from_attributes = True

class EntrepriseCreate(BaseModel):
    name: str
    domain: str
    mail: EmailStr
    address: str
    site: str
    description: str
    partnership_type: Optional[str] = "Azerty uiop"
    partnership_date: Optional[datetime] = datetime.now()

    class Config:
        from_attributes = True

class EntrepriseUpdate(BaseModel):
    name: Optional[str] = None
    domain: Optional[str] = None
    mail: Optional[EmailStr] = None
    address: Optional[str] = None
    site: Optional[str] = None
    description: Optional[str] = None
    partnership_type: Optional[str] = None
    partnership_date: Optional[datetime] = datetime.now()


    class Config:
        from_attributes = True
