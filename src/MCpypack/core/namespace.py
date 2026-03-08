# This file contains the Namespace class

from pathlib import Path
from typing import Dict


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
        self.name: str = name

    def export(self, datapack_dir: Path) -> None:
        """
        Create namespace related content.

        Parameters
        ----------
        datapack_dir:
            Directory of the datapack in which the namespace will be created.
        """

        namespace_dir: Path = datapack_dir / "data" / self.name
        namespace_dir.mkdir(parents=True, exist_ok=False)
