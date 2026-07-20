from sqlalchemy.orm import Session

from app.db_models import RegistrationTable
from app.models import Registration

import requests

EVENT_SERVICE = "http://event-service:8000"

def get_registrations(db: Session):
    return db.query(RegistrationTable).all()


def get_registration(db: Session, registration_id: int):
    return db.query(RegistrationTable).filter(
        RegistrationTable.id == registration_id
    ).first()


def create_registration(db: Session, registration: Registration):

    response = requests.post(

        f"{EVENT_SERVICE}/events/{registration.event_id}/register",

        json={
            "tickets": registration.tickets
        }

    )

    if response.status_code != 200:
        raise Exception("Unable to reserve seats")

    db_registration = RegistrationTable(
        **registration.model_dump()
    )

    db.add(db_registration)

    db.commit()

    db.refresh(db_registration)

    return db_registration

def update_registration(db: Session, registration_id: int, updated_registration: Registration):

    db_registration = get_registration(db, registration_id)

    if db_registration is None:
        return None

    for key, value in updated_registration.model_dump().items():
        setattr(db_registration, key, value)

    db.commit()
    db.refresh(db_registration)

    return db_registration


def delete_registration(db: Session, registration_id: int):

    db_registration = get_registration(db, registration_id)

    if db_registration is None:
        return None

    db.delete(db_registration)
    db.commit()

    return db_registration
