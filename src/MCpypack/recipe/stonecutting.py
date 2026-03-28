from MCpypack.item import Item

from .utils import CountedResult
from .recipe import Recipe

class Stonecutting(Recipe):
    """
    Stonecutting recipe.
    """

    @property
    def TYPE(cls) -> str:
        return "stonecutting"

    def __init__(self,
                 name: str,
                 ingredient: Item,
                 result: CountedResult,
                 ) -> None:
        """
        Init stonecutting recipe.

        Parameters
        ----------
        name:
            Name of the recipe.
        ingredient:
            Ingredient of the stonecutting.
        result:
            Result of the crafting stored as a Result instance.
        """
        super().__init__(name)

        self.config["ingredient"] = ingredient.value
        self.config["result"] = result.to_dict()

