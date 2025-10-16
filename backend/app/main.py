from fastapi import FastAPI
from app.routers import parking

app = FastAPI(title="Smart Parking API")

app.include_router(parking.router)

@app.get("/")
def root():
    return {"message": "🚗 Smart Parking Backend is running!"}
