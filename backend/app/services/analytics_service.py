from app.repositories.analytics_repository import AnalyticsRepository
from uuid import UUID


class AnalyticsService:

    def __init__(self, repository: AnalyticsRepository):
        self.repository = repository

    def get_summary(self) -> dict:

        gender = self.repository.count_gender()

        return {
            "population": self.repository.count_population(),
            "households": self.repository.count_households(),
            "villages": self.repository.count_villages(),
            "male": gender["male"],
            "female": gender["female"],
        }
        
    def get_demographics(self) -> dict:

        return {
            "gender": self.repository.count_gender(),
            "religion": self.repository.religion_distribution(),
            "occupation": self.repository.occupation_distribution(),
            "marital_status": self.repository.marital_status_distribution(),
        }
            
    def get_village_summary(
        self,
        *,
        page: int = 1,
        page_size: int = 20,
        search: str | None = None,
        district_id: UUID | None = None,
        sort: str = "village",
        order: str = "asc",
    ) -> list[dict]:

        return self.repository.village_summary(
            page=page,
            page_size=page_size,
            search=search,
            district_id=district_id,
            sort=sort,
            order=order,
        )