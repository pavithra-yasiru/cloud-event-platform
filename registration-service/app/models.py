from pydantic import BaseModel


class Registration(BaseModel):
    id: int
    event_id: int
    attendee_name: str
    email: str
    phone: str
    tickets: int
