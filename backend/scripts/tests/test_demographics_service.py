from app.database.database import SessionLocal

from app.repositories.analytics_repository import AnalyticsRepository
from app.services.analytics_service import AnalyticsService

db = SessionLocal()

repo = AnalyticsRepository(db)
service = AnalyticsService(repo)

print(service.get_demographics())

db.close()