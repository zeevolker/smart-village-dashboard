"""add citizen relationship to household

Revision ID: f27be4fbd299
Revises: 6de9129e6574
Create Date: 2026-06-29 15:19:13.469198
"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers
revision: str = "f27be4fbd299"
down_revision: Union[str, Sequence[str], None] = "6de9129e6574"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


relationship_type = sa.Enum(
    "HEAD",
    "SPOUSE",
    "CHILD",
    "PARENT",
    "SIBLING",
    "OTHER",
    name="relationship_type",
)


def upgrade() -> None:
    """Upgrade schema."""

    relationship_type.create(op.get_bind(), checkfirst=True)

    op.add_column(
        "citizens",
        sa.Column(
            "relationship_to_head",
            relationship_type,
            nullable=True,
        ),
    )


def downgrade() -> None:
    """Downgrade schema."""

    op.drop_column(
        "citizens",
        "relationship_to_head",
    )

    relationship_type.drop(op.get_bind(), checkfirst=True)