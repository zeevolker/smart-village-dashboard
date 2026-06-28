from __future__ import annotations

import json
from pathlib import Path
from typing import Any

from app.etl.cleaner import TerritoryCleaner

RAW_DIR = Path("data/raw")
PROCESSED_DIR = Path("data/processed")


class TerritoryNormalizer:
    """
    Normalisasi dataset wilayah hasil download BPS.
    """

    def __init__(self):

        PROCESSED_DIR.mkdir(
            parents=True,
            exist_ok=True,
        )

        self.cleaner = TerritoryCleaner()

    # ======================================================
    # JSON Helpers
    # ======================================================

    def _load_json(
        self,
        filepath: Path,
    ) -> list[dict[str, Any]]:
        """
        Membaca satu file JSON.
        """

        with filepath.open(
            encoding="utf-8",
        ) as file:
            return json.load(file)

    def _load_directory(
        self,
        directory: Path,
    ) -> list[dict[str, Any]]:
        """
        Membaca seluruh file JSON dalam sebuah folder.
        """

        rows: list[dict[str, Any]] = []

        for filepath in sorted(directory.glob("*.json")):
            rows.extend(self._load_json(filepath))

        return rows

    # ======================================================
    # Loaders
    # ======================================================

    def load_provinces(
        self,
    ) -> list[dict[str, Any]]:
        return self._load_json(RAW_DIR / "provinces.json")

    def load_regencies(
        self,
    ) -> list[dict[str, Any]]:
        return self._load_directory(RAW_DIR / "regencies")

    def load_districts(
        self,
    ) -> list[dict[str, Any]]:
        return self._load_directory(RAW_DIR / "districts")

    def load_villages(
        self,
    ) -> list[dict[str, Any]]:
        return self._load_directory(RAW_DIR / "villages")

    # ======================================================
    # Helpers
    # ======================================================

    def _get_parent_code(
        self,
        code: str,
    ) -> str:
        """
        Mengambil kode parent berdasarkan struktur
        kode wilayah Kemendagri.

        Contoh:

        32 -> ""

        32.01 -> 32

        32.01.21 -> 32.01

        32.01.21.2001 -> 32.01.21
        """

        parts = code.split(".")

        if len(parts) == 1:
            return ""

        return ".".join(parts[:-1])

    def _normalize(
        self,
        rows: list[dict[str, Any]],
        parent_key: str | None = None,
    ) -> list[dict[str, str]]:

        rows = self.cleaner.clean(rows)

        normalized: list[dict[str, str]] = []

        for row in rows:
            item = {
                "code": row["kode_dagri"],
                "bps_code": row["kode_bps"],
                "name": row["nama_dagri"],
            }

            if parent_key:
                item[parent_key] = self._get_parent_code(row["kode_dagri"])

            normalized.append(item)

        return normalized

    # ======================================================
    # Public API
    # ======================================================

    def normalize_provinces(
        self,
    ) -> list[dict[str, str]]:
        """
        Normalisasi data provinsi.
        """

        return self._normalize(
            self.load_provinces(),
        )

    def normalize_regencies(
        self,
    ) -> list[dict[str, str]]:
        """
        Normalisasi data kabupaten/kota.
        """

        return self._normalize(
            self.load_regencies(),
            parent_key="province_code",
        )

    def normalize_districts(
        self,
    ) -> list[dict[str, str]]:
        """
        Normalisasi data kecamatan.
        """

        return self._normalize(
            self.load_districts(),
            parent_key="regency_code",
        )

    def normalize_villages(
        self,
    ) -> list[dict[str, str]]:
        """
        Normalisasi data desa/kelurahan.
        """

        return self._normalize(
            self.load_villages(),
            parent_key="district_code",
        )
