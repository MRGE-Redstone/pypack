# This file contains the result classes used to express the result of a recipe.
# Some recipes support an amount of items, but some do not.
# We handle this using two different classes:
# 1) SimpleResult  -> No amount of item can be specified.
# 2) CountedResult -> Amount of item can be specified.

from dataclasses import dataclass

from MCpypack.item import Item

@dataclass
class SimpleResult:
    """
    Result of a recipe that does not contain an item count.
    """

    item_id: Item

    def to_dict(self) -> dict[str, str]:
        """
        Return the result as a dict.
        """

        return {
            "id": self.item_id.value,
        }

# CountedResult is not a dataclass.
# This is due to the need of validation for the count property.
# With a dataclass, the user would have to type:
#   CountedResult(item_id=item, _count=count)
# This is inconvenient and we want the user to be able to type:
#   CountedResult(item_id=item, count=count)
class CountedResult:
    """
    Result of a recipe that can contain an item count.
    """

    def __init__(self,
                 item_id: Item,
                 count: int = 1,
                 ) -> None:
        """
        Init a new recipe with a count.

        Parameters
        ----------
        item_id:
            Id of the item.
        count:
            Amount of the item.
        """

        self.item_id: Item = item_id
        self.count = count

    @property
    def count(self) -> int:
        return self._count

    @count.setter
    def count(self, value: int) -> None:
        if not 1 <= value <= 64:
            raise ValueError(f"count must be between 1 and 64, got {value}")
        self._count = value

    def to_dict(self) -> dict[str, str | int]:
        """
        Return the result as a dict.
        """

        result: dict[str, str | int] = {}

        result["id"] = self.item_id.value

        if self.count != 1:
            result["count"] = self.count

        return result
