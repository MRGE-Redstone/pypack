from typing import Any, Dict, List
from .recipe import Recipe

class Crafting_Shapeless(Recipe):
    """
    Shapeless crafting recipe.
    """

    def __init__(self,
                 name: str,
                 ingredients: List[str],
                 result_id: str,
                 result_count: int,
                 group: str = "",
                 category: str = "misc",
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
        """
        super().__init__(name)

        self.config: Dict[str, Any] = {"type": "minecraft:crafting_shapeless",
                             "category" : category,
                             "group" : group,
                             "ingredients" : ingredients,
                             "result" : {"count": result_count, "id" : result_id}}
