from dataclasses import dataclass, field

@dataclass
class Result:
    """
    Represents the result of a recipe.
    """

    item_id: str
    _count: int
    components: None = field(default=None)

    @property
    def count(self) -> int:
        return self._count

    @count.setter
    def count(self, value: int) -> None:
        if not 1 <= value <= 64:
            raise ValueError(f"count must be between 1 and 64, got {self._count}")
        self._count = value

    def __post_init__(self) -> None:
        """
        Validate fields after initialization.
        """

        # Ensure count is between 1 and 64
        self._count = self._count

        # Ensure components is not used
        if self.components is not None:
            raise NotImplementedError("The 'components' field is not implemented yet.")
