# This file contains the glider component

from .components import ItemComponent

class Glider(ItemComponent):
    """
    Glider item component.
    If present, this item allows players to glide (as with elytra) when equipped.
    """

    @property
    def TYPE(self) -> str:
        return "minecraft:glider"

    def __init__(self) -> None:
        super().__init__()

    def to_value(self) -> dict:
        return {}
