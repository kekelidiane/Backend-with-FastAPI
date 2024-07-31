from pydantic import BaseModel, Field, ValidationError
from fastapi import UploadFile, File
from typing import Optional
from datetime import datetime

class Article(BaseModel):
    id_artcicle: str = Field(..., description="L'identifiant unique de l'utilisateur")
    title: str = Field(..., description="Titre de l'article")
    author: str = Field(..., description="Auteur de l'article")
    content: str = Field(..., description="Contenu de l'article")
    source: Optional[str] = Field(default=None, description="La source de l'article")
    date: datetime = Field(..., default_factory=datetime.now, description="Date et heure de publication de l'article")
    # visuals: List[UploadFile] = File(...)

try:
    Article()
except ValidationError as exc:
    print(repr(exc.errors()[0]['type']))
    #> 'missing'