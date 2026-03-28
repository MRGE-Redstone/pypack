from MCpypack.item import Item
from .utils import Category, CategoryLike, Group, CountedResult
from .recipe import Recipe

class CraftingShaped(Recipe):
    """
    Shaped crafting recipe.
    """

    @property
    def TYPE(self) -> str:
        return "minecraft:crafting_shaped"

    def __init__(self,
                 name: str,
                 pattern: list[str],
                 key: dict[str, Item] | dict[str, list[Item]] | dict[str, list[Item] | Item],
                 result: CountedResult,
                 group: Group | None = None,
                 category: CategoryLike = Category.MISC) -> None:

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
