# This file contains the rarity enum

from enum import StrEnum

class Rarity(StrEnum):
    """
    Rarity for Minecraft rarities.
    """

    COMMON = "common"
    UNCOMMON = "uncommon"
    RARE = "rare"
    EPIC = "epic"

    def __str__(self) -> str:
        """
        Return string representation of current value.
        """

        return self.value

    @classmethod
    def values(cls) -> list[str]:
        """
        Return a list of all existing rarities.
        """

        return [c.value for c in cls]

    @classmethod
    def from_str(cls, value: str) -> Rarity:
        """
        Turn string into a possible value or raise ValueError.

        Parameters
        ----------
        value:
            String which will be converted into a rarity.
        """

        try:
            return cls(value)
        except ValueError:
            raise ValueError(f"Invalid rarity: {value}")

