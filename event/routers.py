from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy import select

from core.database import get_db
from sqlalchemy.ext.asyncio import AsyncSession
from . import schemas, models

router = APIRouter()

@router.post(
    '/',
    response_model=schemas.Event,
    status_code = status.HTTP_200_OK,
    response_model_by_alias = True,
    response_description = "Event créé avec succes"
)
async def create_event(event: schemas.EventCreate, db: AsyncSession = Depends(get_db)):
    new_event = models.Event(
        title=event.title,
        date_begin=event.date_begin,
        date_end=event.date_end,
        duration=event.duration,
        location=event.location,
        partners=event.partners,
        description=event.description,
        participants=event.participants,
    )
    
    db.add(new_event)
    await db.commit()
    await db.refresh(new_event)

    return new_event
    

@router.get(
    '/',
    status_code = status.HTTP_200_OK,
    response_model_by_alias = True,
    response_description = "Evenements recupérés"
)
async def get_events(db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(models.Event))
    events = result.scalars().all()
    return events

@router.put(
    "/{id}",
    response_model=schemas.Event,
    status_code = status.HTTP_200_OK,
    response_model_by_alias = True,
    response_description = "Evenement à jour"
)
async def update_event(id_event: int, event: schemas.EventUpdate, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(models.Event).where(models.Event.id == id_event))
    old_event = result.scalar_one_or_none()  # pour obtenir un seul ou None

    if old_event is None:
        raise HTTPException(status_code=404, detail="Evenement introuvable")
    
    for key, value in event.model_dump(exclude_unset=True).items():      # Mettre à jour les champs
        setattr(old_event, key, value)

    await db.commit()
    await db.refresh(old_event)
    
    return old_event

@router.delete(
    "/{id}",
    status_code = status.HTTP_200_OK,
    response_description = "Evenement supprimé !"
)
async def delete_event(id: int, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(models.Event).where(models.Event.id == id))
    old_event = result.scalar_one_or_none()  # pour obtenir un seul ou None

    if not old_event:
        raise HTTPException(status_code=404, detail="Evenement avec ID {id} introuvable")
    
    await db.delete(old_event)
    await db.commit()
    