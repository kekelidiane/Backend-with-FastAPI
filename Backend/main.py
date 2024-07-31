from fastapi import FastAPI
from core.database import init_db
from routes import article, auth, club

app = FastAPI()

app.include_router(article.router, prefix="/article")
# app.include_router(auth.router, prefix="/auth")
@app.on_event("startup")
async def startup():
    await init_db()
