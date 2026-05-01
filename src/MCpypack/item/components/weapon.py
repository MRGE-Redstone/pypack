# This file contains the weapon component

from .components import ItemComponent

class Weapon(ItemComponent):
    """
    Weapon item component.
    If present, the item acts as a weapon.
    """

    TYPE = "minecraft:weapon"

    @property
    def item_damage_per_attack(self) -> int:
        return self._item_damage_per_attack

    @item_damage_per_attack.setter
    def item_damage_per_attack(self, value: int) -> None:

        if not isinstance(value, int):
            raise TypeError(f"item_damage_per_attack must be of type int, got: {type(value)}")

        if not 0 <= value:
            raise ValueError(f"item_damage_per_attack must be a positive integer, got : item_damage_per_attack = {value}")

        self._item_damage_per_attack = value

    @property
    def disable_blocking_for_seconds(self) -> float:
        return self._disable_blocking_for_seconds

    @disable_blocking_for_seconds.setter
    def disable_blocking_for_seconds(self, value: float) -> None:

        if not isinstance(value, float):
            raise TypeError(f"disable_blocking_for_seconds must be of type float, got: {type(value)}")

        if not 0 <= value:
            raise ValueError(f"disable_blocking_for_seconds must be a positive float, got : disable_blocking_for_seconds = {value}")

        self._disable_blocking_for_seconds = value

    def __init__(self,
                 item_damage_per_attack: int = 1,
                 disable_blocking_for_seconds: float = 0.0,
                 ) -> None:
        """
        Init weapon component.

        Parameters
        ----------
        item_damage_per_attack:
            The amount to damage the item for each attack performed. Defaults to 1.
        disable_blocking_for_seconds:
            The amount of seconds that this item can disable a blocking shield on successful attack. If set to 0, this item cannot disable a blocking shield. Defaults to 0.
        """
        
        super().__init__()

        self.item_damage_per_attack = item_damage_per_attack
        self.disable_blocking_for_seconds = disable_blocking_for_seconds

    def to_value(self) -> dict:
        return {
            "item_damage_per_attack": self.item_damage_per_attack,
            "disable_blocking_for_seconds": self.disable_blocking_for_seconds,
        }

