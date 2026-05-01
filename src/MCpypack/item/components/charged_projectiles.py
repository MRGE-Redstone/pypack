# This file contains the charged_projectiles component

from .components import ItemComponent

from MCpypack.utils import ItemStack

class ChargedProjectiles(ItemComponent):
    """
    Charhed projectiles item component.
    """

    TYPE = "minecraft:charged_projectiles"

    @property
    def charged_projectiles(self) -> list[ItemStack]:
        return self._charged_projectiles

    @charged_projectiles.setter
    def charged_projectiles(self, value: list[ItemStack]) -> None:
        if not isinstance(value, list):
            raise TypeError(f"charged_projectiles must be of type list[ItemStack], got: {type(value)}")

        self._charged_projectiles = value

    def __init__(self, charged_projectiles: list[ItemStack]) -> None:
        """
        Init charged projectiles component.

        Parameters
        ----------
        charged_projectiles:
            A single item stack.
        """

        super().__init__()

        self.charged_projectiles = charged_projectiles

    def to_value(self) -> list[dict]:
        return [stack.to_dict() for stack in self.charged_projectiles]
