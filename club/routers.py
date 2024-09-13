from fastapi import APIRouter, HTTPException, status

from . import schemas, models

router = APIRouter()

@router.post(
    '/',
    response_model=schemas.Club,
    status_code=status.HTTP_200_OK,
    response_model_by_alias=True,
    response_description="Club créé avec succès"
)
async def create_club(club: schemas.ClubCreate):
    new_club = await models.Club.create(
        name=club.name,
        domain=club.domain,
        responsible=club.responsible,
        description=club.description or "Azerty uiop"
    )
    return new_club

@router.get(
    '/',
    status_code=status.HTTP_200_OK,
    response_model_by_alias=True,
    response_description="Clubs récupérés"
)
async def get_clubs():
    clubs = await models.Club.query.gino.all()
    return clubs

@router.put(
    "/{id}",
    response_model=schemas.Club,
    status_code=status.HTTP_200_OK,
    response_model_by_alias=True,
    response_description="Club mis à jour"
)
async def update_club(id_club: int, club: schemas.ClubUpdate):
    old_club = await models.Club.get(id_club)
    if old_club is None:
        raise HTTPException(status_code=404, detail="Club introuvable")
    
    await old_club.update(**club.model_dump(exclude_unset=True)).apply()
    return old_club

@router.delete(
    "/{id}",
    status_code=status.HTTP_200_OK,
    response_description="Club supprimé"
)
async def delete_club(id: int):
    old_club = await models.Club.get(id)
    if not old_club:
        raise HTTPException(status_code=404, detail=f"Club avec ID {id} introuvable")
    
    await old_club.delete()
    return {"detail": "Club supprimé avec succès"}
