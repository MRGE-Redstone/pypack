# This file contains the base_color component

from .components import ItemComponent
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from MCpypack.utils import Color

class BaseColor(ItemComponent):
    """
    Base color item component.
    The base dye color of the banner applied on a shield.
    """

    @property
    def TYPE(self) -> str:
        return "minecraft:base_color"

    def __init__(self, color: Color) -> None:
        """
        Init a base color item component.

        Parameters
        ----------
        color:
            Base color of the item.
            It should be applied on a shield.
        """
        super().__init__()

        self.color: str = color.value

    def to_value(self) -> str:
        return self.color
