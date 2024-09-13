from fastapi import APIRouter, Depends, HTTPException, status
from . import schemas, models

router = APIRouter()

@router.post(
    '/',
    response_model=schemas.Project,
    status_code=status.HTTP_200_OK,
    response_model_by_alias=True,
    response_description="Projet créé avec succès"
)
async def create_project(project: schemas.ProjectCreate):
    new_project = await models.Project.create(
        name=project.name,
        date_begin=project.date_begin,
        date_end=project.date_end,
        duration=project.duration,
        project_type=project.project_type,
        partners=project.partners,
        description=project.description,
    )
    return new_project

@router.get(
    '/',
    status_code=status.HTTP_200_OK,
    response_model_by_alias=True,
    response_description="Projets récupérés"
)
async def get_projects():
    projects = await models.Project.query.gino.all()
    return projects

@router.put(
    "/{id}",
    response_model=schemas.Project,
    status_code=status.HTTP_200_OK,
    response_model_by_alias=True,
    response_description="Projet mis à jour"
)
async def update_project(id: int, project: schemas.ProjectUpdate):
    old_project = await models.Project.get(id)

    if not old_project:
        raise HTTPException(status_code=404, detail="Projet introuvable")

    # Mettre à jour les champs de l'objet
    await old_project.update(
        **project.dict(exclude_unset=True)
    ).apply()

    return old_project

@router.delete(
    "/{id}",
    status_code=status.HTTP_200_OK,
    response_description="Projet supprimé !"
)
async def delete_project(id: int):
    old_project = await models.Project.get(id)

    if not old_project:
        raise HTTPException(status_code=404, detail=f"Projet avec ID {id} introuvable")

    await old_project.delete()
    return {"detail": "Projet supprimé avec succès"}
