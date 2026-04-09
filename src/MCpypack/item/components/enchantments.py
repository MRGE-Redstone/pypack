# This file contains the enchantments component

from .components import ItemComponent
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from MCpypack.item import enchantment

class Enchantments(ItemComponent):
    """
    Enchantments item component.
    """

    @property
    def TYPE(self) -> str:
        return "minecraft:enchantments"

    def __init__(self, enchantments: dict[enchantment.Enchantment, int]) -> None:
        """
        Init  enchantments item component.

        Parameters
        ----------
        enchantments:
            Dictionary of enchantment and its level.
        """

        super().__init__()

        self.enchantments: dict[str, int] = {enchantment.value: level for enchantment, level in enchantments.items()}


    def to_value(self) -> dict[str, int]:
        return self.enchantments
