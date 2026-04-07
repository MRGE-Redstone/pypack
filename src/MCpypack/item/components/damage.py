# This file contains the damage component

from .components import ItemComponent

class Damage(ItemComponent):
    """
    Damage item component.
    """

    @property
    def TYPE(self) -> str:
        return "minecraft:damage"

    @property
    def damage(self) -> int:
        return self._damage

    @damage.setter
    def damage(self, value: int) -> None:
        if not 0 <= value:
            raise ValueError(f"damage must be a positive integer, got: damage = {value}")

        self._damage = value

    def __init__(self, damage: int) -> None:
        """
        Init damage component.
        
        Parameters
        ----------
        damage:
            The number of uses consumed (not remaining) of the item's durability. Must be a non-negative integer, defaults to 0. If not present, the item cannot take damage.
        """

        super().__init__()

        self.damage = damage

    def to_value(self) -> int:
        return self.damage

