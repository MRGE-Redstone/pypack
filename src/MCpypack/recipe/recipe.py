# This file contains the Recipe class used to create new recipes

from abc import ABC, abstractmethod
import json
from pathlib import Path
from typing import Any

class Recipe(ABC):
    """
    Recipe class for adding recipes.
    """

    @property
    @abstractmethod
    def TYPE(cls) -> str:
        """
        Return the type of the furnace recipe.
        """
        pass

    def __init__(self, name: str) -> None:
        """
        Set up 'self.config'.

        Parameters
        ----------
        name:
            Name of recipe.
        """

        self.name: str = name

        self.config: dict[str, Any] = {}

        self.config["type"] = self.TYPE

    def export(self, namespace_dir: Path):
        """
        Create recipe file inside namespace.

        Parameters
        ----------
        namespace_dir:
            Directory of the namespace.
        """

        # Recipe directory inside namespace
        recipe_dir: Path = namespace_dir / "recipe"
        recipe_dir.mkdir(parents=True, exist_ok=True)

        file_path: Path = recipe_dir / f"{self.name}.json"
        with open(file_path, "w", encoding="utf-8") as file:
            json.dump(self.config, file, indent=4)
