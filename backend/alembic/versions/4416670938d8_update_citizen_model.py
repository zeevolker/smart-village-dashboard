"""update citizen model

Revision ID: 4416670938d8
Revises: d18efa630d9b
Create Date: 2026-06-28 16:09:26.391919
"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa

from app.enums.gender import Gender
from app.enums.marital_status import MaritalStatus
from app.enums.religion import Religion


# revision identifiers, used by Alembic.
revision: str = "4416670938d8"
down_revision: Union[str, Sequence[str], None] = "d18efa630d9b"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""

    bind = op.get_bind()

    gender_enum = sa.Enum(
        Gender,
        name="gender",
    )

    religion_enum = sa.Enum(
        Religion,
        name="religion",
    )

    marital_status_enum = sa.Enum(
        MaritalStatus,
        name="maritalstatus",
    )

    gender_enum.create(bind, checkfirst=True)
    religion_enum.create(bind, checkfirst=True)
    marital_status_enum.create(bind, checkfirst=True)

    op.add_column(
        "citizens",
        sa.Column(
            "gender",
            gender_enum,
            nullable=False,
        ),
    )

    op.add_column(
        "citizens",
        sa.Column(
            "birth_place",
            sa.String(length=100),
            nullable=False,
        ),
    )

    op.add_column(
        "citizens",
        sa.Column(
            "birth_date",
            sa.Date(),
            nullable=False,
        ),
    )

    op.add_column(
        "citizens",
        sa.Column(
            "religion",
            religion_enum,
            nullable=False,
        ),
    )

    op.add_column(
        "citizens",
        sa.Column(
            "marital_status",
            marital_status_enum,
            nullable=False,
        ),
    )

    op.add_column(
        "citizens",
        sa.Column(
            "occupation",
            sa.String(length=100),
            nullable=False,
        ),
    )

    op.add_column(
        "citizens",
        sa.Column(
            "phone_number",
            sa.String(length=20),
            nullable=True,
        ),
    )

    op.add_column(
        "citizens",
        sa.Column(
            "address",
            sa.String(length=255),
            nullable=False,
        ),
    )


def downgrade() -> None:
    """Downgrade schema."""

    bind = op.get_bind()

    gender_enum = sa.Enum(
        Gender,
        name="gender",
    )

    religion_enum = sa.Enum(
        Religion,
        name="religion",
    )

    marital_status_enum = sa.Enum(
        MaritalStatus,
        name="maritalstatus",
    )

    op.drop_column(
        "citizens",
        "address",
    )

    op.drop_column(
        "citizens",
        "phone_number",
    )

    op.drop_column(
        "citizens",
        "occupation",
    )

    op.drop_column(
        "citizens",
        "marital_status",
    )

    op.drop_column(
        "citizens",
        "religion",
    )

    op.drop_column(
        "citizens",
        "birth_date",
    )

    op.drop_column(
        "citizens",
        "birth_place",
    )

    op.drop_column(
        "citizens",
        "gender",
    )

    gender_enum.drop(bind, checkfirst=True)
    religion_enum.drop(bind, checkfirst=True)
    marital_status_enum.drop(bind, checkfirst=True)