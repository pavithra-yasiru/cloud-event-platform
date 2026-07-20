from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import get_db
from app.models import Program
from app import crud

router = APIRouter()


@router.get("/")
def root():
    return {"message": "Program Service is running"}


@router.get("/programs")
def get_programs(db: Session = Depends(get_db)):
    return crud.get_programs(db)


@router.get("/programs/{program_id}")
def get_program(program_id: int, db: Session = Depends(get_db)):

    program = crud.get_program(db, program_id)

    if program is None:
        raise HTTPException(status_code=404, detail="Program not found")

    return program


@router.post("/programs")
def create_program(program: Program, db: Session = Depends(get_db)):
    return crud.create_program(db, program)


@router.put("/programs/{program_id}")
def update_program(
    program_id: int,
    updated_program: Program,
    db: Session = Depends(get_db)
):

    program = crud.update_program(db, program_id, updated_program)

    if program is None:
        raise HTTPException(status_code=404, detail="Program not found")

    return program


@router.delete("/programs/{program_id}")
def delete_program(
    program_id: int,
    db: Session = Depends(get_db)
):

    program = crud.delete_program(db, program_id)

    if program is None:
        raise HTTPException(status_code=404, detail="Program not found")

    return {
        "message": "Program deleted successfully"
    }
