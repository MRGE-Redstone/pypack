# This file contains the max_damage component

from .components import ItemComponent

class MaxDamage(ItemComponent):
    """
    Max damage item component.
    """

    @property
    def TYPE(self) -> str:
        return "minecraft:max_damage"

    @property
    def max_damage(self) -> int:
        return self._max_damage

    @max_damage.setter
    def max_damage(self, value: int) -> None:
        if not isinstance(value, int):
            raise TypeError(f"max_damage must be of type int, got: {type(value)}")

        if not 0 < value:
            raise ValueError(f"max_damage must be a non-zero positive integer, got : {value}")

        self._max_damage = value

    def __init__(self, max_damage: int) -> None:
        """
        Init a max damage component.

        Parameters
        ----------
        max_damage:
            The maximum amount of damage that this item can take. If not set, this item cannot take damage. Must be a non-zero positive integer.
        """

        super().__init__()

        self.max_damage = max_damage

    def to_value(self) -> int:
        return self.max_damage
