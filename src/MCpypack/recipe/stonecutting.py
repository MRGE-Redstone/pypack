from packaging.version import Version

from MCpypack.item import ItemLike

from MCpypack.utils import ItemStack
from .recipe import Recipe

class Stonecutting(Recipe):
    """
    Stonecutting recipe.
    """

    TYPE = "minecraft:stonecutting"

    def check_version(self, version: Version) -> bool:
        # This just returns True.
        # Later in development, when working for version-heavy checking this
        # will be implemented correctly.

        return True

    def __init__(self,
                 name: str,
                 ingredient: ItemLike,
                 result: ItemStack,
                 ) -> None:
        """
        Init stonecutting recipe.

        Parameters
        ----------
        name:
            Name of the recipe.
        ingredient:
            Ingredient of the stonecutting.
        result:
            Result of the crafting stored as a Result instance.
        """
        super().__init__(name)

        if isinstance(ingredient, list):
            self.config["ingredient"] = [i.value for i in ingredient]
        else:
            self.config["ingredient"] = ingredient.value

        self.config["result"] = result.to_dict()

