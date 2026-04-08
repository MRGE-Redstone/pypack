# This file contains the minimum_attack_charge component

from .components import ItemComponent

class MinimumAttackCharge(ItemComponent):
    """
    Minimum attack charge item component.
    """

    @property
    def TYPE(self) -> str:
        return "minecraft:minimum_attack_charge"

    @property
    def minimum_attack_charge(self) -> float:
        return self._minimum_attack_charge

    @minimum_attack_charge.setter
    def minimum_attack_charge(self, value: float) -> None:
        if not 0.0 <= value <= 1.0:
            raise ValueError(f"minimum_attack_charge must be a non-negative float between 0.0 and 1.0, got : minimum_attack_charge = {value}")

        self._minimum_attack_charge = value

    def __init__(self, minimum_attack_charge: float) -> None:
        """
        Init a max damage component.

        Parameters
        ----------
        minimum_attack_charge:
            Sets the minimum attack charge on the attack indicator required to attack with this item. Must be a non-negative float between 0.0 and 1.0
        """

        super().__init__()

        self.minimum_attack_charge = minimum_attack_charge

    def to_value(self) -> float:
        return self.minimum_attack_charge


