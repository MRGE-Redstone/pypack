from typing import Any

from .utils import Category, CategoryLike, Group, Result
from .recipe import Recipe

class CraftingShapeless(Recipe):
    """
    Shapeless crafting recipe.
    """

    def __init__(self,
                 name: str,
                 ingredients: list[str],
                 result: Result,
                 group: Group = "",
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
        result:
            Result of the crafting stored as a Result instance.
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
                             "result" : {"count": result.count, "id" : result.item_id}}
