from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy import select

from core.database import get_db
from sqlalchemy.ext.asyncio import AsyncSession
from . import schemas, models

router = APIRouter()

@router.post(
    '/',
    response_model=schemas.Innovation,
    status_code = status.HTTP_200_OK,
    response_model_by_alias = True,
    response_description = "Innovation créé avec succes"
)
async def create_innovation(innovation: schemas.InnovationCreate, db: AsyncSession = Depends(get_db)):
    new_innovation = models.Innovation(
        name=innovation.name,
        innovation_type=innovation.innovation_type,
        date=innovation.date,
        description=innovation.description,
    )
    
    db.add(new_innovation)
    await db.commit()
    await db.refresh(new_innovation)

    return new_innovation
    

@router.get(
    '/',
    status_code = status.HTTP_200_OK,
    response_model_by_alias = True,
    response_description = "innovations recupérés"
)
async def get_innovations(db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(models.Innovation))
    innovations = result.scalars().all()
    return innovations

@router.put(
    "/{id}",
    response_model=schemas.Innovation,
    status_code = status.HTTP_200_OK,
    response_model_by_alias = True,
    response_description = "Innovation à jour"
)
async def update_innovation(id_innovation: int, innovation: schemas.InnovationUpdate, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(models.Innovation).where(models.Innovation.id == id_innovation))
    old_innovation = result.scalar_one_or_none()  # pour obtenir un seul ou None

    if old_innovation is None:
        raise HTTPException(status_code=404, detail="innovation introuvable")
    
    for key, value in innovation.model_dump(exclude_unset=True).items():      # Mettre à jour les champs
        setattr(old_innovation, key, value)

    await db.commit()
    await db.refresh(old_innovation)
    
    return old_innovation

@router.delete(
    "/{id}",
    status_code = status.HTTP_200_OK,
    response_description = "Innovation supprimé !"
)
async def delete_innovation(id: int, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(models.Innovation).where(models.Innovation.id == id))
    old_innovation = result.scalar_one_or_none()  # pour obtenir un seul ou None

    if not old_innovation:
        raise HTTPException(status_code=404, detail="Innovation avec ID {id} introuvable")
    
    await db.delete(old_innovation)
    await db.commit()
    