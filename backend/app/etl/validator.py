from __future__ import annotations

from collections import Counter
from typing import Any


class TerritoryValidator:
    """
    Validasi dataset wilayah.
    """

    REQUIRED_FIELDS = (
        "code",
        "bps_code",
        "name",
    )

    def validate(
        self,
        rows: list[dict[str, Any]],
    ) -> None:
        """
        Jalankan seluruh validasi.
        """

        self._validate_required_fields(rows)
        self._validate_duplicate_code(rows)
        self._validate_duplicate_bps(rows)
        
    def _validate_required_fields(
        self,
        rows: list[dict[str, Any]],
    ) -> None:

        for index, row in enumerate(rows, start=1):

            for field in self.REQUIRED_FIELDS:

                value = row.get(field)

                if value is None:
                    raise ValueError(
                        f"Row {index}: '{field}' is missing."
                    )

                if str(value).strip() == "":
                    raise ValueError(
                        f"Row {index}: '{field}' is empty."
                    )
                    
    def _validate_duplicate_code(
        self,
        rows: list[dict[str, Any]],
    ) -> None:

        codes = [row["code"] for row in rows]

        duplicates = [
            code
            for code, count in Counter(codes).items()
            if count > 1
        ]

        if duplicates:
            raise ValueError(
                f"Duplicate code: {duplicates[:10]}"
            )
            
    def _validate_duplicate_bps(
        self,
        rows: list[dict[str, Any]],
    ) -> None:

        codes = [row["bps_code"] for row in rows]

        duplicates = [
            code
            for code, count in Counter(codes).items()
            if count > 1
        ]

        if duplicates:
            raise ValueError(
                f"Duplicate bps_code: {duplicates[:10]}"
            )