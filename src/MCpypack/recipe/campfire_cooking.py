# This file contains the CampfireCooking class

from MCpypack.item import Item
from .utils import Result, Time, Experience
from .recipe import Recipe

class CampfireCooking(Recipe):
    """
    Campfire cooking recipe.
    """

    def __init__(self,
                 name: str,
                 ingredient: Item,
                 cookingtime: Time,
                 result: Result,
                 experience: Experience | None = None,
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

        self.config: dict[str, int | str | dict | float] = {
            "type": "minecraft:campfire_cooking",
            "cookingtime": cookingtime.ticks.value,
            "ingredient": ingredient.value,
            "result": result.to_dict()
        }

        if experience:
            self.config["experience"] = experience
