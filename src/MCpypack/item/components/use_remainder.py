# This file contains the use_remainder component

from .components import ItemComponent

from MCpypack.utils import ItemStack

class UseRemainder(ItemComponent):
    """
    Use remainder item component.
    If present, replaces the item with a remainder item if its stack count has decreased after use.
    """

    TYPE = "minecraft:use_remainder"

    @property
    def use_remainder(self) -> ItemStack:
        return self._use_remainder

    @use_remainder.setter
    def use_remainder(self, use_remainder: ItemStack) -> None:
        if not isinstance(use_remainder, ItemStack):
            raise TypeError(f"use_remainder must be of type ItemStack, got: {type(use_remainder)}")

        self._use_remainder = use_remainder

    def __init__(self, use_remainder: ItemStack) -> None:
        """
        Init use remainder component.

        Parameters
        ----------
        use_remainder:
            A single item stack.
        """

        super().__init__()

        self.use_remainder = use_remainder

    def to_value(self) -> dict:
        return self.use_remainder.to_dict()
