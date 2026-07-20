from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import get_db
from app.models import Registration
from app import crud

router = APIRouter()


@router.get("/")
def root():
    return {"message": "Registration Service is running"}


@router.get("/registrations")
def get_registrations(db: Session = Depends(get_db)):
    return crud.get_registrations(db)


@router.get("/registrations/{registration_id}")
def get_registration(registration_id: int, db: Session = Depends(get_db)):

    registration = crud.get_registration(db, registration_id)

    if registration is None:
        raise HTTPException(status_code=404, detail="Registration not found")

    return registration


@router.post("/registrations")
def create_registration(registration: Registration, db: Session = Depends(get_db)):
    return crud.create_registration(db, registration)


@router.put("/registrations/{registration_id}")
def update_registration(
    registration_id: int,
    updated_registration: Registration,
    db: Session = Depends(get_db)
):

    registration = crud.update_registration(db, registration_id, updated_registration)

    if registration is None:
        raise HTTPException(status_code=404, detail="Registration not found")

    return registration


@router.delete("/registrations/{registration_id}")
def delete_registration(
    registration_id: int,
    db: Session = Depends(get_db)
):

    registration = crud.delete_registration(db, registration_id)

    if registration is None:
        raise HTTPException(status_code=404, detail="Registration not found")

    return {
        "message": "Registration deleted successfully"
    }
