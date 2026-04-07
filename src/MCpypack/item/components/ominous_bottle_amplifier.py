# This file contains the ominous_bottle_amplifier component

from .components import ItemComponent

class OminousBottleAmplifier(ItemComponent):
    """
    Ominous bottle amplifier item component.
    """

    @property
    def TYPE(self) -> str:
        return "minecraft:ominous_bottle_amplifier"

    @property
    def ominous_bottle_amplifier(self) -> int:
        return self._ominous_bottle_amplifier

    @ominous_bottle_amplifier.setter
    def ominous_bottle_amplifier(self, value: int) -> None:
        if not 0 <= value <= 4:
            raise ValueError(f"ominous_bottle_amplifier must be an integer between 0 and 4, got: ominous_bottle_amplifier = {value}")

        self._ominous_bottle_amplifier = value

    def __init__(self, ominous_bottle_amplifier: int) -> None:
        """
        Init ominous_bottle_amplifier component.
        
        Parameters
        ----------
        ominous_bottle_amplifier:
            The amplifier of the Bad Omen effect given to the player or mob upon consuming this item (normally an ominous bottle). Must be a non-negative integer from 0 to 4 (inclusive).
        """

        super().__init__()

        self.ominous_bottle_amplifier = ominous_bottle_amplifier

    def to_value(self) -> int:
        return self.ominous_bottle_amplifier


