from fastapi import FastAPI
from routes import article, auth, club

app = FastAPI()

app.include_router(article.router, prefix="/article")
# app.include_router(auth.router, prefix="/auth")
