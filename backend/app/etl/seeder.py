from __future__ import annotations

import csv
from pathlib import Path
from typing import Any

from sqlalchemy.orm import Session

from app.models.district import District
from app.models.province import Province
from app.models.regency import Regency
from app.models.village import Village

PROCESSED_DIR = Path("data/processed")


class TerritorySeeder:
    """
    Seeder master wilayah Indonesia.
    """

    def __init__(
        self,
        db: Session,
    ):
        self.db = db

    # =====================================================
    # Helpers
    # =====================================================

    def _read_csv(
        self,
        filename: str,
    ) -> list[dict[str, Any]]:

        filepath = PROCESSED_DIR / filename

        with filepath.open(
            encoding="utf-8",
            newline="",
        ) as file:
            return list(csv.DictReader(file))

    # =====================================================
    # Province
    # =====================================================

    def seed_provinces(self):

        rows = self._read_csv("provinces.csv")

        for row in rows:
            province = Province(
                code=row["code"],
                bps_code=row["bps_code"],
                name=row["name"],
            )

            self.db.add(province)

        self.db.flush()

    # =====================================================
    # Lookup Cache
    # =====================================================

    def province_map(
        self,
    ) -> dict[str, str]:

        return {
            province.code: province.id for province in self.db.query(Province).all()
        }

    def regency_map(
        self,
    ) -> dict[str, str]:

        return {regency.code: regency.id for regency in self.db.query(Regency).all()}

    def district_map(
        self,
    ) -> dict[str, str]:

        return {
            district.code: district.id for district in self.db.query(District).all()
        }

    # =====================================================
    # Regency
    # =====================================================

    def seed_regencies(self):

        province_map = self.province_map()

        rows = self._read_csv("regencies.csv")

        for row in rows:
            regency = Regency(
                code=row["code"],
                bps_code=row["bps_code"],
                name=row["name"],
                province_id=province_map[row["province_code"]],
            )

            self.db.add(regency)

        self.db.flush()

    # =====================================================
    # District
    # =====================================================

    def seed_districts(self):

        regency_map = self.regency_map()

        rows = self._read_csv("districts.csv")

        for row in rows:
            district = District(
                code=row["code"],
                bps_code=row["bps_code"],
                name=row["name"],
                regency_id=regency_map[row["regency_code"]],
            )

            self.db.add(district)

        self.db.flush()

    # =====================================================
    # Village
    # =====================================================

    def seed_villages(self):

        district_map = self.district_map()

        rows = self._read_csv("villages.csv")

        for row in rows:
            village = Village(
                code=row["code"],
                bps_code=row["bps_code"],
                name=row["name"],
                district_id=district_map[row["district_code"]],
            )

            self.db.add(village)

        self.db.flush()

    # =====================================================
    # Run
    # =====================================================

    def run(self):

        print("Seeding provinces...")
        self.seed_provinces()

        print("Seeding regencies...")
        self.seed_regencies()

        print("Seeding districts...")
        self.seed_districts()

        print("Seeding villages...")
        self.seed_villages()
