# This file contains the CratfingTransmute class

from packaging.version import Version

from MCpypack.item import ItemLike
from MCpypack.recipe.utils.result import SimpleResult
from .utils import Category, CategoryLike, Group
from .recipe import Recipe


class CratfingTransmute(Recipe):
    """
    Transmute crafting recipe.
    Represents a crafting recipe in a crafting table, a crafter and the survival inventory.
    When matched, output copies the input item stack, changing the item type but
    preserving all stack components.
    """

    @property
    def TYPE(self) -> str:
        return "crafting_transmute"

    def check_version(self, version: Version) -> bool:
        # This just returns True.
        # Later in development, when working for version-heavy checking this
        # will be implemented correctly.

        return True

    def __init__(self,
                 name: str,
                 input: ItemLike,
                 material: ItemLike,
                 result: SimpleResult,
                 group: Group | None = None,
                 category: CategoryLike = Category.MISC,
                 ) -> None:
        """
        Init transmute crating recipe.

        Parameters
        ----------
        name:
            Name of the recipe.
        input:
            Ingredient for item to copy.
        material:
            Additional ingredient to use.
        result:
            The output item of the recipe.
            It keeps item components from the input.
        group:
            Optional.
            Used to group multiple recipes together in the recipe book.
        category:
            Optional.
            Controls to which recipe book category the recipe belongs to.
            Available values are: equipment, building, misc, and redstone.
            Defaults to misc.
        """

        super().__init__(name)

        if isinstance(input, list):
            self.config["input"] = [i.value for i in input]
        else:
            self.config["input"] = input.value

        if isinstance(material, list):
            self.config["material"] = [i.value for i in material]
        else:
            self.config["material"] = material.value

        self.config["result"] = result.to_dict()

        if group:
            self.config["group"] = group
        self.config["category"] = category
