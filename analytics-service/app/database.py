from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker
import clickhouse_connect

DATABASE_URL = "postgresql://postgres:postgres@postgres-service:5432/eventdb"

engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

Base = declarative_base()

clickhouse_client = clickhouse_connect.get_client(
    host="clickhouse",
    port=8123,
    username="admin",
    password="admin123"
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
