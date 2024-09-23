from fastapi import FastAPI

import auth.routers, article.routers, club.routers, entreprise.routers, event.routers, innovation.routers, programs.routers, projet_coop.routers, stage.routers
from core.database import init_db, close_db

app = FastAPI(
    title="API du site",
    summary="------------ Backend du portail web de l'EPL ------------.",
)


@app.on_event("startup")        #appel de l'initialisation de la base de données
async def startup(): 
    await init_db(app)

app.include_router(auth.routers.router)
app.include_router(article.routers.router, prefix="/article")
app.include_router(club.routers.router, prefix="/club")
app.include_router(entreprise.routers.router, prefix="/entreprise")
app.include_router(event.routers.router, prefix="/event")
app.include_router(innovation.routers.router, prefix="/innovation")
app.include_router(programs.routers.router, prefix="/programs")
app.include_router(projet_coop.routers.router, prefix="/project")
app.include_router(stage.routers.router, prefix="/offre_stage")


@app.on_event("shutdown")       #appel de la fermerture de la connexion
async def shutdown():
    await close_db(app)