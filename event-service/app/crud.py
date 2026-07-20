from sqlalchemy.orm import Session
from fastapi import HTTPException
from app.db_models import EventTable
from app.models import Event

import boto3
import json

THRESHOLD = 10

lambda_client = boto3.client(
    "lambda",
    region_name="ap-south-1"
)


def invoke_lambda(event_id, remaining_seats):

    payload = {
        "event_id": event_id,
        "remaining_seats": remaining_seats
    }

    try:
        response = lambda_client.invoke(
            FunctionName="event-seat-notification",
            InvocationType="Event",
            Payload=json.dumps(payload)
        )

        print(f"Lambda invoked successfully: {response}")

    except Exception as e:
        print(f"Lambda invocation failed: {e}")

def get_events(db: Session):
    return db.query(EventTable).all()


def get_event(db: Session, event_id: int):
    return db.query(EventTable).filter(
        EventTable.id == event_id
    ).first()


def create_event(db: Session, event: Event):

    db_event = EventTable(**event.model_dump())

    db.add(db_event)
    db.commit()
    db.refresh(db_event)

    return db_event


def update_event(db: Session, event_id: int, updated_event: Event):

    db_event = get_event(db, event_id)

    if db_event is None:
        return None

    for key, value in updated_event.model_dump().items():
        setattr(db_event, key, value)

    db.commit()
    db.refresh(db_event)

    return db_event


def delete_event(db: Session, event_id: int):

    db_event = get_event(db, event_id)

    if db_event is None:
        return None

    db.delete(db_event)
    db.commit()

    return db_event


def register_event(db: Session, event_id: int, tickets: int):

    event = get_event(db, event_id)

    if event is None:
        return None

    if event.available_seats < tickets:
        raise HTTPException(
             status_code=409,
             detail="Not enough seats available."
        )

    event.available_seats -= tickets

    db.commit()
    db.refresh(event)

    if event.available_seats < THRESHOLD:
        invoke_lambda(
            event.id,
            event.available_seats
        )

    return event
