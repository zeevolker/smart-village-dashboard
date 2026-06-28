from enum import Enum


class Gender(str, Enum):
    """
    Citizen gender.
    """

    MALE = "Male"
    FEMALE = "Female"