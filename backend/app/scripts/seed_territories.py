from app.database.database import SessionLocal
from app.etl.seeder import TerritorySeeder


def main():

    db = SessionLocal()

    try:
        seeder = TerritorySeeder(db)

        seeder.run()

        db.commit()

        print()
        print("✓ Territory seeding completed.")

    except Exception:
        db.rollback()

        raise

    finally:
        db.close()


if __name__ == "__main__":
    main()
