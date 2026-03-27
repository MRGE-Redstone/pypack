# This file contains recipes for furnaces in Minecraft
# It support all 3 types of furnaces which are
# 1) Standard furnace -> Smelting recipes
# 2) Blast furnace    -> Blasting recipes
# 3) Smoker           -> Smoking recipes
# The 3 classes for each type inherit from the Furnace class

from MCpypack.item import Item
from .recipe import Recipe
from .utils import Time, Result, Group, CategoryLike, Category, Experience

from abc import ABC, abstractmethod

class Furnace(Recipe, ABC):
    """
    Base class for furnace recipes.
    """

    @property
    @abstractmethod
    def TYPE(cls) -> str:
        """
        Return the type of the furnace recipe.
        """
        pass

    def __init__(self,
                name: str,
                ingredient: Item,
                cookingtime: Time,
                result: Result,
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
        cookingtime:
            Cookingtime in real-life time values.
        result:
            Result of the smelting.
        category:
            Recipe book category of the recipe.
        group:
            String identifier for grouping recipes.
        experience:
            The output experience of the recipe.
        """

        super().__init__(name)

        # Convert category to Category enum if it is a string
        # Ensure valid value if string
        category_final: str = str(Category.from_str(category))

        self.config: dict[str, str | int | float | dict[str, str | int]] = {
            "type": self.TYPE,
            "category": category_final,
            "cookingtime": cookingtime.ticks.value,
            "ingredient": ingredient.value,
            "result": result.to_dict(),
        }

        if group:
            self.config["group"] = group

        if experience:
            self.config["experience"] = experience

class Smelting(Furnace):
    """
    Smelting recipe.
    """

    @property
    def TYPE(cls) -> str:
        return "minecraft:smelting"

class Blasting(Furnace):
    """
    Blasting recipe.
    """

    @property
    def TYPE(cls) -> str:
        return "minecraft:blasting"

class Smoking(Furnace):
    """
    Smoking recipe.
    """

    @property
    def TYPE(cls) -> str:
        return "minecraft:smoking"
