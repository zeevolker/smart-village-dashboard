from app.repositories.analytics_repository import AnalyticsRepository


def test_count_population(db):
    # Arrange
    repo = AnalyticsRepository(db)

    # Act
    total = repo.count_population()

    # Assert
    assert total > 0


def test_count_households(db):
    # Arrange
    repo = AnalyticsRepository(db)

    # Act
    total = repo.count_households()

    # Assert
    assert total > 0


def test_count_villages(db):
    # Arrange
    repo = AnalyticsRepository(db)

    # Act
    total = repo.count_villages()

    # Assert
    assert total > 0


def test_count_gender(db):
    # Arrange
    repo = AnalyticsRepository(db)

    # Act
    result = repo.count_gender()

    # Assert
    assert "male" in result
    assert "female" in result

    assert result["male"] >= 0
    assert result["female"] >= 0

    population = repo.count_population()

    assert result["male"] + result["female"] == population