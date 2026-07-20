from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.routes import router

from app.database import Base
from app.database import engine

import app.db_models

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Analytics Service",
    description="Microservice for collecting website analytics",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://13.233.81.248:30083",  # Frontend
        "http://13.233.81.248:30086"   # Dashboard
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router)
