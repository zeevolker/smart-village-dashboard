from app.database.database import SessionLocal
from app.repositories.analytics_repository import AnalyticsRepository

db = SessionLocal()

repo = AnalyticsRepository(db)

data = repo.district_summary()

print(f"Total districts: {len(data)}")
print()

for row in data:
    if row["population"] > 0:
        print(row)

db.close()