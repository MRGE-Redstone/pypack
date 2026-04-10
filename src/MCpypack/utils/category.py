# This file contains the Category enum used to represent the category in which
# each recipe is put into
# It also contains the CategoryLike type which is the Category type or the
# str type

from enum import StrEnum
from typing import TypeAlias

class Category(StrEnum):
    """
    Enum for different recipe book categories.
    Available values are "equipment", "building", "misc", and "redstone".
    """

    EQUIPMENT = "equipment"
    BUILDING = "building"
    MISC = "misc"
    REDSTONE = "redstone"

    def __str__(self) -> str:
        """
        Return string representation of current value.
        """

        return self.value

    @classmethod
    def values(cls) -> list[str]:
        """
        Return a list of all possible category values.
        """

        return [c.value for c in cls]

    @classmethod
    def from_str(cls, value: str) -> Category:
        """
        Turn string into a possible value or raise ValueError.

        Parameters
        ----------
        value:
            String which will be converted into Category enum.
        """

        try:
            return cls(value)
        except ValueError:
            raise ValueError(f"Invalid category: {value}")

CategoryLike: TypeAlias = Category | str
