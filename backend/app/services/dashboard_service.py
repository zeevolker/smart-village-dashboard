from app.repositories.analytics_repository import AnalyticsRepository
from app.schemas.dashboard import DashboardResponse


class DashboardService:
    """
    Service untuk menggabungkan seluruh data dashboard.
    """

    def __init__(
        self,
        repository: AnalyticsRepository,
    ) -> None:
        self.repository = repository

    def get_dashboard(self) -> DashboardResponse:
        """
        Mengambil seluruh data dashboard.
        """

        gender = self.repository.count_gender()

        return DashboardResponse(
            summary={
                "population": self.repository.count_population(),
                "households": self.repository.count_households(),
                "villages": self.repository.count_villages(),
                "male": gender["male"],
                "female": gender["female"],
            },
            demographics={
                "gender": gender,
                "religion": self.repository.religion_distribution(),
                "occupation": self.repository.occupation_distribution(),
                "marital_status": self.repository.marital_status_distribution(),
            },
            villages=self.repository.village_summary(),
        )