from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy import select

from core.database import get_db
from sqlalchemy.ext.asyncio import AsyncSession
from . import schemas, models

router = APIRouter()

@router.post(
    '/',
    response_model=schemas.Stage,
    status_code = status.HTTP_200_OK,
    response_model_by_alias = True,
    response_description = "Stage créé avec succes"
)
async def create_offer(offer: schemas.StageCreate, db: AsyncSession = Depends(get_db)):
    new_offer = models.Stage(
        post=offer.post,
        date_begin=offer.date_begin,
        date_end=offer.date_end,
        duration=offer.duration,
        domain=offer.domain,
        entreprise=offer.entreprise,
        remuneration_salary=offer.remuneration_salary,
        stage_type=offer.stage_type
    )
    
    db.add(new_offer)
    await db.commit()
    await db.refresh(new_offer)

    return new_offer
    

@router.get(
    '/',
    status_code = status.HTTP_200_OK,
    response_model_by_alias = True,
    response_description = "Offres de stage recupérés"
)
async def get_offers(db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(models.Stage))
    offers = result.scalars().all()
    return offers

@router.put(
    "/{id}",
    response_model=schemas.Stage,
    status_code = status.HTTP_200_OK,
    response_model_by_alias = True,
    response_description = "Offre de stage à jour"
)
async def update_offer(id_offer: int, offer: schemas.StageUpdate, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(models.Stage).where(models.Stage.id == id_offer))
    old_offer = result.scalar_one_or_none()  # pour obtenir un seul ou None

    if old_offer is None:
        raise HTTPException(status_code=404, detail="Offre de stage introuvable")
    
    for key, value in offer.model_dump(exclude_unset=True).items():      # Mettre à jour les champs
        setattr(old_offer, key, value)

    await db.commit()
    await db.refresh(old_offer)
    
    return old_offer

@router.delete(
    "/{id}",
    status_code = status.HTTP_200_OK,
    response_description = "Offre supprimé !"
)
async def delete_offer(id: int, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(models.Stage).where(models.Stage.id == id))
    old_offer = result.scalar_one_or_none()  # pour obtenir un seul ou None

    if not old_offer:
        raise HTTPException(status_code=404, detail="Stage avec ID {id} introuvable")
    
    await db.delete(old_offer)
    await db.commit()
    