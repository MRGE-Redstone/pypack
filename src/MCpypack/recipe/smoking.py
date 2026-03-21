# This file contains the Smoking class
# It represents a smoking recipe

from typing import Any
from .utils import CategoryLike, Group, Result, Time, Category
from .recipe import Recipe


class Smoking(Recipe):
    """
    Smoking recipe.
    """

    def __init__(self,
                 name: str,
                 ingredient: str,
                 cookingtime: Time,
                 result: Result,
                 group: Group = '',
                 category: CategoryLike = Category.MISC,
                 ) -> None:
        """
        Init new smoking recipe.

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
        """

        super().__init__(name)

        # Convert category to Category enum if it is a string
        # Ensure valid value if string
        category_final: str = str(Category.from_str(category))

        self.config: dict[str, Any] = {
            "type": "minecraft:smoking",
            "category": category_final,
            "group": group,
            "cookingtime": cookingtime.ticks.value,
            "ingredient": ingredient,
            "result": result.to_dict()

        }

