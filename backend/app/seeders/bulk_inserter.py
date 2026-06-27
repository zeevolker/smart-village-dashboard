from typing import Any

from sqlalchemy import insert
from sqlalchemy.orm import Session


class BulkInserter:

    def __init__(self, db: Session):
        self.db = db

    def insert(
        self,
        model: type,
        rows: list[dict[str, Any]],
    ) -> None:

        if not rows:
            return

        try:
            self.db.execute(
                insert(model),
                rows,
            )

            self.db.commit()

        except Exception:
            self.db.rollback()
            raise