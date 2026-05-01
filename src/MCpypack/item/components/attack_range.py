# This file contains the attack_range component

from .components import ItemComponent

class AttackRange(ItemComponent):
    """
    Attack range item component.
    Determines the attack range and hitbox margin of a weapon.
    """

    TYPE = "minecraft:attack_range"

    @property
    def min_reach(self) -> float:
        return self._min_reach

    @min_reach.setter
    def min_reach(self, value: float) -> None:
        if not 0.0 <= value <= 64.0:
            raise ValueError(f"min_reach must be a float between 0.0 and 64.0, got: min_reach = {value}")

        self._min_reach = value

    @property
    def max_reach(self) -> float:
        return self._max_reach

    @max_reach.setter
    def max_reach(self, value: float) -> None:
        if not 0.0 <= value <= 64.0:
            raise ValueError(f"max_reach must be a float between 0.0 and 64.0, got: max_reach = {value}")

        self._max_reach = value

    @property
    def min_creative_reach(self) -> float:
        return self._min_creative_reach

    @min_creative_reach.setter
    def min_creative_reach(self, value: float) -> None:
        if not 0.0 <= value <= 64.0:
            raise ValueError(f"min_creative_reach must be a float between 0.0 and 64.0, got: min_creative_reach = {value}")

        self._min_creative_reach = value

    @property
    def max_creative_reach(self) -> float:
        return self._max_creative_reach

    @max_creative_reach.setter
    def max_creative_reach(self, value: float) -> None:
        if not 0.0 <= value <= 64.0:
            raise ValueError(f"max_creative_reach must be a float between 0.0 and 64.0, got: max_creative_reach = {value}")

        self._max_creative_reach = value

    @property
    def hitbox_margin(self) -> float:
        return self._hitbox_margin

    @hitbox_margin.setter
    def hitbox_margin(self, value) -> None:
        if not 0.0 <= value <= 1.0:
            raise ValueError(f"hitbox_margin must be a float between 0.0 and 1.0, got: hitbox_margin = {value}")

        self._hitbox_margin = value

    @property
    def mob_factor(self) -> float:
        return self._mob_factor

    @mob_factor.setter
    def mob_factor(self, value) -> None:
        if not 0.0 <= value <= 2.0:
            raise ValueError(f"mob_factor must be a float between 0.0 and 2.0, got: mob_factor = {value}")

        self._mob_factor = value

    def __init__(self,
                 min_reach: float = 0.0,
                 max_reach: float = 3.0,
                 min_creative_reach: float = 0.0,
                 max_creative_reach: float = 5.0,
                 hitbox_margin: float = 0.3,
                 mob_factor: float = 1.0,
                 ) -> None:
        """
        Init attach range component.

        Parameters
        ----------
        min_reach:
            The minimum distance in blocks from the attacker to the target to be considered valid. Defaults to 0.0, valid from 0.0 to 64.0.
        max_reach:
            The maximum distance in blocks from the attacker to the target to be considered valid. Defaults to 3.0, valid from 0.0 to 64.0.
        min_creative_reach:
            The minimum distance in blocks from the attacker to the target to be considered valid in Creative mode. Defaults to 0.0, valid from 0.0 to 64.0.
        max_creative_reach:
            The maximum distance in blocks from the attacker to the target to be considered valid in Creative mode. Defaults to 5.0, valid from 0.0 to 64.0.
        hitbox_margin:
            The margin applied to the target bounding box when checking for valid hitbox collision. Defaults to 0.3, valid from 0.0 to 1.0.
        mob_factor:
            The multiplier applied to min_range and max_range when checking for valid distance if item is used by a mob. Defaults to 1.0, valid from 0.0 to 2.0.
        """

        super().__init__()

        self.min_reach = min_reach
        self.max_reach = max_reach
        self.min_creative_reach = min_creative_reach
        self.max_creative_reach = max_creative_reach
        self.hitbox_margin = hitbox_margin
        self.mob_factor = mob_factor

    def to_value(self) -> dict:
        return {
            "min_reach": self.min_reach,
            "max_reach": self.max_reach,
            "min_creative_reach": self.min_creative_reach,
            "max_creative_reach": self.max_creative_reach,
            "hitbox_margin": self.hitbox_margin,
            "mob_factor": self.mob_factor,
        }
