# This file contains recipe types for the smithing table
# 1) Smithing Transform

from .recipe import Recipe
from MCpypack.item import ItemLike
from .utils import SimpleResult

class SmithingTransform(Recipe):
    """
    Smithing transform recipe.
    """

    @property
    def TYPE(self) -> str:
        return "smithing_transform"

    def __init__(self,
                 name: str,
                 base: ItemLike,
                 result: SimpleResult,
                 addition: ItemLike | None = None,
                 template: ItemLike | None = None,
                 ) -> None:
        """
        Init smithing transform recipe.

        Parameters
        ----------
        name:
            Name of the recipe.
        base:
            Ingredient specifying an item to be upgraded.
        result:
            Item specifying the resulting upgraded item.
        addition:
            Optional.
            Ingredient specifying an item to be added.
        template:
            Optional.
            Ingredient specifying an item to act as the template.
        """

        super().__init__(name)

        if isinstance(base, list):
            self.config["base"] = [i.value for i in base]
        else:
            self.config["base"] = base.value

        self.config["result"] = result.to_dict()

        if addition is not None:
            if isinstance(addition, list):
                self.config["addition"] = [i.value for i in addition]
            else:
                self.config["addition"] = addition.value

        if template is not None:
            if isinstance(template, list):
                self.config["template"] = [i.value for i in template]
            else:
                self.config["template"] = template.value
