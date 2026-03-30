# This file contains the Namespace class

from pathlib import Path

from MCpypack.core import NAMESPACE_PATTERN
from MCpypack.recipe.recipe import Recipe

class Namespace:
    """
    Represents a namespace.
    """

    def __init__(self,
                 name: str,
                ) -> None:
        """
        Initialize namespace instance.

        Parameters
        ----------
        name:
            Name of the namespace.
        """

        # Validate name
        if not NAMESPACE_PATTERN.match(name):
            raise ValueError(f"Invalid namespace name: '{name}'")

        self.name: str = name

        self.recipes: list[Recipe] = []

    def add_recipes(self, *recipes: Recipe) -> None:
        """
        Add recipes to namespace.

        Parameters
        ----------
        *recipes:
            Recipes to add.
        """

        # Ensure recipes do not share the same name
        existing_names: list[str] = [recipe.name for recipe in self.recipes]

        for recipe in recipes:
            if recipe.name in existing_names:
                raise ValueError(f"Recipe with name {recipe.name} already exists in namespace {self.name}")
            existing_names.append(recipe.name)
            self.recipes.append(recipe)

    def export(self, datapack_dir: Path) -> None:
        """
        Create namespace related content.

        Parameters
        ----------
        datapack_dir:
            Directory of the datapack in which the namespace will be created.
        """

        namespace_dir: Path = datapack_dir / "data" / self.name
        namespace_dir.mkdir(parents=True, exist_ok=True)

        # Handle recipes
        if self.recipes:
            for recipe in self.recipes:
                recipe.export(namespace_dir=namespace_dir)
