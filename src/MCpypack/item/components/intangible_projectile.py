# This file contains the intangible_projectile component

from .components import ItemComponent

class IntangibleProjectile(ItemComponent):
    """
    Intangible projectile item component.
    If present on an item that can be used as a projectile without breaking upon impact (such as arrows and tridents), the projectile cannot be picked up by a player once fired, unless they are in creative mode. When present on any item, a line of gray text that says "Intangible" is added to the item's tooltip.
    """

    TYPE = "minecraft:intangible_projectile"

    def __init__(self) -> None:
        super().__init__()

    def to_value(self) -> dict:
        return {}

