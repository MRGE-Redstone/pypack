from packaging.version import Version

from MCpypack.item import ItemLike
from .utils import Category, CategoryLike, Group, CountedResult
from .recipe import Recipe

class CraftingShaped(Recipe):
    """
    Shaped crafting recipe.
    """

    @property
    def TYPE(self) -> str:
        return "minecraft:crafting_shaped"

    def check_version(self, version: Version) -> bool:
        # This just returns True.
        # Later in development, when working for version-heavy checking this
        # will be implemented correctly.

        return True

    def __init__(self,
                 name: str,
                 pattern: list[str],
                 key: dict[str, ItemLike],
                 result: CountedResult,
                 group: Group | None = None,
                 category: CategoryLike = Category.MISC,
                 show_notification: bool | None = None,
                 ) -> None:
        """
        Init shaped crafting recipe.

        Parameters
        ----------
        name:
            Name of the recipe.
        pattern:
            Pattern representing a crafting grid.
            Can be 1*1, 2*2, or 3*3.
        key:
            All keys used for this shaped crafting recipe.
        result:
            Result of the shaped crafting with id and count.
        group:
            Optional.
            Used to group multiple recipes together in the recipe book.
        category:
            Recipe book category.
            Default is "misc".
        show_notification:
            Optional.
            Determines if a notification is shown when unlocking the recipe.
        """

        super().__init__(name)

        # Validate keys
        pattern_keys = {char for row in pattern for char in row if char != " "}
        used_keys = set(key.keys())
        if pattern_keys != used_keys:
            raise ValueError(f"Pattern keys {pattern_keys} and used keys {used_keys} do not match.")

        # Convert category
        category_final = str(Category.from_str(category))

        # Convert key values inline: single Item -> str, list[Item] -> list[str]
        key_final: dict[str, str | list[str]] = {}
        for k, v in key.items():
            if isinstance(v, list):
                key_final[k] = [i.value for i in v]
            else:
                key_final[k] = v.value

        # Assign config
        self.config["category"] = category_final
        self.config["key"] = key_final
        self.config["pattern"] = pattern
        self.config["result"] = result.to_dict()
        if group:
            self.config["group"] = group
        if show_notification is not None:
            self.config["show_notification"] = show_notification
