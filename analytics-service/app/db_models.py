from sqlalchemy import Column, Integer, String

from app.database import Base


class AnalyticsTable(Base):
    __tablename__ = "analytics"

    id = Column(Integer, primary_key=True, index=True)
    event_type = Column(String, nullable=False)
    page = Column(String, nullable=False)
    event_time = Column(String, nullable=False)

import clickhouse_connect

clickhouse_client = clickhouse_connect.get_client(
    host="clickhouse",
    port=8123,
    username="admin",
    password="admin123"
)
