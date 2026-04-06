# This file contains recipe types for the smithing table
# 1) Smithing Transform
# 2) Smithing Trim

from packaging.version import Version

from .recipe import Recipe
from MCpypack.item import ItemLike, TrimPattern
from .utils import SimpleResult

class SmithingTransform(Recipe):
    """
    Smithing transform recipe.
    """

    @property
    def TYPE(self) -> str:
        return "minecraft:smithing_transform"

    def check_version(self, version: Version) -> bool:
        # This just returns True.
        # Later in development, when working for version-heavy checking this
        # will be implemented correctly.

        return True

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

class SmithingTrim(Recipe):
    """
    Smithing trim recipe for the smithing table.
    """

    @property
    def TYPE(self) -> str:
        return "minecraft:smithing_trim"

    def check_version(self, version: Version) -> bool:
        # This just returns True.
        # Later in development, when working for version-heavy checking this
        # will be implemented correctly.

        return True

    def __init__(self,
                 name: str,
                 base: ItemLike,
                 template: ItemLike,
                 addition: ItemLike,
                 pattern: TrimPattern,
                 ) -> None:
        """
        Init smithing trim recipe.

        Parameters
        ----------
        name:
            Name of the recipe.
        base:
            Ingredient which should get the pattern.
        template:
            Smithing template which is needed.
        addition:
            Ingredient specifying an item to be added.
        pattern:
            Pattern to be applied.
            Values can be found in TrimPattern enum.
        """

        super().__init__(name)

        def ingredient_to_config(ingredient: ItemLike) -> str | list[str]:
            """
            Convert ItemLike into str or list[str] for the config.
            """

            if isinstance(ingredient, list):
                return [i.value for i in ingredient]
            else:
                return ingredient.value

        self.config["base"] = ingredient_to_config(base)
        self.config["template"] = ingredient_to_config(template)
        self.config["addition"] = ingredient_to_config(addition)

        self.config["pattern"] = pattern.value

