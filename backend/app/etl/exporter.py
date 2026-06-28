from __future__ import annotations

import csv
from pathlib import Path
from typing import Any


PROCESSED_DIR = Path("data/processed")


class TerritoryExporter:
    """
    Export dataset menjadi CSV.
    """

    def __init__(self):

        PROCESSED_DIR.mkdir(
            parents=True,
            exist_ok=True,
        )

    def export_csv(
        self,
        rows: list[dict[str, Any]],
        filename: str,
    ) -> None:

        if not rows:
            print(f"{filename}: no data.")
            return

        filepath = PROCESSED_DIR / filename

        fieldnames = rows[0].keys()

        with filepath.open(
            "w",
            newline="",
            encoding="utf-8",
        ) as file:

            writer = csv.DictWriter(
                file,
                fieldnames=fieldnames,
            )

            writer.writeheader()

            writer.writerows(rows)

        print(f"✓ {filename} exported.")