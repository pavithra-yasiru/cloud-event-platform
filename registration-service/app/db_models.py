from sqlalchemy import Column, Integer, String

from app.database import Base


class RegistrationTable(Base):
    __tablename__ = "registrations"

    id = Column(Integer, primary_key=True, index=True)
    event_id = Column(Integer, nullable=False)
    attendee_name = Column(String, nullable=False)
    email = Column(String, nullable=False)
    phone = Column(String, nullable=False)
    tickets = Column(Integer, nullable=False)
