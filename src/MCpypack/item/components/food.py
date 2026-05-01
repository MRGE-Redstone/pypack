# This file contains the food component

from .components import ItemComponent

class Food(ItemComponent):
    """
    Food item component.
    The food stats applied to the mob or player upon consuming this item.
    """

    TYPE = "minecraft:food"

    @property
    def nutrition(self) -> int:
        return self._nutrition

    @nutrition.setter
    def nutrition(self, value: int) -> None:
        if not 0 <= value:
            raise ValueError(f"nutrition must be a non-negative integer, got: nutrition = {value}")

        self._nutrition = value

    @property
    def saturation(self) -> float:
        return self._saturation

    @saturation.setter
    def saturation(self, value: float) -> None:
        if not 0 <= value:
            raise ValueError(f"saturation must be a non-negative float, got: saturation = {value}")

        self._saturation = value

    def __init__(self,
                 nutrition: int,
                 saturation: float,
                 can_always_eat: bool = False,
                 ) -> None:
        """
        Init food item component.

        Parameters
        ----------
        nutrition:
            The number of food points restored by this item when the player eats. The number of health points restored by this item when used to feed cats. Wolfs, nautilus and zombie nautilus restored the twice the value. Must be a non-negative integer.
        saturation:
            The amount of saturation restored by this item when eaten.
        can_always_eat:
            True -> Player can it it when not hungry.
            False -> Player can not it it when not hungry.
            Defaults to False.
        """

        super().__init__()

        self.nutrition = nutrition
        self.saturation = saturation
        self.can_always_eat = can_always_eat

    def to_value(self) -> dict:
        return {
            "nutrition": self.nutrition,
        "saturation": self.saturation,
            "can_always_eat": self.can_always_eat,
        }
