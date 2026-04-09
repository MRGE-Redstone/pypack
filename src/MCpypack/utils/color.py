# This file contains the color enum

from enum import StrEnum

class Color(StrEnum):
    """
    Enum for Minecraft color types.
    """

    WHITE = "white"
    LIGHT_GREY = "light_gray"
    GREY = "gray"
    BLACK = "black"
    BROWN = "brown"
    RED = "red"
    ORANGE = "orange"
    YELLOW = "yellow"
    LIME = "lime"
    GREEN = "green"
    CYAN = "cyan"
    LIGHT_BLUE = "light_blue"
    BLUE = "blue"
    PURPLE = "purple"
    MAGENTA = "magenta"
    PINK = "pink"

    def __str__(self) -> str:
        """
        Return string representation of current value.
        """

        return self.value

    @classmethod
    def values(cls) -> list[str]:
        """
        Return a list of all possible color types.
        """

        return [c.value for c in cls]

    @classmethod
    def from_str(cls, value: str) -> Color:
        """
        Turn string into a possible value or raise ValueError.

        Parameters
        ----------
        value:
            String which will be converted into a color.
        """

        try:
            return cls(value)
        except ValueError:
            raise ValueError(f"Invalid color: {value}")
