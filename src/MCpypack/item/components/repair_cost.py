# This file contains the repair_cost component

from .components import ItemComponent

class RepairCost(ItemComponent):
    """
    Repair cost item component.
    """

    TYPE = "minecraft:repair_cost"

    @property
    def repair_cost(self) -> int:
        return self._repair_cost

    @repair_cost.setter
    def repair_cost(self, value: int) -> None:
        if not value >= 0:
            raise ValueError(f"Repair cost for RepairCost must be a positive integer and not: value = {value}!")

        self._repair_cost = value


    def __init__(self, repair_cost: int = 0) -> None:
        """
        Init repair cost component.


        Parameters
        ----------
        repair_cost:
            The number of experience levels to add to the base level cost when repairing, combining, or renaming this item with an anvil. Must be a non-negative integer, defaults to 0.
        """

        super().__init__()

        self.repair_cost = repair_cost


    def to_value(self) -> int:
        return self.repair_cost
