from typing import Any

from .category import Category, CategoryLike
from .recipe import Recipe

class CraftingShapeless(Recipe):
    """
    Shapeless crafting recipe.
    """

    def __init__(self,
                 name: str,
                 ingredients: list[str],
                 result_id: str,
                 result_count: int,
                 group: str = "",
                 category: CategoryLike = Category.MISC,
                 ) -> None:
        """
        Init shapeless crafting recipe.

        Parameters
        ----------
        name:
            Name of the recipe.
        ingredients:
            List of ingredients for the recipe.
        result_id:
            Result of the crafting.
        result_count:
            Amount of result.
        group:
            String identifier for grouping recipes.
        category:
            Recipe book category.
            Default is "misc".
        """
        super().__init__(name)

        # Convert category to Category enum if it is a string
        # Ensure valid value if string
        category_final: str = str(Category.from_str(category))

        self.config: dict[str, Any] = {"type": "minecraft:crafting_shapeless",
                             "category" : category_final,
                             "group" : group,
                             "ingredients" : ingredients,
                             "result" : {"count": result_count, "id" : result_id}}
