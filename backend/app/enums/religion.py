from enum import Enum


class Religion(str, Enum):
    """
    Citizen religion.
    """

    ISLAM = "Islam"
    CHRISTIAN = "Christian"
    CATHOLIC = "Catholic"
    HINDU = "Hindu"
    BUDDHIST = "Buddhist"
    CONFUCIAN = "Confucian"