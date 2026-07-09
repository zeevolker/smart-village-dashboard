from app.repositories.citizen_repository import CitizenRepository


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