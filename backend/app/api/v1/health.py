from fastapi import APIRouter
from sqlalchemy import text

from app.database.database import SessionLocal

router = APIRouter(
    prefix="/health",
    tags=["Health"],
)


@router.get("")
def health():
    db = SessionLocal()

    try:
        db.execute(text("SELECT 1"))

        return {
            "status": "healthy",
            "database": "connected",
            "version": "1.0.0",
        }

    finally:
        db.close()