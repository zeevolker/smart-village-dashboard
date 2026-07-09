from app.repositories.analytics_repository import AnalyticsRepository
from app.services.analytics_service import AnalyticsService


def test_get_demographics(db):
    # Arrange
    repo = AnalyticsRepository(db)
    service = AnalyticsService(repo)

    # Act
    result = service.get_demographics()

    # Assert
    assert "gender" in result
    assert "religion" in result
    assert "occupation" in result
    assert "marital_status" in result

    assert result["gender"]["male"] >= 0
    assert result["gender"]["female"] >= 0

    assert len(result["religion"]) > 0
    assert len(result["occupation"]) > 0
    assert len(result["marital_status"]) > 0