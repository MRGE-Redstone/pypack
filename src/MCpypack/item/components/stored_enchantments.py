# This file contains the stored_enchantments component

from .components import ItemComponent
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from MCpypack.item import enchantment

class StoredEnchantments(ItemComponent):
    """
    Stored enchantments item component.
    Items with this component do not have the enchantment.
    See Enchantments component for this.
    """

    @property
    def TYPE(self) -> str:
        return "minecraft:stored_enchantments"

    def __init__(self, stored_enchantments: dict[enchantment.Enchantment, int]) -> None:
        """
        Init stored enchantments item component.

        Parameters
        ----------
        stored_enchantments:
            Dictionary of stored enchantments and their levels.
            Levels must be greater than 0.
        """

        super().__init__()

        # Level greater than 0
        for enchantment, level in stored_enchantments.items():
            if not level > 0:
                raise ValueError(f"Enchantment level must be greater than 0, got: {level} for {enchantment}!")

        self.stored_enchantments: dict[str, int] = {enchantment.value: level for enchantment, level in stored_enchantments.items()}


    def to_value(self) -> dict[str, int]:
        return self.stored_enchantments
