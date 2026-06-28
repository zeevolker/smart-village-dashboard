from pathlib import Path

DATA_DIR = Path(__file__).parent.parent / "data"


def csv_path(filename: str) -> Path:
    """
    Mengembalikan path file CSV di folder data.
    """
    return DATA_DIR / filename
