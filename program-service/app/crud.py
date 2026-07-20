from sqlalchemy.orm import Session

from app.db_models import ProgramTable
from app.models import Program


def get_programs(db: Session):
    return db.query(ProgramTable).all()


def get_program(db: Session, program_id: int):
    return db.query(ProgramTable).filter(
        ProgramTable.id == program_id
    ).first()


def create_program(db: Session, program: Program):
    db_program = ProgramTable(**program.model_dump())

    db.add(db_program)
    db.commit()
    db.refresh(db_program)

    return db_program


def update_program(db: Session, program_id: int, updated_program: Program):

    db_program = get_program(db, program_id)

    if db_program is None:
        return None

    for key, value in updated_program.model_dump().items():
        setattr(db_program, key, value)

    db.commit()
    db.refresh(db_program)

    return db_program


def delete_program(db: Session, program_id: int):

    db_program = get_program(db, program_id)

    if db_program is None:
        return None

    db.delete(db_program)
    db.commit()

    return db_program
