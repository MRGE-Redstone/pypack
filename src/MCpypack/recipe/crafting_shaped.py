from MCpypack.item import Item

from .utils import Category, CategoryLike, Group, CountedResult
from .recipe import Recipe

class CraftingShaped(Recipe):
    """
    Shaped crafting recipe.
    """

    @property
    def TYPE(cls) -> str:
        return "minecraft:crafting_shaped"

    def __init__(self,
                 name: str,
                 pattern: list[str],
                 key: dict[str, Item],
                 result: CountedResult,
                 group: Group | None = None,
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
            Optional.
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

        # dict[str, Item] to dict[str, str]
        key_final: dict[str, str] = {
            k: v.value for k, v in key.items()
        }

        self.config["category"] = category_final
        self.config["key"] = key_final
        self.config["pattern"] = pattern
        self.config["result"] = result.to_dict()

        if group:
            self.config["group"] = "group"

