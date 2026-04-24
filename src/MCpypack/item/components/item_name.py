# This file contains the item_name component

from .components import ItemComponent
from MCpypack.utils import PlainText

class ItemName(ItemComponent):
    """
    Item name item component.
    Unlike the minecraft:custom_name component, this name cannot be erased using an anvil, is not italicized, and does not appear in some labels, such as banner markers and item frames.
    """

    @property
    def TYPE(self) -> str:
        return "minecraft:item_name"

    @property
    def item_name(self) -> PlainText:
        return self._item_name

    @item_name.setter
    def item_name(self, value: PlainText) -> None:
        if not isinstance(value, PlainText):
            raise ValueError(f"item_name must be of type PlainText, got: {type(value)}")

        self._item_name = value

    def __init__(self,
                 item_name: PlainText,
                 ) -> None:
        """
        Init item name component.

        Parameters
        ----------
        item_name:
            The default name of this item, as a text component.
        """

        super().__init__()

        self.item_name = item_name

    def to_value(self) -> dict:
        return self.item_name.to_dict()
