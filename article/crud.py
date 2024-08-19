from datetime import datetime
from sqlalchemy.orm import Session
from fastapi import Depends, File, HTTPException, UploadFile

from core.database import get_db
from . import schemas, models

async def create_article(article: schemas.ArticleCreate, db: Session = Depends(get_db)):
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
    

# async def get_articles(db: Session):
#     return db.query(models.Article).all()


# async def delete_article(db: Session, id: str):
#     db_article = db.query(models.Article).filter(models.Article.title == id).first()
#     if not db_article:
#         raise HTTPException(status_code=404, detail="Article introuvable")
    
#     db.delete(db_article)
#     db.commit()
    
#     return {"message": "Article deleted successfully"}

# async def update_article(id_article: int, article: schemas.ArticleUpdate, db: Session = Depends(get_db)):
 
    # if old_article is None:
    #     raise HTTPException(status_code=404, detail="Article introuvable")
    
    # # Mettre à jour les champs de l'article
    # for key, value in article.model_dump(exclude_unset=True).items():
    #     setattr(old_article, key, value)
    
    # db.add(old_article)
    # await db.commit()
    # await db.refresh(old_article)
    
    # return old_article