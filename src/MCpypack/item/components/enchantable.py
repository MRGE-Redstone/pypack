# This file contains the enchantable component

from .components import ItemComponent

class Enchantable(ItemComponent):
    """
    Enchantable item component.
    If this and minecraft:enchantments are present on an item, and applicable enchantments are available, the item can be enchanted in an enchanting table.
    """

    TYPE = "minecraft:enchantable"

    @property
    def value(self) -> int:
        return self._value

    @value.setter
    def value(self, new_value: int) -> None:
        if not (new_value > 0):
            raise ValueError(f"value must be greater than 0 for enchantable component, got: {new_value}")

        self._value = new_value

    def __init__(self, value: int) -> None:
        """
        Init an enchantable item component.

        Parameters
        ----------
        value:
            Positive integer representing the item's enchantability. A higher value allows enchantments with a higher cost to be picked.
        """

        super().__init__()

        self.value = value

    def to_value(self) -> dict[str, int]:
        return {"value":self.value}

