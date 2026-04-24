# This file contains the max_stack_size component

from .components import ItemComponent

class MaxStackSize(ItemComponent):
    """
    Max stack size item component.
    """

    @property
    def TYPE(self) -> str:
        return "minecraft:max_stack_size"

    @property
    def max_stack_size(self) -> int:
        return self._max_stack_size

    @max_stack_size.setter
    def max_stack_size(self, value: int) -> None:
        if not isinstance(value, int):
            raise TypeError(f"max_stack_size must be of type int, got: {type(value)}")

        if not 1 <= value <= 99:
            raise ValueError(f"max_stack_size must be an integer between 1 and 99, got : max_stack_size = {value}")

        self._max_stack_size = value

    def __init__(self, max_stack_size: int) -> None:
        """
        Init a max damage component.

        Parameters
        ----------
        max_stack_size:
            The maximum number of items that can fit in a stack. Must be a positive integer between 1 and 99 (inclusive).
        """

        super().__init__()

        self.max_stack_size = max_stack_size

    def to_value(self) -> int:
        return self.max_stack_size

