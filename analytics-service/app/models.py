from pydantic import BaseModel


class Analytics(BaseModel):
    event_type: str
    page: str
    event_time: str
