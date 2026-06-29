from app.database.database import SessionLocal
from app.seeders.user_seeder import UserSeeder


def main() -> None:
    db = SessionLocal()

    try:
        UserSeeder(
            db,
        ).run()

    finally:
        db.close()


if __name__ == "__main__":
    main()