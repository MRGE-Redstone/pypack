# This file contains the CraftingDecoratedPot class

from packaging.version import Version

from MCpypack.item import ItemLike
from MCpypack.utils import ItemStack
from .recipe import Recipe

class CraftingDecoratedPot(Recipe):
    """
    Decorated pot crafting recipe.
    """

    @property
    def TYPE(self) -> str:
        return "minecraft:crafting_decorated_pot"

    def check_version(self, version: Version) -> bool:

        if version < Version("26.1"):
            raise ValueError(f"This recipe ({self.TYPE}) wasn't implemented until Verison 26.1")

        return True

    def __init__(self,
                 name: str,
                 left: ItemLike,
                 right: ItemLike,
                 front: ItemLike,
                 back: ItemLike,
                 result: ItemStack,
                 ) -> None:
        """
        Init decorated pot crafting recipe.

        Parameters
        ----------
        name:
            Name of the recipe.
        left:
            Ingredient for the left slot.
        right:
            Ingredient for the right slot.
        back:
            Ingredient for the back slot.
        front:
            Ingredient for the front slot.
        result:
            Result of the cooking.
            Can contain a count.
        """

        super().__init__(name)

        def ingredient_to_config(ingredient: ItemLike) -> str | list[str]:
            """
            Convert ItemLike into str or list[str] for the config.
            """

            if isinstance(ingredient, list):
                return [i.value for i in ingredient]
            else:
                return ingredient.value

        self.config["left"] = ingredient_to_config(left)
        self.config["right"] = ingredient_to_config(right)
        self.config["back"] = ingredient_to_config(back)
        self.config["front"] = ingredient_to_config(front)

        self.config["result"] = result.to_dict()
