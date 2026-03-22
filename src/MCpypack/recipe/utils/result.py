from dataclasses import dataclass, field

from MCpypack.item import Item

@dataclass
class Result:
    """
    Represents the result of a recipe.
    """

    item_id: Item
    _count: int = field(default=1)
    components: None = field(default=None)

    @property
    def count(self) -> int:
        return self._count

    @count.setter
    def count(self, value: int) -> None:
        if not 1 <= value <= 64:
            raise ValueError(f"count must be between 1 and 64, got {value}")
        self._count = value

    def __post_init__(self) -> None:
        """
        Validate fields after initialization.
        """

        # Ensure count is between 1 and 64
        self.count = self._count

        # Ensure components is not used
        if self.components is not None:
            raise NotImplementedError("The 'components' field is not implemented yet.")

    def to_dict(self) -> dict:
        return {
            "id": self.item_id.value,
            "count": self._count
        }
