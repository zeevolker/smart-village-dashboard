from app.etl.cleaner import TerritoryCleaner
from app.etl.normalizer import TerritoryNormalizer


def main():

    normalizer = TerritoryNormalizer()

    cleaner = TerritoryCleaner()

    datasets = {
        "provinces": normalizer.normalize_provinces(),
        "regencies": normalizer.normalize_regencies(),
        "districts": normalizer.normalize_districts(),
        "villages": normalizer.normalize_villages(),
    }

    for name, rows in datasets.items():
        cleaned = cleaner.clean(
            rows,
            name,
        )

        print(f"{name:<12}{len(cleaned)} valid rows")


if __name__ == "__main__":
    main()
