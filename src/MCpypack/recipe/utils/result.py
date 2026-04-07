# This file contains the result classes used to express the result of a recipe.
# Some recipes support an amount of items, but some do not.
# We handle this using two different classes:
# 1) SimpleResult  -> No amount of item can be specified.
# 2) CountedResult -> Amount of item can be specified.

from dataclasses import dataclass

from MCpypack.item import Item, ItemComponents

@dataclass
class SimpleResult:
    """
    Result of a recipe that does not contain an item count.
    """

    item_id: Item
    components: ItemComponents | None = None

    def to_dict(self) -> dict:
        """
        Return the result as a dict.
        """

        result: dict = {
            "id": self.item_id.value,
        }

        if self.components is not None:
            result["components"] = self.components.config

        return result

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
                 components: ItemComponents | None = None,
                 ) -> None:
        """
        Init a new recipe with a count.

        Parameters
        ----------
        item_id:
            Id of the item.
        count:
            Amount of the item.
        components:
            Additional components the item should get.
        """

        self.item_id: Item = item_id
        self.count = count
        if components is not None:
            self.components: ItemComponents = components

    @property
    def count(self) -> int:
        return self._count

    @count.setter
    def count(self, value: int) -> None:
        if not 1 <= value <= 99:
            raise ValueError(f"count must be between 1 and 99, got {value}")
        self._count = value

    def to_dict(self) -> dict:
        """
        Return the result as a dict.
        """

        result: dict = {}

        result["id"] = self.item_id.value

        if self.count != 1:
            result["count"] = self.count

        if self.components:
            result["components"] = self.components.config

        return result
