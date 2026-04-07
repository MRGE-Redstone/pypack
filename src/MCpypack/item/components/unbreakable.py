# This file contains the unbreakable component

from .components import ItemComponent

class Unbreakable(ItemComponent):
    """
    Unbreakable item component.
    If set, this item cannot lose durability, and blue "Unbreakable" text will appear in the item's tooltip.
    """

    @property
    def TYPE(self) -> str:
        return "minecraft:unbreakable"

    def __init__(self) -> None:
        super().__init__()

    def to_value(self) -> dict:
        return {}

