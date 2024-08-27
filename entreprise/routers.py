from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy import select

from core.database import get_db
from sqlalchemy.ext.asyncio import AsyncSession
from . import schemas, models

router = APIRouter()

@router.post(
    '/',
    response_model=schemas.Entreprise,
    status_code = status.HTTP_200_OK,
    response_model_by_alias = True,
    response_description = "Entreprise créé avec succes"
)
async def create_entreprise(entreprise: schemas.EntrepriseCreate, db: AsyncSession = Depends(get_db)):
    new_club = models.Entreprise(
        name=entreprise.name,
        domain=entreprise.domain,
        mail=entreprise.mail,
        address=entreprise.address,
        site=entreprise.site,
        description=entreprise.description or "Azerty uiop",
        partnership_type=entreprise.partnership_type,
        partnership_date=entreprise.partnership_date,
    )
    
    db.add(new_club)
    await db.commit()
    await db.refresh(new_club)

    return new_club
    

@router.get(
    '/',
    status_code = status.HTTP_200_OK,
    response_model_by_alias = True,
    response_description = "Entreprises recupérés"
)
async def get_entreprises(db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(models.Entreprise))
    entreprises = result.scalars().all()
    return entreprises

@router.put(
    "/{id}",
    response_model=schemas.Entreprise,
    status_code = status.HTTP_200_OK,
    response_model_by_alias = True,
    response_description = "Entreprise à jour"
)
async def update_entreprise(id_entreprise: int, club: schemas.EntrepriseUpdate, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(models.Entreprise).where(models.Entreprise.id == id_entreprise))
    old_entreprise = result.scalar_one_or_none()  # pour obtenir un seul ou None

    if old_entreprise is None:
        raise HTTPException(status_code=404, detail="Entreprise introuvable")
    
    for key, value in club.model_dump(exclude_unset=True).items():      # Mettre à jour les champs
        setattr(old_entreprise, key, value)

    await db.commit()
    await db.refresh(old_entreprise)
    
    return old_entreprise

@router.delete(
    "/{id}",
    status_code = status.HTTP_200_OK,
    response_description = "Entreprise supprimé !"
)
async def delete_entreprise(id: int, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(models.Entreprise).where(models.Entreprise.id == id))
    old_entreprise = result.scalar_one_or_none()  # pour obtenir un seul ou None

    if not old_entreprise:
        raise HTTPException(status_code=404, detail="Entreprise avec ID {id} introuvable")
    
    await db.delete(old_entreprise)
    await db.commit()
    