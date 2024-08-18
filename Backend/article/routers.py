from datetime import datetime
import os
from fastapi import APIRouter, Depends, File, HTTPException, UploadFile
from typing import List

from sqlalchemy import select
from core.database import get_db
from sqlalchemy.orm import Session
from . import crud, schemas, models

router = APIRouter()

MAX_FILE_SIZE_MB = 100  # Taille maximale du fichier en Mo

@router.post("/")
async def create_article(article: schemas.ArticleCreate, db: Session = Depends(get_db)):
    # Vérifiez si l'article existe déjà (si nécessaire)
    
    query = select(models.Article).filter(models.Article.id_article == article.id_article)
    result = await db.execute(query)
    existing_article = result.scalars().first()
    existing_article = existing_article.scalar()
    
    if existing_article:
        raise HTTPException(status_code=400, detail="Un article avec cet ID existe deja.")
    
    # Créez l'objet Article à partir du modèle SQLAlchemy
    db_article = models.Article(
        id_article=article.id_article,
        title=article.title,
        author=article.author,
        content=article.content,
        source=article.source or "Unknown",  # Utiliser "Unknown" si source est None
        date=article.date or datetime.now()  # Utiliser la date actuelle si None
    )
    
    db.add(db_article)
    await db.commit()
    await db.refresh(db_article)
    
    return {"message": "Article créé avec succes", "article": db_article}

@router.get('/')
async def get_articles(db: Session = Depends(get_db)):
    return crud.get_articles(db)

@router.put("/{id_article}")
async def update_article(id_article: str, article: schemas.ArticleUpdate, db: Session = Depends(get_db)):
    return crud.update_article(db, id_article, article)

@router.delete("/{id_article}")
async def delete_article(id_article: str, db: Session = Depends(get_db)):
    return crud.delete_article(db, id_article)


'''
async def create_article(
    article: schemas.ArticleCreate, 
    #files: List[UploadFile] = File(...), 
    db: Session = Depends(get_db)
):
    file_urls = []

    def validate_file(file: UploadFile):
        file.file.seek(0, os.SEEK_END)
        file_size_mb = file.file.tell() / (1024 * 1024)
        if file_size_mb > MAX_FILE_SIZE_MB:
            raise HTTPException(status_code=400, detail="Fichier trop volumineux.")
        
        if not file.content_type.startswith(('image/', 'video/')):
            raise HTTPException(status_code=400, detail="Le fichier doit être une image ou une vidéo.")
        
        file.file.seek(0)

    for file in files:
        validate_file(file)
    
        file_location = f"files/{file.filename}"
        os.makedirs(os.path.dirname(file_location), exist_ok=True)

        with open(file_location, "wb") as f:
            f.write(file.file.read())
        file_urls.append(file_location)
        file.file.seek(0)

    new_article = crud.create_article(db, article, file_urls)
    
    return new_article

'''