# This file contains the CraftingSpecialShieldDecoration class

from packaging.version import Version

from MCpypack.item import ItemLike
from MCpypack.utils import CountedResult
from MCpypack.recipe.recipe import Recipe

class CraftingSpecialShieldDecoration(Recipe):
    """
    Special shield decoration crafting recipe.
    """

    @property
    def TYPE(self) -> str:
        return "minecraft:crafting_special_shielddecoration"

    def check_version(self, version: Version) -> bool:
        # This just returns True.
        # Later in development, when working for version-heavy checking this
        # will be implemented correctly.

        return True

    def __init__(self,
                 name: str,
                 target: ItemLike,
                 banner: ItemLike,
                 result: CountedResult,
                 ) -> None:
        """
        Init special shield decoration crafting recipe.

        Parameters
        ----------
        name:
            Name of the recipe.
        target:
            Base item.
            A shield would make sense, but can be anything.
        banner:
            Base item.
            If it is a banner the recipe will work and the nbt-data will be
            copied.
        result:
            Result of the crafting.
            Should be a shield, but can be anything.
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

        self.config["target"] = ingredient_to_config(target)
        self.config["banner"] = ingredient_to_config(banner)

        self.config["result"] = result.to_dict()

