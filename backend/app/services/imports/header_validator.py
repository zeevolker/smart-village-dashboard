class HeaderValidator:
    """
    Validasi header file Excel citizen.
    """

    REQUIRED_HEADERS = [
        "nik",
        "full_name",
        "gender",
        "birth_place",
        "birth_date",
        "religion",
        "marital_status",
        "occupation",
        "phone_number",
        "household_id",
        "village_id",
    ]

    def validate(
        self,
        headers: list[str],
    ) -> None:
        """
        Raise ValueError jika header tidak sesuai.
        """

        if headers != self.REQUIRED_HEADERS:
            raise ValueError(
                "Invalid Excel header."
            )