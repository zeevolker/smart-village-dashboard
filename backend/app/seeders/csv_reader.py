import csv
from pathlib import Path


class CsvReader:
    """
    Utility untuk membaca file CSV.
    """

    def __init__(self, filepath: Path):
        self.filepath = filepath

    def read(self) -> list[dict[str, str]]:
        if not self.filepath.exists():
            raise FileNotFoundError(
                f"Dataset not found: {self.filepath}"
            )

        with self.filepath.open(
            mode="r",
            encoding="utf-8-sig",
            newline="",
        ) as file:

            reader = csv.DictReader(file)

            return list(reader)