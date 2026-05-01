# This file contains the provides_trim_material component

from MCpypack.item.final import trim_materials
from .components import ItemComponent
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from MCpypack.item.final import TrimMaterial

class ProvidesTrimMaterial(ItemComponent):
    """
    Provides trim material item component.
    When present, this item provides the specified trim material when used in a trimming recipe.
    """

    TYPE = "minecraft:provides_trim_material"

    def __init__(self, trim_material: TrimMaterial) -> None:
        """
        Init provides trim material component.

        Parameters
        ----------
        trim_material:
            Specifies trim material.
        """

        super().__init__()

        self.trim_material: str = trim_material.value

    def to_value(self) -> str:
        return self.trim_material
