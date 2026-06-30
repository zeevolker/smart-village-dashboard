from __future__ import annotations

import argparse

from app.database.database import SessionLocal

from scripts.seeders.population_seeder import PopulationSeeder


def parse_args():

    parser = argparse.ArgumentParser(
        description="Synthetic Population Seeder"
    )

    parser.add_argument(
        "--households",
        type=int,
        default=10,
        help="Number of households to generate.",
    )

    return parser.parse_args()


def main():

    args = parse_args()

    db = SessionLocal()

    try:

        seeder = PopulationSeeder(db)

        seeder.seed(
            households=args.households,
        )

    finally:

        db.close()


if __name__ == "__main__":
    main()