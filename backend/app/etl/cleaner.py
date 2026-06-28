from __future__ import annotations

from collections import defaultdict
from typing import Any


class TerritoryCleaner:
    """
    Membersihkan data wilayah dari anomali API BPS.
    """

    def clean(
        self,
        rows: list[dict[str, Any]],
    ) -> list[dict[str, Any]]:
        """
        Jalankan seluruh proses cleaning.
        """

        rows = self._remove_invalid_rows(rows)

        rows = self._remove_duplicate_dagri(rows)

        return rows

    def _remove_duplicate_dagri(
        self,
        rows: list[dict[str, Any]],
    ) -> list[dict[str, Any]]:
        """
        Jika satu kode_dagri memiliki lebih dari satu record,
        pilih record terbaik.
        """

        groups: dict[str, list[dict[str, Any]]] = defaultdict(list)

        for row in rows:
            groups[row["kode_dagri"]].append(row)

        cleaned: list[dict[str, Any]] = []

        removed = 0

        for _dagri_code, candidates in groups.items():
            if len(candidates) == 1:
                cleaned.append(candidates[0])
                continue

            best = self._choose_best_candidate(
                candidates,
            )

            cleaned.append(best)

            removed += len(candidates) - 1

        if removed:
            print(f"Cleaner removed {removed} duplicate rows.")

        return cleaned

    def _choose_best_candidate(
        self,
        candidates: list[dict[str, Any]],
    ) -> dict[str, Any]:
        """
        Memilih record terbaik.
        """

        # Prioritas 1:
        # nama_bps == nama_dagri

        for row in candidates:
            if row["nama_bps"].strip().upper() == row["nama_dagri"].strip().upper():
                return row

        # Prioritas 2:
        # kode_bps terpendek

        return min(
            candidates,
            key=lambda row: len(row["kode_bps"]),
        )

    def _remove_invalid_rows(
        self,
        rows: list[dict[str, Any]],
    ) -> list[dict[str, Any]]:
        """
        Menghapus record yang tidak memiliki kode Dagri.
        """

        cleaned = []

        removed = 0

        for row in rows:
            dagri = row.get("kode_dagri", "").strip()

            if not dagri:
                removed += 1
                continue

            cleaned.append(row)

        if removed:
            print(f"Cleaner removed {removed} invalid rows.")

        return cleaned
