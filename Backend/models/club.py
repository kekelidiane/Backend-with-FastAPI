from fastapi import UploadFile, File
from pydantic import BaseModel, Field
from typing import Optional, List

class Club(BaseModel):
    id_club: Optional[str] = Field(default=None, description="L'identifiant unique du club")
    name: str = Field(..., description="Nom du club")
    domain: str = Field(..., description="Domaine d'activité du club")
    description: str = Field(...)
    responsable: str = Field(..., description="Identité du responsable du club")
