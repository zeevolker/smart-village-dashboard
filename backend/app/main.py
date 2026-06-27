from fastapi import FastAPI
from app.api.test import router as test_router

app = FastAPI(
    title="Smart Village Dashboard API",
    version="1.0.0",
)

app.include_router(test_router)


@app.get("/")
def root():
    return {
        "message": "Welcome to Smart Village Dashboard API"
    }