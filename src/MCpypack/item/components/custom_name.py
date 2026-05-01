# This file contains the custom_name component

from .components import ItemComponent
from MCpypack.utils import PlainText

class CustomName(ItemComponent):
    """
    Custom name item component.
    Used to specify an item, block, or entity's custom name. This component can be added, changed, or removed by any player with the item who has access to an anvil.
    """

    TYPE = "minecraft:custom_name"

    @property
    def custom_name(self) -> PlainText:
        return self._custom_name

    @custom_name.setter
    def custom_name(self, value: PlainText) -> None:
        if not isinstance(value, PlainText):
            raise ValueError(f"custom_name must be of type PlainText, got: {type(value)}")

        self._custom_name = value

    def __init__(self,
                 custom_name: PlainText,
                 ) -> None:
        """
        Init custom name component.

        Parameters
        ----------
        custom_name:
            Text component to use as this item, block, or entity's name. If present on an item, this component has highest priority to display as the item's name, and appears italic unless overridden by the text component format. If present on an entity, it will appear as a name tag when the entity's hitbox is hovered over by the player. If present on a block with a GUI (such as a container), this replaces the name at the top of the GUI. If present on a command block, this replaces the execution context name when the command is ran. See Text component format.
        """

        super().__init__()

        self.custom_name = custom_name

    def to_value(self) -> dict:
        return self.custom_name.to_dict()
