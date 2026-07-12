from app.repositories.citizen_repository import CitizenRepository
from app.enums.gender import Gender
from app.enums.marital_status import MaritalStatus
from app.enums.religion import Religion


def test_search_without_keyword(db):
    repo = CitizenRepository(db)

    items, total, pages = repo.search()

    assert total > 0
    assert pages > 0
    assert len(items) > 0


def test_search_with_keyword(db):
    repo = CitizenRepository(db)

    items, total, pages = repo.search("Hari")

    assert total == 1
    assert pages == 1
    assert len(items) == 1

    citizen = items[0]

    assert (
        "hari" in citizen.full_name.lower()
        or "hari" in citizen.nik.lower()
    )
    
def test_search_filter_gender(db):
    repo = CitizenRepository(db)

    items, total, pages = repo.search(
        gender=Gender.MALE,
    )

    assert total > 0
    assert pages > 0
    assert len(items) > 0

    assert all(
        citizen.gender == Gender.MALE
        for citizen in items
    )


def test_search_filter_religion(db):
    repo = CitizenRepository(db)

    items, total, pages = repo.search(
        religion=Religion.ISLAM,
    )

    assert total > 0
    assert pages > 0
    assert len(items) > 0

    assert all(
        citizen.religion == Religion.ISLAM
        for citizen in items
    )


def test_search_filter_marital_status(db):
    repo = CitizenRepository(db)

    items, total, pages = repo.search(
        marital_status=MaritalStatus.MARRIED,
    )

    assert total > 0
    assert pages > 0
    assert len(items) > 0

    assert all(
        citizen.marital_status == MaritalStatus.MARRIED
        for citizen in items
    )