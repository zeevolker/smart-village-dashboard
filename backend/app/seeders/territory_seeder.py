from app.seeders.base_seeder import BaseSeeder
from app.seeders.csv_reader import CsvReader
from app.scripts.utils import csv_path

from app.seeders.csv_validator import CsvValidator

from app.seeders.bulk_inserter import BulkInserter

class TerritorySeeder(BaseSeeder):
    """
    Seeder untuk master data wilayah Indonesia.
    """

    def run(self) -> None:
        try:
            print("Starting territory seeder...")

            reader = CsvReader(
                csv_path("provinces.csv")
            )

            rows = reader.read()

            CsvValidator.validate_headers(
                rows,
                ["code", "name"],
            )

            print(f"Loaded {len(rows)} provinces.")

            print("Done.")

        except Exception as exc:
            print(f"Seeder failed: {exc}")

        finally:
            self.close()
    
        inserter = BulkInserter(self.db)