from pydantic import BaseModel


class Event(BaseModel):
    id: int
    title: str
    venue: str
    date: str
    ticket_price: float
    capacity: int
    available_seats: int
