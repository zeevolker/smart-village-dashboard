from app.database.database import SessionLocal
from app.seeders.citizen_seeder import CitizenSeeder


def main() -> None:

    db = SessionLocal()

    try:

        print(
            "Starting Citizen Seeder..."
        )

        CitizenSeeder(
            db,
        ).run(
            total=500,
        )

        print(
            "Citizen Seeder completed."
        )

    finally:

        db.close()


if __name__ == "__main__":
    main()