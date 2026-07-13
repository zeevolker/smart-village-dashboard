from fastapi import FastAPI

from app.api.router import api_router
from app.core.handlers import (
    register_exception_handlers,
)
from app.schemas.response import success_response

from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title="Smart Village Dashboard API",
    description="Backend API for Smart Village Dashboard.",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:3000",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

register_exception_handlers(app)

app.include_router(api_router)


@app.get("/")
def root():
    return success_response(
        {
            "name": "Smart Village Dashboard API",
            "version": "1.0.0",
            "status": "running",
        },
        message="Welcome",
    )
