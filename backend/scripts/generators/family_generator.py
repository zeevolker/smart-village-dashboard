from __future__ import annotations

import random

from app.enums.relationship import RelationshipType


class FamilyGenerator:
    """
    Generate realistic household compositions.
    """

    FAMILY_PATTERNS = (
        (
            RelationshipType.HEAD,
            RelationshipType.SPOUSE,
        ),
        (
            RelationshipType.HEAD,
            RelationshipType.SPOUSE,
            RelationshipType.CHILD,
        ),
        (
            RelationshipType.HEAD,
            RelationshipType.SPOUSE,
            RelationshipType.CHILD,
            RelationshipType.CHILD,
        ),
        (
            RelationshipType.HEAD,
            RelationshipType.SPOUSE,
            RelationshipType.CHILD,
            RelationshipType.CHILD,
            RelationshipType.CHILD,
        ),
        (
            RelationshipType.HEAD,
            RelationshipType.PARENT,
        ),
        (
            RelationshipType.HEAD,
            RelationshipType.SIBLING,
        ),
    )

    @classmethod
    def generate_structure(
        cls,
    ) -> list[RelationshipType]:
        """
        Generate a family structure without citizen data.
        """

        return list(
            random.choice(
                cls.FAMILY_PATTERNS
            )
        )