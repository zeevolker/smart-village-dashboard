from app.database.database import SessionLocal
from app.repositories.analytics_repository import AnalyticsRepository

db = SessionLocal()

repo = AnalyticsRepository(db)

print(repo.religion_distribution())
print()
print(repo.occupation_distribution())
print()
print(repo.marital_status_distribution())

db.close()