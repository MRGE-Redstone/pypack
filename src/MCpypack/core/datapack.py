# This file contains the Datapack class

from pathlib import Path # For export directory
from typing import Dict, List
from packaging.version import Version # For checking Minecraft Version
import shutil
import json
import zipfile

from MCpypack import recipe

from .namespace import Namespace

class Datapack:
    """
    Represent a datatpack that can be exported.
    """

    def __init__(self,
                 name: str,
                 description: str,
                 version: str,
                 relative_icon_path: str = '',
                 relative_export_dir: str = "export",
                 ) -> None:
        """
        Initialize a Datapack instance.

        Parameters
        ----------
        name:
            Name of the datapack.
        description:
            Description of the datapack.
        version:
            Minecraft Version the datapack should be created for.
        relative_icon_path:
            Icon path of the datapack relative to the current working directory.
        relative_export_dir:
            Relative directory to where the datapack will be exported.
        """

        self.name: str = name
        self.version: Version = Version(version)
        self.version_value: int | float = self._get_version_value()
        self.description: str = description
        self.icon_path: Path | None = Path.cwd() / relative_icon_path if relative_icon_path else None
        self.export_dir: Path = Path.cwd() / relative_export_dir

        # Store namespaces added with 'add_namespace'
        self.namespaces: List[Namespace] = []

    def _get_version_value(self) -> int | float:
        """
        Map Minecraft version to datapack version value.

        Returns:
            int | float: Datapack version.
        """

        v: Version = self.version

        _VERSION_MAP = [
            ("1.13", "1.14.4", 4),
            ("1.15", "1.16.1", 5),
            ("1.16.2", "1.16.5", 6),
            ("1.17", "1.17.1", 7),
            ("1.18", "1.18.1", 8),
            ("1.18.2", "1.18.2", 9),
            ("1.19", "1.19.3", 10),
            ("1.19.4", "1.19.4", 12),
            ("1.20", "1.20.1", 15),
            ("1.20.2", "1.20.2", 18),
            ("1.20.3", "1.20.4", 26),
            ("1.20.5", "1.20.6", 41),
            ("1.21", "1.21.1", 48),
            ("1.21.2", "1.21.3", 57),
            ("1.21.4", "1.21.4", 61),
            ("1.21.5", "1.21.5", 71),
            ("1.21.6", "1.21.6", 80),
            ("1.21.7", "1.21.8", 81),
            ("1.21.9", "1.21.10", 88.0),
            ("1.21.11", "1.21.11", 94.1),
        ]

        for min_v, max_v, pack_format in _VERSION_MAP:
                if Version(min_v) <= v <= Version(max_v):
                    return pack_format

        # Minecraft Version not supported
        raise ValueError(f"Unsupported version of Minecraft: {v}")

    def add_namespaces(self, *namespaces: Namespace) -> None:
        """
        Add namespace to datapack.

        Parameters
        ----------
        *namespaces:
            Add one or more namespaces to the datapack.
        """
        
        # Ensure namespaces do not have the same name
        existing_namespaces: List[str] = [namespace.name for namespace in self.namespaces]

        for namespace in namespaces:
            if namespace.name in existing_namespaces:
                raise ValueError(f"Namespace with name {namespace.name} already exists in Datapack {self.name}")
            existing_namespaces.append(namespace.name)
            self.namespaces.append(namespace)

        self.namespaces.extend(namespaces)

    def export(self, overwrite: bool = True, zip: bool = False) -> None:
        """
        Export the datapack to location specified in 'relative_export_dir'.

        Creates the export directory if it does not exist.

        Parameters
        ----------
        overwrite:
            Delete the current version of the datapack and create the new one or
            panic if there is already a version of the datapack present.
            If set to 'False' append a number to the name if it already exists.
        zip:
            Export the datapack as a zip file.
        """

        # Create export directory
        self.export_dir.mkdir(parents=True, exist_ok=True)

        # Create datapack directory
        datapack_dir: Path = self.export_dir / self.name

        # Delete previous version of the datapack if present
        if overwrite and datapack_dir.is_dir():
            shutil.rmtree(datapack_dir)

        if datapack_dir.exists():
            if overwrite:
                # Delete previous version of the datapack
                shutil.rmtree(datapack_dir)
            else:
                # Next available numbered version
                counter: int = 1
                while datapack_dir.exists():
                    datapack_dir = self.export_dir / f"{self.name}_{counter}"
                    counter += 1

        datapack_dir.mkdir(parents=True, exist_ok=False)

        # Create pack.mcmeta file
        pack_mcmeta_content: Dict[str, Dict[str, str | int | float]] = {
            "pack": {
                "description": self.description,
                "min_format": self.version_value,
                "max_format": self.version_value
            }
        }

        pack_mcmeta_file: Path = datapack_dir / "pack.mcmeta"
        with open(pack_mcmeta_file, "w", encoding="utf-8") as file:
            json.dump(pack_mcmeta_content, file, indent=4)

        # Copy icon into datapack
        if self.icon_path and self.icon_path.is_file():
            destination: Path = datapack_dir / "pack.png"
            shutil.copy(self.icon_path, destination)

        # Create namespaces
        if self.namespaces:
            for namespace in self.namespaces:
                namespace.export(datapack_dir=datapack_dir)

        # Create zip if 'zip' is set to 'True'
        if zip:
            zip_file_path: Path = self.export_dir / f"{datapack_dir.name}.zip"
            with zipfile.ZipFile(zip_file_path, "w",
                                 compression=zipfile.ZIP_DEFLATED) as zipf:
                for file_path in datapack_dir.rglob("*"):
                    zipf.write(file_path,
                               arcname=file_path.relative_to(datapack_dir.parent))
