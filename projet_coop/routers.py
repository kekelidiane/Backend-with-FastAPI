from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy import select

from core.database import get_db
from sqlalchemy.ext.asyncio import AsyncSession
from . import schemas, models

router = APIRouter()

@router.post(
    '/',
    response_model=schemas.Project,
    status_code = status.HTTP_200_OK,
    response_model_by_alias = True,
    response_description = "Projet créé avec succes"
)
async def create_project(project: schemas.ProjectCreate, db: AsyncSession = Depends(get_db)):
    new_project = models.Project(
        name=project.name,
        date_begin=project.date_begin,
        date_end=project.date_end,
        duration=project.duration,
        project_type=project.project_type,
        partners=project.partners,
        description=project.description,
    )
    
    db.add(new_project)
    await db.commit()
    await db.refresh(new_project)

    return new_project
    

@router.get(
    '/',
    status_code = status.HTTP_200_OK,
    response_model_by_alias = True,
    response_description = "Projets recupérés"
)
async def get_projects(db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(models.Project))
    projects = result.scalars().all()
    return projects

@router.put(
    "/{id}",
    response_model=schemas.Project,
    status_code = status.HTTP_200_OK,
    response_model_by_alias = True,
    response_description = "Projet à jour"
)
async def update_project(id_project: int, project: schemas.ProjectUpdate, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(models.Project).where(models.Project.id == id_project))
    old_project = result.scalar_one_or_none()  # pour obtenir un seul ou None

    if old_project is None:
        raise HTTPException(status_code=404, detail="Project introuvable")
    
    for key, value in project.model_dump(exclude_unset=True).items():      # Mettre à jour les champs
        setattr(old_project, key, value)

    await db.commit()
    await db.refresh(old_project)
    
    return old_project

@router.delete(
    "/{id}",
    status_code = status.HTTP_200_OK,
    response_description = "Project supprimé !"
)
async def delete_project(id: int, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(models.Project).where(models.Project.id == id))
    old_project = result.scalar_one_or_none()  # pour obtenir un seul ou None

    if not old_project:
        raise HTTPException(status_code=404, detail="Project avec ID {id} introuvable")
    
    await db.delete(old_project)
    await db.commit()
    