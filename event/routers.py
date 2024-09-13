from fastapi import APIRouter, HTTPException, status

from . import schemas, models

router = APIRouter()

# Route POST: Créer un événement
@router.post(
    '/',
    response_model=schemas.Event,
    status_code=status.HTTP_200_OK,
    response_model_by_alias=True,
    response_description="Event créé avec succès"
)
async def create_event(event: schemas.EventCreate):
    new_event = await models.Event.create(
        title=event.title,
        date_begin=event.date_begin,
        date_end=event.date_end,
        duration=event.duration,
        location=event.location,
        partners=event.partners,
        description=event.description,
        participants=event.participants,
    )
    return new_event

# Route GET: Récupérer tous les événements
@router.get(
    '/',
    status_code=status.HTTP_200_OK,
    response_model_by_alias=True,
    response_description="Événements récupérés"
)
async def get_events():
    events = await models.Event.query.gino.all()
    return events

# Route PUT: Mettre à jour un événement par ID
@router.put(
    "/{id}",
    response_model=schemas.Event,
    status_code=status.HTTP_200_OK,
    response_model_by_alias=True,
    response_description="Événement mis à jour"
)
async def update_event(id_event: int, event: schemas.EventUpdate):
    old_event = await models.Event.get(id_event)

    if not old_event:
        raise HTTPException(status_code=404, detail="Événement introuvable")
    
    # Mise à jour des champs de l'événement
    await old_event.update(**event.dict(exclude_unset=True)).apply()
    
    return old_event

# Route DELETE: Supprimer un événement par ID
@router.delete(
    "/{id}",
    status_code=status.HTTP_200_OK,
    response_description="Événement supprimé"
)
async def delete_event(id: int):
    old_event = await models.Event.get(id)

    if not old_event:
        raise HTTPException(status_code=404, detail=f"Événement avec ID {id} introuvable")
    
    await old_event.delete()
    return {"detail": "Événement supprimé avec succès"}
