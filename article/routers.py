from datetime import datetime
from fastapi import APIRouter, Depends, File, HTTPException, UploadFile, status
from sqlalchemy import select

from core.database import get_db
from sqlalchemy.ext.asyncio import AsyncSession
from . import schemas, models

router = APIRouter()

MAX_FILE_SIZE_MB = 100  # Taille maximale du fichier en Mo

@router.post(
    '/',
    response_model=schemas.Article,
    status_code = status.HTTP_200_OK,
    response_model_by_alias = True,
    response_description = "Artcile créé avec succes"
)
async def create_article(article: schemas.ArticleCreate, db: AsyncSession = Depends(get_db)):
    new_article = models.Article(
        title=article.title,
        author=article.author,
        content=article.content,
        source=article.source or "Unknown",
        date=(article.date or datetime.now()).replace(tzinfo=None)  # Utiliser la date actuelle si None
    )
    
    db.add(new_article)
    await db.commit()
    await db.refresh(new_article)

    return new_article
    

@router.get(
    '/',
    status_code = status.HTTP_200_OK,
    response_model_by_alias = True,
    response_description = "Articles recupérés"
)
async def get_articles(db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(models.Article))
    articles = result.scalars().all()
    return articles

@router.put(
    "/{id}",
    response_model=schemas.Article,
    status_code = status.HTTP_200_OK,
    response_model_by_alias = True,
    response_description = "Artcile à jour"
)
async def update_article(id_article: int, article: schemas.ArticleUpdate, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(models.Article).where(models.Article.id == id_article))
    old_article = result.scalar_one_or_none()  # pour obtenir un seul article ou None

    if old_article is None:
        raise HTTPException(status_code=404, detail="Article introuvable")
    
    for key, value in article.model_dump(exclude_unset=True).items():      # Mettre à jour les champs de l'article
        setattr(old_article, key, value)

    # try:
    await db.commit()
    await db.refresh(old_article)

    # except Exception as e:
    #         await db.rollback()
    #         raise HTTPException(status_code=500, detail=str(e))
    
    return old_article

@router.delete(
    "/{id}",
    status_code = status.HTTP_200_OK,
    response_description = "Artcile supprimé !"
)
async def delete_article(id: int, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(models.Article).where(models.Article.id == id))
    old_article = result.scalar_one_or_none()  # pour obtenir un seul article ou None

    if not old_article:
        raise HTTPException(status_code=404, detail="Article avec ID {id} introuvable")
    
    await db.delete(old_article)
    await db.commit()
    

#Ancienne fonction potentiellement la cause d'erreurs donc à revoir
'''
async def create_article(
    article: schemas.ArticleCreate, 
    files: List[UploadFile] = File(...), 
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