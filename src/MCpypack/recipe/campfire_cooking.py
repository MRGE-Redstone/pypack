# This file contains the CampfireCooking class

from packaging.version import Version

from MCpypack.item import ItemLike
from MCpypack.utils import Time, Experience, ItemStack
from .recipe import Recipe

class CampfireCooking(Recipe):
    """
    Campfire cooking recipe.
    """

    @property
    def TYPE(self) -> str:
        return "minecraft:campfire_cooking"

    def check_version(self, version: Version) -> bool:
        # This just returns True.
        # Later in development, when working for version-heavy checking this
        # will be implemented correctly.

        return True

    def __init__(self,
                 name: str,
                 ingredient: ItemLike,
                 result: ItemStack,
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

        if isinstance(ingredient, list):
            self.config["ingredient"] = [i.value for i in ingredient]
        else:
            self.config["ingredient"] = ingredient.value

        self.config["result"] = result.to_dict()

        if experience:
            self.config["experience"] = experience

        if cookingtime:
            self.config["cookingtime"] = cookingtime.ticks.value
