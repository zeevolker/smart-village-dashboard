from app.database.database import SessionLocal
from app.repositories.citizen_repository import CitizenRepository


def main():
    db = SessionLocal()

    repo = CitizenRepository(db)

    items, total, pages = repo.search("Hari")

    print(f"Total Citizens : {total}")
    print(f"Total Pages    : {pages}")
    print()

    for citizen in items[:5]:
        print(
            citizen.nik,
            citizen.full_name,
        )

    db.close()


if __name__ == "__main__":
    main()