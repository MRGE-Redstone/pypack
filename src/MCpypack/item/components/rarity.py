# This file contains the rarity component

from .components import ItemComponent
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from MCpypack import utils

class Rarity(ItemComponent):
    """
    Rarity item component.
    Sets the rarity of this item, which affects the default color of its name.
    """

    TYPE = "minecraft:rarity"

    def __init__(self, rarity: utils.Rarity) -> None:
        """
        Init a rarity item component.

        Parameters
        ----------
        rarity:
            Rarity of the item.
        """
        super().__init__()

        self.rarity: str = rarity.value

    def to_value(self) -> str:
        return self.rarity
