from sqlalchemy import Column, Integer, String, Float

from app.database import Base


class EventTable(Base):
    __tablename__ = "events"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    venue = Column(String, nullable=False)
    date = Column(String, nullable=False)
    ticket_price = Column(Float, nullable=False)
    capacity = Column(Integer, nullable=False)
    available_seats = Column(Integer, nullable=False)
