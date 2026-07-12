from app.database.database import SessionLocal
from app.models.district import District
from sqlalchemy import func, select

db = SessionLocal()

count = db.scalar(
    select(func.count(District.id))
)

print(count)

db.close()