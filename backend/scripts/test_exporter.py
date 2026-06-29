from app.etl.cleaner import TerritoryCleaner
from app.etl.exporter import TerritoryExporter
from app.etl.normalizer import TerritoryNormalizer


def main() -> None:

    normalizer = TerritoryNormalizer()
    cleaner = TerritoryCleaner()
    exporter = TerritoryExporter()

    datasets = {
        "provinces.csv": normalizer.normalize_provinces(),
        "regencies.csv": normalizer.normalize_regencies(),
        "districts.csv": normalizer.normalize_districts(),
        "villages.csv": normalizer.normalize_villages(),
    }

    for filename, rows in datasets.items():
        cleaned = cleaner.clean(
            rows,
            filename.replace(".csv", ""),
        )

        exporter.export_csv(
            cleaned,
            filename,
        )


if __name__ == "__main__":
    main()
