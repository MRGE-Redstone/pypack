from packaging.version import Version

from MCpypack.item import ItemLike, Item, Tag

from .utils import Category, CategoryLike, Group, CountedResult
from .recipe import Recipe

class CraftingShapeless(Recipe):
    """
    Shapeless crafting recipe.
    """

    @property
    def TYPE(self) -> str:
        return "minecraft:crafting_shapeless"

    def check_version(self, version: Version) -> bool:
        # This just returns True.
        # Later in development, when working for version-heavy checking this
        # will be implemented correctly.

        return True

    def __init__(self,
                 name: str,
                 ingredients: ItemLike | list[ItemLike],
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
        

        # Convert ingredients into useful list
        ingredients_final: list[str] | list[list[str]] | list[list[str] | str]

        if isinstance(ingredients, Item | Tag.ITEM):
            # Plain item and not a list of ingredients
            # -> Just convert it into a list with just the one value
            ingredients_final = [ingredients.value]

        elif isinstance(ingredients, list):
            # Ingredients is not just one value but rather a list
            # The list may contains just items or lists of items

            ingredients_final = []

            for ingredient in ingredients:
                if isinstance(ingredient, Item | Tag.ITEM):
                    # If it is just an item append it to the list
                    ingredients_final.append(ingredient.value)

                elif isinstance(ingredient, list):
                    # If it is another list of type list[Item]
                    # -> Put each element into a list and then append it to the
                    #    final list
                    inner: list[str] = []
                    for sub in ingredient:
                        if isinstance(sub, Item | Tag.ITEM):
                            inner.append(sub.value)
                    ingredients_final.append(inner)

        self.config["category"] = category_final
        self.config["ingredients"] = ingredients_final
        self.config["result"] = result.to_dict()

        if group:
            self.config["group"] = group
