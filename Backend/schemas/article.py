from datetime import datetime
from typing import List
from core.db_models import Table_Article

def individual_serial(article: Table_Article) -> dict:
    return {
        "id": str(article.id),
        "id_article": str(article.id_article),
        "author": str(article.author),
        "content": str(article.content),
        "source": str(article.source),
        "title": str(article.title),
        "date": article.date.isoformat() if article.date else None,
    }

def list_serial(articles: List[Table_Article]) -> list:
    return [individual_serial(article) for article in articles]

 