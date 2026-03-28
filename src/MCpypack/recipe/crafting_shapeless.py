from MCpypack.item import Item

from .utils import Category, CategoryLike, Group, CountedResult
from .recipe import Recipe

class CraftingShapeless(Recipe):
    """
    Shapeless crafting recipe.
    """

    @property
    def TYPE(cls) -> str:
        return "minecraft:crafting_shapeless"

    def __init__(self,
                 name: str,
                 ingredients: list[Item],
                 result: CountedResult,
                 group: Group | None = None,
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
            Optional.
            String identifier for grouping recipes.
        category:
            Recipe book category.
            Default is "misc".
        """
        super().__init__(name)

        # Convert category to Category enum if it is a string
        # Ensure valid value if string
        category_final: str = str(Category.from_str(category))
        
        ingredients_final: list[str] = list(map(lambda ingredient: ingredient.value, ingredients))

        self.config["category"] = category_final
        self.config["ingredients"] = ingredients_final
        self.config["result"] = result.to_dict()

        if group:
            self.config["group"] = group
