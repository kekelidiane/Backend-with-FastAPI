from fastapi import FastAPI
from article import routers
# import article.routes

app = FastAPI()

app.include_router(routers.router, prefix="/article")
# app.include_router(auth.router, prefix="/auth")
