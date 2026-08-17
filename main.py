from fastapi import FastAPI

from app.database import engine, Base
from app.Router.auth import router as auth_router
from app.Models import models

app = FastAPI(title="TrustBank Digital", description="API for TrustBank Digital", version="1.0.0")

Base.metadata.create_all(bind=engine)

app.include_router(auth_router)

@app.get("/")
def read_root():
    return {"message": "Welcome to TrustBank Digital API!"}



