from fastapi import FastAPI
import article.routers, club.routers, entreprise.routers, event.routers, innovation.routers, programs.routers, projet_coop.routers, stage.routers
# import auth.routers

app = FastAPI(
    title="API du site de l'EPL",
    summary="------------ Backend du portail web de l'EPL ------------.",
)

# app.include_router(auth.router, prefix="/auth")
app.include_router(article.routers.router, prefix="/article")
app.include_router(club.routers.router, prefix="/club")
app.include_router(entreprise.routers.router, prefix="/entreprise")
app.include_router(event.routers.router, prefix="/event")
app.include_router(innovation.routers.router, prefix="/innovation")
app.include_router(programs.routers.router, prefix="/programs")
app.include_router(projet_coop.routers.router, prefix="/project")
app.include_router(stage.routers.router, prefix="/offre_stage")
