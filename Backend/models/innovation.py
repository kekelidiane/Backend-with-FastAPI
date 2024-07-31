from fastapi import UploadFile, File
from pydantic import BaseModel, Field, EmailStr
from typing import Optional, List
from datetime import datetime

class Innovation(BaseModel):
    id_innov: Optional[str] = Field(default=None, description="L'identifiant unique de l'utilisateur, automatiquement généré")
    name: str = Field(..., description="Nom de l'innovation")
    type: str = Field(description="Type d'innovation")
    description: str 
    date: datetime = Field(..., default_factory=datetime.utcnow, description="Date de publication de l'innovation")
