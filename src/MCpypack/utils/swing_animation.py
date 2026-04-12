# This file contains the SwingAnimation enum

from enum import StrEnum

class SwingAnimation(StrEnum):
    """
    Enum for Minecraft color types.
    """

    NONE = "none"
    WHACK = "whack"
    STAB = "stab"

    def __str__(self) -> str:
        """
        Return string representation of current value.
        """

        return self.value

    @classmethod
    def values(cls) -> list[str]:
        """
        Return a list of all possible swing animation types.
        """

        return [c.value for c in cls]

    @classmethod
    def from_str(cls, value: str) -> SwingAnimation:
        """
        Turn string into a possible value or raise ValueError.

        Parameters
        ----------
        value:
            String which will be converted into a swing animation.
        """

        try:
            return cls(value)
        except ValueError:
            raise ValueError(f"Invalid swing animation: {value}")
