from app.etl.cleaner import TerritoryCleaner
from app.etl.normalizer import TerritoryNormalizer
from app.etl.validator import TerritoryValidator


def main() -> None:

    normalizer = TerritoryNormalizer()
    cleaner = TerritoryCleaner()
    validator = TerritoryValidator()

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

        validator.validate(cleaned)

        print(f"✓ {name:<12}{len(cleaned)} rows valid")


if __name__ == "__main__":
    main()
