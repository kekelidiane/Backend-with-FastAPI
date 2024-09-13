from fastapi import APIRouter, Depends, HTTPException, status

from . import schemas, models

router = APIRouter()

@router.post(
    '/',
    response_model=schemas.Program,
    status_code=status.HTTP_200_OK,
    response_model_by_alias=True,
    response_description="Program créé avec succès"
)
async def create_program(program: schemas.ProgramCreate):
    new_program = await models.Program.create(
        name=program.name,
        date_begin=program.date_begin,
        date_end=program.date_end,
        duration=program.duration,
        program_type=program.program_type,
        partners=program.partners,
        description=program.description,
    )
    return new_program

@router.get(
    '/',
    status_code=status.HTTP_200_OK,
    response_model_by_alias=True,
    response_description="Programs récupérés"
)
async def get_programs():
    programs = await models.Program.query.gino.all()
    return programs

@router.put(
    "/{id}",
    response_model=schemas.Program,
    status_code=status.HTTP_200_OK,
    response_model_by_alias=True,
    response_description="Program mis à jour"
)
async def update_program(id: int, program: schemas.ProgramUpdate):
    old_program = await models.Program.get(id)

    if not old_program:
        raise HTTPException(status_code=404, detail="Program introuvable")

    # Mettre à jour les champs de l'objet
    await old_program.update(
        **program.dict(exclude_unset=True)
    ).apply()

    return old_program

@router.delete(
    "/{id}",
    status_code=status.HTTP_200_OK,
    response_description="Program supprimé !"
)
async def delete_program(id: int):
    old_program = await models.Program.get(id)

    if not old_program:
        raise HTTPException(status_code=404, detail=f"Program avec ID {id} introuvable")

    await old_program.delete()
    return {"detail": "Program supprimé avec succès"}
