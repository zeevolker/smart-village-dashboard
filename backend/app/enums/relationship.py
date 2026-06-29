from enum import Enum


class RelationshipType(
    str,
    Enum,
):
    """
    Relationship to the head of household.
    """

    HEAD = "Head"
    SPOUSE = "Spouse"
    CHILD = "Child"
    PARENT = "Parent"
    SIBLING = "Sibling"
    OTHER = "Other"