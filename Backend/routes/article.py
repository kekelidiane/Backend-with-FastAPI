from datetime import datetime
import os
from fastapi import APIRouter, Depends, File, Form, HTTPException, UploadFile, HTTPException
from typing import List, Any
from core.db_models import Table_Article
from models.article import Article
from core.database import get_db
from schemas.article import list_serial, individual_serial
from sqlalchemy.orm import Session

router = APIRouter()

MAX_FILE_SIZE_MB = 100  # Taille maximale du fichier en Mo

#POST request method
@router.post("/")
async def create_article(
    id_article: str = Form(...),
    title: str = Form(...),
    author: str = Form(...),
    content: str = Form(...),
    source: str = Form(...),
    date: datetime = Form(...),
    files: List[UploadFile] = File(...),
    db: Session = Depends(get_db), 
):
    file_urls = []

#---- Methode pour verifier le format des visuels ------
    def validate_file(files: List[UploadFile] = File(...)):
        file_size_mb = len(file.file.read()) / (1024 * 1024)
        if file_size_mb > MAX_FILE_SIZE_MB:
            raise HTTPException(status_code=400, detail="Fichier trop volumineux.")
        
        # Vérifier le type MIME du fichier
        if not file.content_type.startswith(('image/', 'video/')):
            raise HTTPException(status_code=400, detail="Le fichier doit être une image ou une vidéo.")
        
        file.file.seek(0) # Revenir au début du fichier (parameter) files: Any
#------

    for file in files:
        validate_file(files)
    
    # Enregistrez le fichier
    file_location = f"files/{file.filename}"
    os.makedirs(os.path.dirname(file_location), exist_ok=True) # Créez le dossier si nécessaire

    with open(file_location, "wb") as f:
        f.write(file.file.read())
    file_urls.append(file_location)
    # print("info" "file '{file.filename}' saved at '{file_location}'")


    article = Table_Article(
        id_article = id_article,
        title = title,
        author = author,
        content = content,
        source = source,
        date = date,
        visuals = ",".join(file_urls)
    )

    db.add(article)
    await db.commit()
    await db.refresh(article)
    
    return individual_serial(article)


#GET request method
@router.get('/')
async def get_article(db: Session = Depends(get_db)):
    articles = db.query(Table_Article).all()
    return list_serial(articles)

#PUT request method
@router.put("/{id_article}")
async def update_article(id_article: str, article: Article, db: Session = Depends(get_db)):
    db_article = db.query(Table_Article).filter(Table_Article.id_article == id_article).first()
    if not db_article:
        raise HTTPException(status_code=404, detail="Article not found")
    
    update_data = article.model_dump(exclude_unset=True)
    for key, value in update_data.items():
        setattr(db_article, key, value)
    
    db.commit()
    db.refresh(db_article)
    
    return individual_serial(db_article)

#DELETE request method
@router.delete("/{id_article}")
async def delete_article(id_article: str, db: Session = Depends(get_db)):
    db_article = db.query(Table_Article).filter(Table_Article.id_article == id_article).first()
    if not db_article:
        raise HTTPException(status_code=404, detail="Article not found")
    
    db.delete(db_article)
    db.commit()
    
    return {"message": "Article deleted successfully"}
