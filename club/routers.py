from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy import select

from core.database import get_db
from sqlalchemy.ext.asyncio import AsyncSession
from . import schemas, models

router = APIRouter()

@router.post(
    '/',
    response_model=schemas.Club,
    status_code = status.HTTP_200_OK,
    response_model_by_alias = True,
    response_description = "Club créé avec succes"
)
async def create_club(club: schemas.ClubCreate, db: AsyncSession = Depends(get_db)):
    new_club = models.Club(
        name=club.name,
        domain=club.domain,
        responsible=club.responsible,
        description=club.description or "Azerty uiop",
    )
    
    db.add(new_club)
    await db.commit()
    await db.refresh(new_club)

    return new_club
    

@router.get(
    '/',
    status_code = status.HTTP_200_OK,
    response_model_by_alias = True,
    response_description = "Clubs recupérés"
)
async def get_clubs(db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(models.Club))
    clubs = result.scalars().all()
    return clubs

@router.put(
    "/{id}",
    response_model=schemas.Club,
    status_code = status.HTTP_200_OK,
    response_model_by_alias = True,
    response_description = "Club à jour"
)
async def update_club(id_club: int, club: schemas.ClubUpdate, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(models.Club).where(models.Club.id == id_club))
    old_club = result.scalar_one_or_none()  # pour obtenir un seul article ou None

    if old_club is None:
        raise HTTPException(status_code=404, detail="Club introuvable")
    
    for key, value in club.model_dump(exclude_unset=True).items():      # Mettre à jour les champs
        setattr(old_club, key, value)

    await db.commit()
    await db.refresh(old_club)
    
    return old_club

@router.delete(
    "/{id}",
    status_code = status.HTTP_200_OK,
    response_description = "Club supprimé !"
)
async def delete_club(id: int, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(models.Club).where(models.Club.id == id))
    old_club = result.scalar_one_or_none()  # pour obtenir un seul article ou None

    if not old_club:
        raise HTTPException(status_code=404, detail="Club avec ID {id} introuvable")
    
    await db.delete(old_club)
    await db.commit()
    