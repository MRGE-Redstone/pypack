# This file contains the bundle_contents component

from .components import ItemComponent
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from MCpypack.utils import ItemStack

class BundleContents(ItemComponent):
    """
    Bundle contents item component.
    """

    TYPE = "minecraft:bundle_contents"

    def __init__(self, bundle_contents: list[ItemStack]) -> None:
        """
        Init bundle contents component.

        Parameters
        ----------
        bundle_contents:
            The items stored inside this bundle.
        """

        super().__init__()

        self.bundle_contents = [result.to_dict() for result in bundle_contents]

    def to_value(self) -> list[dict]:
        return self.bundle_contents
