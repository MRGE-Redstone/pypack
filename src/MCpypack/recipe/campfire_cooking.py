# This file contains the CampfireCooking class

from MCpypack.item import Item
from .utils import SimpleResult, Time, Experience
from .recipe import Recipe

class CampfireCooking(Recipe):
    """
    Campfire cooking recipe.
    """

    def __init__(self,
                 name: str,
                 ingredient: Item,
                 result: SimpleResult,
                 cookingtime: Time | None = None,
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
        result:
            Result of the cooking.
        cookingtime:
            Optional. Cookingtime in real-life time values.
        experience:
            Optional. The output experience of the recipe.
        """

        super().__init__(name)

        self.config: dict[str, int | str | dict | float] = {
            "type": "minecraft:campfire_cooking",
            "ingredient": ingredient.value,
            "result": result.to_dict()
        }

        if experience:
            self.config["experience"] = experience

        if cookingtime:
            self.config["cookingtime"] = cookingtime.ticks.value
