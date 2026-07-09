from app.services.citizen_service import CitizenService


def test_search_without_keyword(db):
    # Arrange
    service = CitizenService(db)

    # Act
    result = service.search()

    # Assert
    assert result.total > 0
    assert result.pages > 0
    assert len(result.items) > 0


def test_search_with_keyword(db):
    # Arrange
    service = CitizenService(db)

    # Act
    result = service.search("Hari")

    # Assert
    assert result.total == 1
    assert result.pages == 1
    assert len(result.items) == 1

    citizen = result.items[0]

    assert (
        "hari" in citizen.full_name.lower()
        or "hari" in citizen.nik.lower()
    )