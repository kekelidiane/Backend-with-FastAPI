from fastapi import APIRouter, Depends, HTTPException, status

from . import schemas, models

router = APIRouter()

@router.post(
    '/',
    response_model=schemas.Stage,
    status_code=status.HTTP_200_OK,
    response_model_by_alias=True,
    response_description="Stage créé avec succès"
)
async def create_stage(stage: schemas.StageCreate):
    new_stage = await models.Stage.create(
        post=stage.post,
        date_begin=stage.date_begin,
        date_end=stage.date_end,
        duration=stage.duration,
        domain=stage.domain,
        entreprise=stage.entreprise,
        remuneration_salary=stage.remuneration_salary,
        stage_type=stage.stage_type
    )
    return new_stage

@router.get(
    '/',
    status_code=status.HTTP_200_OK,
    response_model_by_alias=True,
    response_description="Stages récupérés"
)
async def get_stages():
    stages = await models.Stage.query.gino.all()
    return stages

@router.put(
    "/{id}",
    response_model=schemas.Stage,
    status_code=status.HTTP_200_OK,
    response_model_by_alias=True,
    response_description="Stage mis à jour"
)
async def update_stage(id: int, stage: schemas.StageUpdate):
    old_stage = await models.Stage.get(id)

    if not old_stage:
        raise HTTPException(status_code=404, detail="Stage introuvable")

    await old_stage.update(
        **stage.dict(exclude_unset=True)
    ).apply()

    return old_stage

@router.delete(
    "/{id}",
    status_code=status.HTTP_200_OK,
    response_description="Stage supprimé !"
)
async def delete_stage(id: int):
    old_stage = await models.Stage.get(id)

    if not old_stage:
        raise HTTPException(status_code=404, detail=f"Stage avec ID {id} introuvable")

    await old_stage.delete()
    return {"detail": "Stage supprimé avec succès"}
