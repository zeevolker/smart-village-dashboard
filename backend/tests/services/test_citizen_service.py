from app.services.citizen_service import CitizenService
from app.enums.gender import Gender
from app.enums.marital_status import MaritalStatus
from app.enums.religion import Religion


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
    
def test_search_filter_gender(db):
    service = CitizenService(db)

    result = service.search(
        gender=Gender.MALE,
    )

    assert result.total > 0
    assert result.pages > 0
    assert len(result.items) > 0

    assert all(
        citizen.gender == Gender.MALE
        for citizen in result.items
    )


def test_search_filter_religion(db):
    service = CitizenService(db)

    result = service.search(
        religion=Religion.ISLAM,
    )

    assert result.total > 0
    assert result.pages > 0
    assert len(result.items) > 0

    assert all(
        citizen.religion == Religion.ISLAM
        for citizen in result.items
    )


def test_search_filter_marital_status(db):
    service = CitizenService(db)

    result = service.search(
        marital_status=MaritalStatus.MARRIED,
    )

    assert result.total > 0
    assert result.pages > 0
    assert len(result.items) > 0

    assert all(
        citizen.marital_status == MaritalStatus.MARRIED
        for citizen in result.items
    )