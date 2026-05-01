# This file contains the container component

from .components import ItemComponent
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from MCpypack.utils import ItemStack

class Container(ItemComponent):
    """
    Container item component.
    """

    TYPE = "minecraft:container"

    @property
    def container(self) -> dict[int, dict]:
        return self._container

    @container.setter
    def container(self, value: dict[int, ItemStack]) -> None:
        _container: dict[int, dict] = {}
        for slot, item_stack in value.items():
            if slot < 0:
                raise ValueError(f"Slot number must be a positive integer or 0, got: {slot} for {item_stack.to_dict()}")

            _container[slot] = item_stack.to_dict()

        self._container = _container

    def __init__(self, container: dict[int, ItemStack]) -> None:
        """
        Init container item component.

        Parameters
        ----------
        container:
            Dictionary of slot number in the container and the corresponding item stack.
        """
        super().__init__()

        self.container = container

    def to_value(self) -> list[dict]:
        return [{"slot": slot, "item": item} for slot, item in self.container.items()]
