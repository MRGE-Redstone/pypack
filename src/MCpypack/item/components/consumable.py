# This file contains the consumable component

from .components import ItemComponent

class Consumable(ItemComponent):
    """
    Consumable item component.
    If present, the item can be consumed. Its options can also be modified.
    """

    TYPE = "minecraft:consumable"

    def __init__(self) -> None:
        super().__init__()

    def to_value(self) -> dict:
        return {}

