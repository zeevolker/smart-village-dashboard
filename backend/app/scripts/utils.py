from pathlib import Path


BASE_DIR = Path(__file__).resolve().parents[2]

DATA_DIR = BASE_DIR / "data"


def csv_path(filename: str) -> Path:
    """
    Mengembalikan path file CSV pada folder data.
    """
    return DATA_DIR / filename