import json
from pathlib import Path
from typing import Any

from tqdm import tqdm

from app.etl.client import BPSClient

RAW_DIR = Path("data/raw")


class TerritoryDownloader:
    """
    Downloader data wilayah Indonesia
    dari Bridging API BPS.
    """

    def __init__(self):
        RAW_DIR.mkdir(parents=True, exist_ok=True)

        self.client = BPSClient()

    # ==========================
    # API
    # ==========================

    def get_provinces(self) -> list[dict[str, Any]]:
        return self.client.get_wilayah(
            level="provinsi",
            parent=0,
        )

    def get_regencies(
        self,
        province_code: str,
    ) -> list[dict[str, Any]]:
        return self.client.get_wilayah(
            level="kabupaten",
            parent=province_code,
        )

    def get_districts(
        self,
        regency_code: str,
    ) -> list[dict[str, Any]]:
        return self.client.get_wilayah(
            level="kecamatan",
            parent=regency_code,
        )

    def get_villages(
        self,
        district_code: str,
    ) -> list[dict[str, Any]]:
        return self.client.get_wilayah(
            level="desa",
            parent=district_code,
        )

    # ==========================
    # File
    # ==========================

    def _save_json(
        self,
        data: list[dict[str, Any]],
        filepath: Path,
    ) -> None:
        """
        Simpan JSON ke file.
        """

        filepath.parent.mkdir(
            parents=True,
            exist_ok=True,
        )

        with filepath.open(
            "w",
            encoding="utf-8",
        ) as file:
            json.dump(
                data,
                file,
                ensure_ascii=False,
                indent=4,
            )

    # ==========================
    # Download
    # ==========================

    def download_provinces(
        self,
    ) -> list[dict[str, Any]]:
        provinces = self.get_provinces()

        self._save_json(
            provinces,
            RAW_DIR / "provinces.json",
        )

        return provinces

    def download_regencies(self) -> None:
        """
        Download seluruh kabupaten/kota.
        """

        provinces = self.get_provinces()

        regency_dir = RAW_DIR / "regencies"
        regency_dir.mkdir(
            parents=True,
            exist_ok=True,
        )

        for province in tqdm(
            provinces,
            desc="Downloading Regencies",
            unit="province",
        ):
            province_code = province["kode_bps"]

            regencies = self.get_regencies(
                province_code,
            )

            self._save_json(
                regencies,
                regency_dir / f"{province_code}.json",
            )

        print("\n✓ All regencies downloaded.")

    def download_districts(self) -> None:
        """
        Download seluruh kecamatan.
        """

        provinces = self.get_provinces()

        district_dir = RAW_DIR / "districts"
        district_dir.mkdir(
            parents=True,
            exist_ok=True,
        )

        regencies = []

        for province in provinces:
            regencies.extend(
                self.get_regencies(
                    province["kode_bps"],
                )
            )

        for regency in tqdm(
            regencies,
            desc="Downloading Districts",
            unit="regency",
        ):
            regency_code = regency["kode_bps"]

            districts = self.get_districts(
                regency_code,
            )

            self._save_json(
                districts,
                district_dir / f"{regency_code}.json",
            )

        print("\n✓ All districts downloaded.")

    def download_villages_by_regency(
        self,
        regency_code: str,
    ) -> None:
        """
        Download seluruh desa/kelurahan
        untuk satu kabupaten/kota.
        """

        village_dir = RAW_DIR / "villages"
        village_dir.mkdir(
            parents=True,
            exist_ok=True,
        )

        districts = self.get_districts(
            regency_code,
        )

        for district in tqdm(
            districts,
            desc=f"Downloading Villages ({regency_code})",
            unit="district",
        ):
            district_code = district["kode_bps"]

            villages = self.get_villages(
                district_code,
            )

            self._save_json(
                villages,
                village_dir / f"{district_code}.json",
            )

        print("\n✓ Villages downloaded.")
