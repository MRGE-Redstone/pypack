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

from abc import ABC, abstractmethod

class Furnace(Recipe, ABC):
    """
    Base class for furnace recipes.
    """

    @property
    @abstractmethod
    def TYPE(self) -> str:
        """
        Return the type of the furnace recipe.
        """
        pass

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

    @property
    def TYPE(self) -> str:
        return "minecraft:smelting"

class Blasting(Furnace):
    """
    Blasting recipe.
    """

    @property
    def TYPE(self) -> str:
        return "minecraft:blasting"

class Smoking(Furnace):
    """
    Smoking recipe.
    """

    @property
    def TYPE(self) -> str:
        return "minecraft:smoking"
