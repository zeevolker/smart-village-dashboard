from __future__ import annotations

from backend.scripts.utils import csv_path
from sqlalchemy import select

from app.models.district import District
from app.models.province import Province
from app.models.regency import Regency
from app.models.village import Village
from app.seeders.base_seeder import BaseSeeder
from app.seeders.bulk_inserter import BulkInserter
from app.seeders.csv_reader import CsvReader
from app.seeders.csv_validator import CsvValidator


class TerritorySeeder(BaseSeeder):
    """
    Seeder master data wilayah Indonesia.
    """

    def __init__(self) -> None:
        super().__init__()

        self.inserter = BulkInserter(self.db)

    # =====================================================
    # Public
    # =====================================================

    def run(self) -> None:
        try:
            print("===================================")
            print(" Territory Seeder")
            print("===================================\n")

            self.seed_provinces()
            self.seed_regencies()
            self.seed_districts()
            self.seed_villages()

            self.db.commit()

            print("\n===================================")
            print("✓ Territory seeding completed.")
            print("===================================")

        except Exception:
            self.db.rollback()
            raise

        finally:
            self.close()

    # =====================================================
    # Private Helpers
    # =====================================================

    def _load_csv(
        self,
        filename: str,
        headers: list[str],
    ) -> list[dict[str, str]]:
        rows = CsvReader(
            csv_path(filename),
        ).read()

        CsvValidator.validate_headers(
            rows,
            headers,
        )

        return rows

    def _validate_parent(
        self,
        mapping: dict[str, str],
        code: str,
        entity: str,
    ) -> str:

        parent_id = mapping.get(code)

        if parent_id is None:
            raise ValueError(f"{entity} code '{code}' not found.")

        return parent_id

    def _province_map(self) -> dict[str, str]:
        return dict(
            self.db.execute(
                select(
                    Province.code,
                    Province.id,
                )
            )
        )

    def _regency_map(self) -> dict[str, str]:
        return dict(
            self.db.execute(
                select(
                    Regency.code,
                    Regency.id,
                )
            )
        )

    def _district_map(self) -> dict[str, str]:
        return dict(
            self.db.execute(
                select(
                    District.code,
                    District.id,
                )
            )
        )

    # =====================================================
    # Provinces
    # =====================================================

    def seed_provinces(self) -> None:

        print("Seeding provinces...")

        rows = self._load_csv(
            "provinces.csv",
            [
                "code",
                "bps_code",
                "name",
            ],
        )

        self.inserter.insert(
            Province,
            rows,
        )

        self.db.flush()

        print(f"✓ {len(rows):,} provinces inserted.")

    # =====================================================
    # Regencies
    # =====================================================

    def seed_regencies(self) -> None:

        print("Seeding regencies...")

        rows = self._load_csv(
            "regencies.csv",
            [
                "code",
                "bps_code",
                "name",
                "province_code",
            ],
        )

        province_map = self._province_map()

        data: list[dict[str, str]] = []

        for row in rows:
            data.append(
                {
                    "code": row["code"],
                    "bps_code": row["bps_code"],
                    "name": row["name"],
                    "province_id": self._validate_parent(
                        province_map,
                        row["province_code"],
                        "Province",
                    ),
                }
            )

        self.inserter.insert(
            Regency,
            data,
        )

        self.db.flush()

        print(f"✓ {len(data):,} regencies inserted.")

    # =====================================================
    # Districts
    # =====================================================

    def seed_districts(self) -> None:

        print("Seeding districts...")

        rows = self._load_csv(
            "districts.csv",
            [
                "code",
                "bps_code",
                "name",
                "regency_code",
            ],
        )

        regency_map = self._regency_map()

        data: list[dict[str, str]] = []

        for row in rows:
            data.append(
                {
                    "code": row["code"],
                    "bps_code": row["bps_code"],
                    "name": row["name"],
                    "regency_id": self._validate_parent(
                        regency_map,
                        row["regency_code"],
                        "Regency",
                    ),
                }
            )

        self.inserter.insert(
            District,
            data,
        )

        self.db.flush()

        print(f"✓ {len(data):,} districts inserted.")

    # =====================================================
    # Villages
    # =====================================================

    def seed_villages(self) -> None:

        print("Seeding villages...")

        rows = self._load_csv(
            "villages.csv",
            [
                "code",
                "bps_code",
                "name",
                "district_code",
            ],
        )

        district_map = self._district_map()

        data: list[dict[str, str]] = []

        for row in rows:
            data.append(
                {
                    "code": row["code"],
                    "bps_code": row["bps_code"],
                    "name": row["name"],
                    "district_id": self._validate_parent(
                        district_map,
                        row["district_code"],
                        "District",
                    ),
                }
            )

        self.inserter.insert(
            Village,
            data,
        )

        self.db.flush()

        print(f"✓ {len(data):,} villages inserted.")
