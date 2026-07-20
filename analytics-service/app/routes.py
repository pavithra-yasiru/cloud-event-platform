from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import get_db
from app.models import Analytics
from app import crud

router = APIRouter()


@router.get("/")
def root():
    return {
        "message": "Analytics Service is running"
    }


@router.get("/analytics")
def get_analytics(db: Session = Depends(get_db)):
    return crud.get_analytics(db)


@router.post("/analytics")
def create_analytics(
    analytics: Analytics,
    db: Session = Depends(get_db)
):
    return crud.create_analytics(db, analytics)
