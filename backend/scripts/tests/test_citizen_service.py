from app.database.database import SessionLocal
from app.services.citizen_service import CitizenService


def main():
    db = SessionLocal()

    service = CitizenService(db)

    result = service.search("Hari")

    print(f"Total : {result.total}")
    print(f"Pages : {result.pages}")
    print()

    for citizen in result.items[:5]:
        print(
            citizen.nik,
            citizen.full_name,
        )

    db.close()


if __name__ == "__main__":
    main()