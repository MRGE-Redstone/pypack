# This file contains the Recipe class used to create new recipes

from abc import ABC, abstractmethod
import json
from pathlib import Path
from typing import Any

from packaging.version import Version

from MCpypack.core.valid import RECIPE_PATTERN

class Recipe(ABC):
    """
    Recipe class for adding recipes.
    """

    @property
    @abstractmethod
    def TYPE(self) -> str:
        """
        Return the type of the furnace recipe.
        """
        pass

    @abstractmethod
    def check_version(self, version: Version) -> bool:
        """
        Return if recipe type exists for specified version.
        """

    def __init__(self, name: str) -> None:
        """
        Set up 'self.config'.

        Parameters
        ----------
        name:
            Name of recipe.
        """

        # Validate name
        if not RECIPE_PATTERN.match(name):
            raise ValueError(f"Invalid recipe name: '{name}'")

        self.name: str = name

        self.config: dict[str, Any] = {}

        self.config["type"] = self.TYPE

    def export(self, namespace_dir: Path, version: Version) -> None:
        """
        Create recipe file inside namespace.

        Parameters
        ----------
        namespace_dir:
            Directory of the namespace.
        """

        if not self.check_version(version):
            return

        # Recipe directory inside namespace
        recipe_dir: Path = namespace_dir / "recipe"
        recipe_dir.mkdir(parents=True, exist_ok=True)

        file_path: Path = recipe_dir / f"{self.name}.json"
        with open(file_path, "w", encoding="utf-8") as file:
            json.dump(self.config, file, indent=4)
