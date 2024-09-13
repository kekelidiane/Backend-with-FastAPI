from fastapi import APIRouter, Depends, HTTPException, status

from . import schemas, models

router = APIRouter()

@router.post(
    '/',
    response_model=schemas.Entreprise,
    status_code=status.HTTP_200_OK,
    response_model_by_alias=True,
    response_description="Entreprise créée avec succès"
)
async def create_entreprise(entreprise: schemas.EntrepriseCreate):
    new_entreprise = await models.Entreprise.create(
        name=entreprise.name,
        domain=entreprise.domain,
        mail=entreprise.mail,
        address=entreprise.address,
        site=entreprise.site,
        description=entreprise.description or "Azerty uiop",
        partnership_type=entreprise.partnership_type,
        partnership_date=entreprise.partnership_date,
    )
    
    return new_entreprise

@router.get(
    '/',
    status_code=status.HTTP_200_OK,
    response_model_by_alias=True,
    response_description="Entreprises récupérées"
)
async def get_entreprises():
    entreprises = await models.Entreprise.query.gino.all()
    return entreprises

@router.put(
    "/{id}",
    response_model=schemas.Entreprise,
    status_code=status.HTTP_200_OK,
    response_model_by_alias=True,
    response_description="Entreprise mise à jour"
)
async def update_entreprise(id_entreprise: int, entreprise: schemas.EntrepriseUpdate):
    old_entreprise = await models.Entreprise.get(id_entreprise)

    if not old_entreprise:
        raise HTTPException(status_code=404, detail="Entreprise introuvable")
    
    # Mettre à jour les champs
    await old_entreprise.update(**entreprise.model_dump(exclude_unset=True)).apply()

    return old_entreprise


@router.delete(
    "/{id}",
    status_code=status.HTTP_200_OK,
    response_description="Entreprise supprimée"
)
async def delete_entreprise(id: int):
    old_entreprise = await models.Entreprise.get(id)

    if not old_entreprise:
        raise HTTPException(status_code=404, detail=f"Entreprise avec ID {id} introuvable")
    
    await old_entreprise.delete()
    return {"detail": "Entreprise supprimée avec succès"}
