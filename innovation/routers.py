from fastapi import APIRouter, HTTPException, status

from . import schemas, models

router = APIRouter()

# Route POST: Créer une innovation
@router.post(
    '/',
    response_model=schemas.Innovation,
    status_code=status.HTTP_200_OK,
    response_model_by_alias=True,
    response_description="Innovation créée avec succès"
)
async def create_innovation(innovation: schemas.InnovationCreate):
    new_innovation = await models.Innovation.create(
        name=innovation.name,
        innovation_type=innovation.innovation_type,
        date=innovation.date,
        description=innovation.description,
    )
    return new_innovation

# Route GET: Récupérer toutes les innovations
@router.get(
    '/',
    status_code=status.HTTP_200_OK,
    response_model_by_alias=True,
    response_description="Innovations récupérées"
)
async def get_innovations():
    innovations = await models.Innovation.query.gino.all()
    return innovations

# Route PUT: Mettre à jour une innovation par ID
@router.put(
    "/{id}",
    response_model=schemas.Innovation,
    status_code=status.HTTP_200_OK,
    response_model_by_alias=True,
    response_description="Innovation mise à jour"
)
async def update_innovation(id_innovation: int, innovation: schemas.InnovationUpdate):
    old_innovation = await models.Innovation.get(id_innovation)

    if not old_innovation:
        raise HTTPException(status_code=404, detail="Innovation introuvable")
    
    # Mettre à jour les champs de l'innovation
    await old_innovation.update(**innovation.dict(exclude_unset=True)).apply()
    
    return old_innovation

# Route DELETE: Supprimer une innovation par ID
@router.delete(
    "/{id}",
    status_code=status.HTTP_200_OK,
    response_description="Innovation supprimée"
)
async def delete_innovation(id: int):
    old_innovation = await models.Innovation.get(id)

    if not old_innovation:
        raise HTTPException(status_code=404, detail=f"Innovation avec ID {id} introuvable")
    
    await old_innovation.delete()
    return {"detail": "Innovation supprimée avec succès"}
