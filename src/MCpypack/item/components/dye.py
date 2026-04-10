# This file contains the dye component

from .components import ItemComponent
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from MCpypack.utils import Color

class Dye(ItemComponent):
    """
    Dye item component.
    When present on an item, stores the color of dye that this item can be used as for the purpose of crafting recipes and mob or block interactions.
    """

    @property
    def TYPE(self) -> str:
        return "minecraft:dye"

    def __init__(self, dye: Color) -> None:
        """
        Init a dye item component.

        Parameters
        ----------
        color:
            Dye the item should be behave as.
        """
        super().__init__()

        self.dye: str = dye.value

    def to_value(self) -> str:
        return self.dye
