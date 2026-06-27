class CsvValidator:
    """
    Validator sederhana untuk dataset CSV.
    """

    @staticmethod
    def validate_headers(
        rows: list[dict],
        required_headers: list[str],
    ) -> None:

        if not rows:
            raise ValueError("Dataset is empty.")

        headers = list(rows[0].keys())

        missing = [
            header
            for header in required_headers
            if header not in headers
        ]

        if missing:
            raise ValueError(
                f"Missing required headers: {', '.join(missing)}"
            )