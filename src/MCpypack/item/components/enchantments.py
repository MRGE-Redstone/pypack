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
            Dictionary of enchantments and their levels.
            Levels must be greater than 0.
        """

        super().__init__()

        # Level greater than 0
        for enchantment, level in enchantments.items():
            if not level > 0:
                raise ValueError(f"Enchantment level must be greater than 0, got: {level} for {enchantment}!")

        self.enchantments: dict[str, int] = {enchantment.value: level for enchantment, level in enchantments.items()}

    def to_value(self) -> dict[str, int]:
        return self.enchantments
