# This file contains the use_effects component

from .components import ItemComponent

class UseEffects(ItemComponent):
    """
    Use effects item component.
    """

    @property
    def TYPE(self) -> str:
        return "minecraft:use_effects"

    @property
    def speed_multiplier(self) -> float:
        return self._speed_multiplier

    @speed_multiplier.setter
    def speed_multiplier(self, value: float) -> None:
        if not (0.0 <= value <= 1.0):
            raise ValueError(f"speed_multiplier must be a float between 0.0 and 1.0, got: speed_multiplier = {value}")

        self._speed_multiplier = value

    def __init__(self,
                 can_sprint: bool = False,
                 speed_multiplier: float = 0.2,
                 interact_vibrations: bool = True,
                 ) -> None:
        """
        Init an use effects item component.

        Parameters
        ----------
        can_sprint:
            If the player can sprint during use. Defaults to false.
        speed_multiplier:
            A ranged float (0.0-1.0 inclusive) speed multiplier inflicted during use. Defaults to 0.2.
        interact_vibrations:
            Whether using this item emits the minecraft:item_interact_start and minecraft:item_interact_finish game events. Defaults to true.
        """

        super().__init__()

        self.can_sprint = can_sprint
        self.speed_multiplier = speed_multiplier
        self.interact_vibrations = interact_vibrations

    def to_value(self) -> dict:
        return {
            "can_sprint": self.can_sprint,
            "speed_multiplier": self.speed_multiplier,
            "interact_vibrations": self.interact_vibrations,
        }
