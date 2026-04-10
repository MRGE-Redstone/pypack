# This file contains the repairable component

from .components import ItemComponent
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from MCpypack.item import ItemLike

class Repairable(ItemComponent):
    """
    Repairable item component.
    Allows the item to be repaired, if damageable, in an anvil using the specified ingredient. Also repairs equipped items in the body slot of a tamed wolf.
    """

    @property
    def TYPE(self) -> str:
        return "minecraft:repairable"

    def __init__(self, items: ItemLike) -> None:
        """
        Init repairable item component.


        Parameters
        ----------
        items:
            Items which can be used to repair this item.
        """

        super().__init__()

        if isinstance(items, list):
            self.items  = [i.value for i in items]
        else:
            self.items = items.value

    def to_value(self) -> dict[str, list[str] | str]:
        return {
            "items": self.items
        }
