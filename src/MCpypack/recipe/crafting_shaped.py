from typing import Any, Dict, List, Set
from .recipe import Recipe

class Crafting_Shaped(Recipe):
    """
    Shaped crafting recipe.
    """

    def __init__(self,
                 name: str,
                 pattern: List[str],
                 key: Dict[str, str],
                 result_id: str,
                 result_count: int,
                 group: str = "",
                 category: str = "misc",
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

        # Collect all keys used
        pattern_keys: Set[str] = {char for row in pattern for char in row if char != " "}
        used_keys: Set[str] = set(key.keys())

        # Make sure every key in pattern is also in keys
        if pattern_keys != used_keys:
            raise ValueError(f"Pattern keys {pattern_keys} and used keys {used_keys} do not match.")

        # Create the config the way Minecraft expects it
        self.config: Dict[str, Any] = {"type": "minecraft:crafting_shaped",
                             "category": category,
                             "group": group,
                             "key": key,
                             "pattern": pattern,
                             "result": {"count": result_count, "id" : result_id}}

