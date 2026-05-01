# This file contains recipes for furnaces in Minecraft.
# It support all 3 types of furnaces which are:
# 1) Standard furnace -> Smelting recipes
# 2) Blast furnace    -> Blasting recipes
# 3) Smoker           -> Smoking recipes
# The 3 classes for each type inherit from the Furnace class.
# All of them have to implement the TYPE property.

from packaging.version import Version

from MCpypack.item import ItemLike
from .recipe import Recipe
from MCpypack.utils import Time, Group, CategoryLike, Category, Experience, ItemStack

from abc import ABC

class Furnace(Recipe, ABC):
    """
    Base class for furnace recipes.
    """

    # !ToDO
    # Add another class attribute that does not require
    # declaring for the ABC Furnace class.
    TYPE = ""

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
                group: Group | None = None,
                category: CategoryLike = Category.MISC,
                experience: Experience | None = None,

                ) -> None:
        """
        Init new furnace recipe.

        Parameters
        ----------
        name:
            Name of the smelting recipe.
        ingredient:
            Ingredient of the recipe.
        result:
            Result of the smelting.
        cookingtime:
            Optional.
            Cookingtime in real-life time values.
        category:
            Recipe book category of the recipe.
        group:
            String identifier for grouping recipes.
        experience:
            Optional. The output experience of the recipe.
        """

        super().__init__(name)

        # Convert category to Category enum if it is a string
        # Ensure valid value if string
        category_final: str = str(Category.from_str(category))

        self.config["category"] = category_final

        if isinstance(ingredient, list):
            self.config["ingredient"] = [i.value for i in ingredient]
        else:
            self.config["ingredient"] = ingredient.value

        self.config["result"] = result.to_dict()

        if group:
            self.config["group"] = group

        if experience:
            self.config["experience"] = experience

        if cookingtime:
            self.config["cookingtime"] = cookingtime.ticks.value

class Smelting(Furnace):
    """
    Smelting recipe.
    """

    TYPE = "minecraft:smelting"

class Blasting(Furnace):
    """
    Blasting recipe.
    """

    TYPE = "minecraft:blasting"

class Smoking(Furnace):
    """
    Smoking recipe.
    """

    TYPE = "minecraft:smoking"
