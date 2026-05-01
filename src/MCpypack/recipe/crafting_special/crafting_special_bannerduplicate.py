# This file contains the CraftingSpecialBannerDuplicate class

from packaging.version import Version

from MCpypack.item import ItemLike
from MCpypack.utils import ItemStack
from MCpypack.recipe.recipe import Recipe

class CraftingSpecialBannerDuplicate(Recipe):
    """
    Special banner duplicate crafting recipe.
    """

    TYPE = "minecraft:crafting_special_bannerduplicate"

    def check_version(self, version: Version) -> bool:
        # This just returns True.
        # Later in development, when working for version-heavy checking this
        # will be implemented correctly.

        return True

    def __init__(self,
                 name: str,
                 banner: ItemLike,
                 result: ItemStack,
                 ) -> None:
        """
        Init special banner duplicate crafting recipe.

        Parameters
        ----------
        name:
            Name of the recipe.
        banner:
            Base banner with color and pattern.
        result:
            Result of the crafting.
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

        self.config["banner"] = ingredient_to_config(banner)

        self.config["result"] = result.to_dict()
