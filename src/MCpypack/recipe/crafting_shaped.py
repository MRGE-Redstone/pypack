from typing import Any

from .utils import Category, CategoryLike, Group, Result
from .recipe import Recipe

class CraftingShaped(Recipe):
    """
    Shaped crafting recipe.
    """

    def __init__(self,
                 name: str,
                 pattern: list[str],
                 key: dict[str, str],
                 result: Result,
                 group: Group = "",
                 category: CategoryLike = Category.MISC,
                 ) -> None:
        """
        Init shaped crafting recipe.

        Parameters
        ----------
        name:
            Name of the recipe.
        pattern:
            A list of single-character keys to describe a pattern for shaped
            crafting. Each row is one string. Spaces can be used to indicate an
            empty spot.
        key:
            All keys used for this shaped crafting recipe. Must contain all keys
            used in pattern.
        result:
            Result of the crafting stored as a Recipe instance.
        group:
            String identifier for grouping recipes.
        category:
            Recipe book category.
            Default is "misc".
        """
        super().__init__(name)

        # Collect all keys used
        pattern_keys: set[str] = {char for row in pattern for char in row if char != " "}
        used_keys: set[str] = set(key.keys())

        # Make sure every key in pattern is also in keys
        if pattern_keys != used_keys:
            raise ValueError(f"Pattern keys {pattern_keys} and used keys {used_keys} do not match.")

        # Convert category to Category enum if it is a string
        # Ensure valid value if string
        category_final: str = str(Category.from_str(category))

        # Create the config the way Minecraft expects it
        self.config: dict[str, Any] = {"type": "minecraft:crafting_shaped",
                             "category": category_final,
                             "group": group,
                             "key": key,
                             "pattern": pattern,
                             "result": {"count": result.count, "id" : result.item_id}}

