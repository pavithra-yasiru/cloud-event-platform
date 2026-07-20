from sqlalchemy import Column, Integer, String

from app.database import Base


class ProgramTable(Base):
    __tablename__ = "programs"

    id = Column(Integer, primary_key=True, index=True)
    event_id = Column(Integer, nullable=False)
    title = Column(String, nullable=False)
    speaker = Column(String, nullable=False)
    start_time = Column(String, nullable=False)
    end_time = Column(String, nullable=False)
