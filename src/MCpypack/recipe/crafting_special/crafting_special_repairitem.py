# This file contains the CraftingSpecialBannerDuplicate class

from packaging.version import Version

from MCpypack.recipe.recipe import Recipe

class CraftingSpecialRepairItem(Recipe):
    """
    Special repair item crafting recipe.
    """

    TYPE = "minecraft:crafting_special_repairitem"

    def check_version(self, version: Version) -> bool:
        # This just returns True.
        # Later in development, when working for version-heavy checking this
        # will be implemented correctly.

        return True

    def __init__(self,
                 name: str,
                 ) -> None:
        """
        Init special repair item crafting recipe.

        Parameters
        ----------
        name:
            Name of the recipe.
        """

        super().__init__(name)
