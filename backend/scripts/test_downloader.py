from app.etl.downloader import TerritoryDownloader


def main():
    downloader = TerritoryDownloader()

    downloader.download_villages_by_regency(
        "3201",
    )


if __name__ == "__main__":
    main()
