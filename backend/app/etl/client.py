from typing import Any

import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

from app.etl.constants import (
    BRIDGING_DAGRI_URL,
    BRIDGING_URL,
    PERIODE_MERGE,
    REQUEST_TIMEOUT,
)


HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/149.0.0.0 Safari/537.36"
    ),
    "Referer": "https://sig.bps.go.id/bridging-kode/index",
    "X-Requested-With": "XMLHttpRequest",
    "Accept": "application/json, text/plain, */*",
}


class BPSClient:
    """
    HTTP Client untuk Bridging API BPS.
    """

    TERRITORY_ENDPOINTS = {
        "provinsi": BRIDGING_DAGRI_URL,
        "kabupaten": BRIDGING_DAGRI_URL,
        "kecamatan": BRIDGING_URL,
        "desa": BRIDGING_URL,
    }

    def __init__(self) -> None:
        self.session = requests.Session()

        self.session.headers.update(HEADERS)

        retry = Retry(
            total=5,
            backoff_factor=1,
            status_forcelist=[
                429,
                500,
                502,
                503,
                504,
            ],
            allowed_methods=["GET"],
        )

        adapter = HTTPAdapter(
            max_retries=retry,
        )

        self.session.mount(
            "https://",
            adapter,
        )

        self.session.mount(
            "http://",
            adapter,
        )

    def get_wilayah(
        self,
        level: str,
        parent: str | int,
    ) -> list[dict[str, Any]]:
        """
        Mengambil data wilayah dari API BPS.
        """

        if level not in self.TERRITORY_ENDPOINTS:
            raise ValueError(
                f"Unknown level: {level}"
            )

        response = self.session.get(
            self.TERRITORY_ENDPOINTS[level],
            params={
                "level": level,
                "parent": parent,
                "periode_merge": PERIODE_MERGE,
            },
            timeout=REQUEST_TIMEOUT,
        )

        response.raise_for_status()

        data = response.json()

        if level == "kecamatan" and str(parent) == "7210":
            print("\n=== DEBUG 7210 ===")

            for row in data:
                if row["kode_bps"] == "7210121":
                    print(row)

            print("==================\n")

        if not isinstance(data, list):
            raise ValueError(
                f"Unexpected response for level={level}"
            )

        return data