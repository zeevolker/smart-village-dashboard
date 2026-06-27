from fastapi import APIRouter
from sqlalchemy import text

from app.database.database import SessionLocal

router = APIRouter()


@router.get("/db-test")
def db_test():
    db = SessionLocal()

    try:
        db.execute(text("SELECT 1"))

        return {
            "status": "success",
            "message": "Database connected!"
        }

    finally:
        db.close()