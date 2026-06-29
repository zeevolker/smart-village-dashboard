"""create households table

Revision ID: 6de9129e6574
Revises: 4416670938d8
Create Date: 2026-06-29 10:40:04.215966

"""

from typing import Sequence, Union

import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision: str = "6de9129e6574"
down_revision: Union[str, Sequence[str], None] = "4416670938d8"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""

    op.create_table(
        "households",
        sa.Column(
            "kk_number",
            sa.String(length=16),
            nullable=False,
        ),
        sa.Column(
            "address",
            sa.String(length=255),
            nullable=False,
        ),
        sa.Column(
            "rt",
            sa.String(length=3),
            nullable=False,
        ),
        sa.Column(
            "rw",
            sa.String(length=3),
            nullable=False,
        ),
        sa.Column(
            "postal_code",
            sa.String(length=5),
            nullable=False,
        ),
        sa.Column(
            "village_id",
            sa.UUID(),
            nullable=False,
        ),
        sa.Column(
            "id",
            sa.UUID(),
            nullable=False,
        ),
        sa.Column(
            "created_at",
            sa.DateTime(timezone=True),
            server_default=sa.text("now()"),
            nullable=False,
        ),
        sa.Column(
            "updated_at",
            sa.DateTime(timezone=True),
            server_default=sa.text("now()"),
            nullable=False,
        ),
        sa.ForeignKeyConstraint(
            ["village_id"],
            ["villages.id"],
            ondelete="RESTRICT",
        ),
        sa.PrimaryKeyConstraint(
            "id",
        ),
    )

    op.create_index(
        op.f("ix_households_kk_number"),
        "households",
        ["kk_number"],
        unique=True,
    )

    op.create_index(
        "ix_households_village_id",
        "households",
        ["village_id"],
    )

    op.add_column(
        "citizens",
        sa.Column(
            "household_id",
            sa.UUID(),
            nullable=True,
        ),
    )

    op.create_foreign_key(
        "fk_citizens_household_id",
        "citizens",
        "households",
        ["household_id"],
        ["id"],
        ondelete="SET NULL",
    )


def downgrade() -> None:
    """Downgrade schema."""

    op.drop_constraint(
        "fk_citizens_household_id",
        "citizens",
        type_="foreignkey",
    )

    op.drop_column(
        "citizens",
        "household_id",
    )

    op.drop_index(
        "ix_households_village_id",
        table_name="households",
    )

    op.drop_index(
        op.f("ix_households_kk_number"),
        table_name="households",
    )

    op.drop_table(
        "households",
    )