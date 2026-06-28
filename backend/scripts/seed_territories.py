from scripts.utils import csv_path


def main():
    print("===================================")
    print(" Smart Village Territory Seeder")
    print("===================================")

    print()

    print("Dataset location:")

    print(csv_path("provinces.csv"))

    print(csv_path("regencies.csv"))

    print(csv_path("districts.csv"))

    print(csv_path("villages.csv"))


if __name__ == "__main__":
    main()
