from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy import select

from core.database import get_db
from sqlalchemy.ext.asyncio import AsyncSession
from . import schemas, models

router = APIRouter()

@router.post(
    '/',
    response_model=schemas.Program,
    status_code = status.HTTP_200_OK,
    response_model_by_alias = True,
    response_description = "Program créé avec succes"
)
async def create_program(program: schemas.ProgramCreate, db: AsyncSession = Depends(get_db)):
    new_program = models.Program(
        name=program.name,
        date_begin=program.date_begin,
        date_end=program.date_end,
        duration=program.duration,
        program_type=program.program_type,
        partners=program.partners,
        description=program.description,
    )
    
    db.add(new_program)
    await db.commit()
    await db.refresh(new_program)

    return new_program
    

@router.get(
    '/',
    status_code = status.HTTP_200_OK,
    response_model_by_alias = True,
    response_description = "Programs recupérés"
)
async def get_programs(db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(models.Program))
    programs = result.scalars().all()
    return programs

@router.put(
    "/{id}",
    response_model=schemas.Program,
    status_code = status.HTTP_200_OK,
    response_model_by_alias = True,
    response_description = "Program à jour"
)
async def update_program(id_program: int, program: schemas.ProgramUpdate, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(models.Program).where(models.Program.id == id_program))
    old_program = result.scalar_one_or_none()  # pour obtenir un seul ou None

    if old_program is None:
        raise HTTPException(status_code=404, detail="Program introuvable")
    
    for key, value in program.model_dump(exclude_unset=True).items():      # Mettre à jour les champs
        setattr(old_program, key, value)

    await db.commit()
    await db.refresh(old_program)
    
    return old_program

@router.delete(
    "/{id}",
    status_code = status.HTTP_200_OK,
    response_description = "Program supprimé !"
)
async def delete_program(id: int, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(models.Program).where(models.Program.id == id))
    old_program = result.scalar_one_or_none()  # pour obtenir un seul ou None

    if not old_program:
        raise HTTPException(status_code=404, detail="Program avec ID {id} introuvable")
    
    await db.delete(old_program)
    await db.commit()
    