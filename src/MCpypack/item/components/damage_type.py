# This file contains the damage_type component

from .components import ItemComponent

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from MCpypack.item.final import DamageType as DamageTypeEnum

class DamageType(ItemComponent):
    """
    Damage type item component.
    """

    @property
    def TYPE(self) -> str:
        return "minecraft:damage_type"

    def __init__(self, damage_type: DamageTypeEnum) -> None:
        """
        Init damage_type component.
        
        Parameters
        ----------
        damage_type:
        """

        super().__init__()

        self.damage_type = damage_type

    def to_value(self) -> str:
        return self.damage_type.value

