from app.database.database import SessionLocal
from app.repositories.analytics_repository import AnalyticsRepository


db = SessionLocal()

repo = AnalyticsRepository(db)

print("Population :", repo.count_population())
print("Households :", repo.count_households())
print("Villages   :", repo.count_villages())
print("Gender     :", repo.count_gender())

db.close()