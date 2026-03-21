# This file contains the CampfireCooking class

from typing import Any
from .utils import Result, Time
from .recipe import Recipe

class CampfireCooking(Recipe):
    """
    Campfire cooking recipe.
    """

    def __init__(self,
                 name: str,
                 ingredient: str,
                 cookingtime: Time,
                 result: Result,
                 ) -> None:
        """
        Init campfire cooking recipe.

        Parameters
        ----------
        name:
            Name of the recipe.
        ingredient:
            Ingredient of the recipe.
        cookingtime:
            Cookingtime in real-life time values.
        result:
            Result of the cooking.
        """

        super().__init__(name)

        self.config: dict[str, Any] = {
            "type": "minecraft:campfire_cooking",
            "cookingtime": cookingtime.ticks.value,
            "ingredient": ingredient,
            "result": result.to_dict()
        }
