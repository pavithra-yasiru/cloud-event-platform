from fastapi import APIRouter, Depends, HTTPException, Body
from sqlalchemy.orm import Session

from app.database import get_db
from app.models import Event
from app import crud

router = APIRouter()


@router.get("/")
def root():
    return {
        "message": "Event Service is running"
    }


@router.get("/events")
def get_events(db: Session = Depends(get_db)):
    return crud.get_events(db)


@router.get("/events/{event_id}")
def get_event(event_id: int, db: Session = Depends(get_db)):

    event = crud.get_event(db, event_id)

    if event is None:
        raise HTTPException(status_code=404, detail="Event not found")

    return event


@router.post("/events")
def create_event(event: Event, db: Session = Depends(get_db)):
    return crud.create_event(db, event)


@router.put("/events/{event_id}")
def update_event(
    event_id: int,
    updated_event: Event,
    db: Session = Depends(get_db)
):

    event = crud.update_event(db, event_id, updated_event)

    if event is None:
        raise HTTPException(status_code=404, detail="Event not found")

    return event

@router.post("/events/{event_id}/register")
def register_event(
    event_id: int,
    payload: dict = Body(...),
    db: Session = Depends(get_db)
):

    tickets = payload.get("tickets", 1)

    event = crud.register_event(
        db,
        event_id,
        tickets
    )

    if event is None:
        raise HTTPException(
            status_code=404,
            detail="Event not found"
        )

    return event

@router.delete("/events/{event_id}")
def delete_event(
    event_id: int,
    db: Session = Depends(get_db)
):

    event = crud.delete_event(db, event_id)

    if event is None:
        raise HTTPException(status_code=404, detail="Event not found")

    return {
        "message": "Event deleted successfully"
    }
