from app.database.database import SessionLocal

from app.repositories.analytics_repository import AnalyticsRepository
from app.services.analytics_service import AnalyticsService

db = SessionLocal()

repo = AnalyticsRepository(db)
service = AnalyticsService(repo)

data = service.get_village_summary(
    sort="village",
    order="desc",
)

print(len(data))
print()

for row in data:
    print(row)

db.close()