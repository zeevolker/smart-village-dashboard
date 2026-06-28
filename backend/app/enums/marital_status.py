from enum import Enum


class MaritalStatus(str, Enum):
    """
    Citizen marital status.
    """

    SINGLE = "Single"
    MARRIED = "Married"
    DIVORCED = "Divorced"
    WIDOWED = "Widowed"