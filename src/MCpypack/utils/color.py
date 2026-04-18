# This file contains the color enums and classes

from enum import StrEnum
import re

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

class HexColor:
    """
    Color class that uses a hex value for the color.
    """

    HEX_PATTERN = re.compile(r"^[0-9a-fA-F]{6}$")

    @property
    def color(self) -> str:
        return self._color

    @color.setter
    def color(self, value: str) -> None:
        if not isinstance(value, str):
            raise ValueError(f"color must be a string, got: type = {type(value)}")

        if not self.HEX_PATTERN.fullmatch(value):
            raise ValueError(f"color must be a valid 6-digit hex string, got: {value}")

        self._color = f"#{value.upper()}"

    def __init__(self,
                 color: str
                 ) -> None:
        """
        Init a new HexColor object.
        """

        self.color = color

    @classmethod
    def from_str(cls, value: str) -> HexColor:
        """
        Turn string into a hex color.

        Parameters
        ----------
        value:
            String which will be converted into a color.
        """

        return cls(value)

class TextColor(StrEnum):
    """
    Enum for Minecraft text color types.
    """

    BLACK = "black"
    DARK_BLUE = "dark_blue"
    DARK_GREEN = "dark_green"
    DARK_AQUA = "dark_aqua"
    DARK_RED = "dark_red"
    DARK_PURPLE = "dark_purple"
    GOLD = "gold"
    GRAY = "gray"
    DARK_GRAY = "dark_gray"
    BLUE = "blue"
    GREEN = "green"
    AQUA = "aqua"
    RED = "red"
    LIGHT_PURPLE = "light_purple"
    YELLOW = "yellow"
    WHITE = "white"

    def __str__(self) -> str:
        """
        Return string representation of current value.
        """

        return self.value

    @classmethod
    def values(cls) -> list[str]:
        """
        Return a list of all possible text color types.
        """

        return [c.value for c in cls]

    @classmethod
    def from_str(cls, value: str) -> TextColor:
        """
        Turn string into a possible value or raise ValueError.

        Parameters
        ----------
        value:
            String which will be converted into a text color.
        """

        try:
            return cls(value)
        except ValueError:
            raise ValueError(f"Invalid text color: {value}")
