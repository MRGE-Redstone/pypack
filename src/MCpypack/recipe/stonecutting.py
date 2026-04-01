from MCpypack.item import ItemLike

from .utils import CountedResult
from .recipe import Recipe

class Stonecutting(Recipe):
    """
    Stonecutting recipe.
    """

    @property
    def TYPE(self) -> str:
        return "stonecutting"

    def __init__(self,
                 name: str,
                 ingredient: ItemLike,
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

        if isinstance(ingredient, list):
            self.config["ingredient"] = [i.value for i in ingredient]
        else:
            self.config["ingredient"] = ingredient.value

        self.config["result"] = result.to_dict()

