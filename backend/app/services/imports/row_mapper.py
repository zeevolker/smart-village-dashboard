class RowMapper:
    """
    Mengubah satu baris Excel menjadi dictionary.
    """

    def map(
        self,
        headers: list[str],
        row: tuple,
    ) -> dict:
        return {
            header: value
            for header, value in zip(
                headers,
                row,
            )
        }