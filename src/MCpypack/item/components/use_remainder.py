# This file contains the use_remainder component

from .components import ItemComponent
from typing import TYPE_CHECKING


if TYPE_CHECKING:
    # We use this to avoid circular imports
    from MCpypack.utils import CountedResult

class UseRemainder(ItemComponent):
    """
    Use remainder item component.
    If present, replaces the item with a remainder item if its stack count has decreased after use.
    """

    @property
    def TYPE(self) -> str:
        return "minecraft:use_remainder"

    def __init__(self, use_remainder: CountedResult) -> None:
        """
        Init use remainder component.

        Parameters
        ----------
        use_remainder:
            A single item stack.
        """

        super().__init__()

        self.use_remainder = use_remainder

    def to_value(self) -> dict:
        return self.use_remainder.to_dict()
