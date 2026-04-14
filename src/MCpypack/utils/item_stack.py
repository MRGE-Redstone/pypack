# This file contains the ItemStack class used representing an itemstack.
# In earlier versions we used to different result classes for this.
# But itemstacks are also used in other places than results of recipes.
# Also Minecraft lately supports counts for almost all recipes.

from dataclasses import dataclass

from MCpypack.item import item, components

# Earlier CountedResult
class ItemStack:
    """
    An itemstack.
    """

    @property
    def item_id(self) -> item.Item:
        return self._item_id

    @item_id.setter
    def item_id(self, new_item_id: item.Item) -> None:
        if not isinstance(new_item_id, item.Item):
            raise TypeError(f"item_it must be of type 'item.Item', got: {type(new_item_id)}")

        self._item_id = new_item_id

    @property
    def count(self) -> int:
        return self._count

    @count.setter
    def count(self, value: int) -> None:
        if not isinstance(value, int):
            raise TypeError(f"count must be an integer, got: {type(value)}")

        if not 1 <= value <= 99:
            raise ValueError(f"count must be between 1 and 99, got {value}")
        self._count = value

    @property
    def components(self) -> components.ItemComponents | None:
        return self._components

    @components.setter
    def components(self, new_components: components.ItemComponents | None) -> None:
        if not isinstance(new_components, components.ItemComponents | None):
            raise TypeError(f"components must be of type 'components.ItemComponents' or 'None', got: {type(new_components)}")

        self._components = new_components

    def __init__(self,
                 *,
                 item_id: item.Item,
                 count: int = 1,
                 components: components.ItemComponents | None = None,
                 ) -> None:
        """
        Init a new itemstack.

        Parameters
        ----------
        item_id:
            Id of the item.
        count:
            Amount of the item.
        components:
            Additional components the item should get.
        """

        self.item_id = item_id
        self.count = count
        self.components = components

    def to_dict(self) -> dict:
        """
        Return the item_stack as a dict.
        """

        result: dict = {}

        result["id"] = self.item_id.value

        if self.count != 1:
            result["count"] = self.count

        if self.components:
            result["components"] = self.components.config

        return result
