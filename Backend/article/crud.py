from sqlalchemy.orm import Session
from typing import List
from fastapi import HTTPException
from models import Article
from schemas import ArticleCreate, ArticleUpdate

def create_article(db: Session, article: ArticleCreate, file_urls: List[str]):
    new_article = Article(
        id_article=article.id_article,
        title=article.title,
        author=article.author,
        content=article.content,
        source=article.source,
        date=article.date,
        visuals=",".join(file_urls)
    )

    db.add(new_article)
    db.commit()
    db.refresh(new_article)
    
    return new_article

def get_articles(db: Session):
    return db.query(Article).all()

def update_article(db: Session, id_article: str, article: ArticleUpdate):
    db_article = db.query(Article).filter(Article.id_article == id_article).first()
    if not db_article:
        raise HTTPException(status_code=404, detail="Article not found")
    
    for key, value in article.dict(exclude_unset=True).items():
        setattr(db_article, key, value)
    db.commit()
    db.refresh(db_article)

    return db_article

def delete_article(db: Session, id_article: str):
    db_article = db.query(Article).filter(Article.id_article == id_article).first()
    if not db_article:
        raise HTTPException(status_code=404, detail="Article not found")
    
    db.delete(db_article)
    db.commit()
    
    return {"message": "Article deleted successfully"}
