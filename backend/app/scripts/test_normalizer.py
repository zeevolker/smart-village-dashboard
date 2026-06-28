from app.etl.normalizer import TerritoryNormalizer


def main():
    normalizer = TerritoryNormalizer()

    datasets = {
        "Provinces": normalizer.normalize_provinces(),
        "Regencies": normalizer.normalize_regencies(),
        "Districts": normalizer.normalize_districts(),
        "Villages": normalizer.normalize_villages(),
    }

    for name, rows in datasets.items():
        print("=" * 60)
        print(name)
        print(f"Total : {len(rows)}")
        print(rows[:3])
        print()


if __name__ == "__main__":
    main()