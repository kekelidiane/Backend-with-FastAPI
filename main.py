from fastapi import FastAPI
import article.routers, club.routers, entreprise.routers, event.routers, innovation.routers, programs.routers, projet_coop.routers, stage.routers

app = FastAPI(
    title="API du site de l'EPL",
    summary="------------ Backend du portail web de l'EPL ------------.",
)

app.include_router(article.routers.router, prefix="/article")
# app.include_router(auth.router, prefix="/auth")
