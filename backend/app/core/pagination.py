from math import ceil

from sqlalchemy import Select, func, select
from sqlalchemy.orm import Session


class Paginator:

    def __init__(
        self,
        db: Session,
    ):
        self.db = db

    def paginate(
        self,
        stmt: Select,
        page: int = 1,
        size: int = 20,
    ) -> tuple[list, int]:

        page = max(page, 1)
        size = max(size, 1)

        count_stmt = (
            select(func.count())
            .select_from(stmt.subquery())
        )

        total = self.db.scalar(count_stmt) or 0

        rows = self.db.scalars(
            stmt.offset(
                (page - 1) * size
            ).limit(size)
        ).all()

        return rows, total

    @staticmethod
    def pages(
        total: int,
        size: int,
    ) -> int:

        if total == 0:
            return 0

        return ceil(total / size)