from pydantic import BaseModel


class Program(BaseModel):
    id: int
    event_id: int
    title: str
    speaker: str
    start_time: str
    end_time: str
