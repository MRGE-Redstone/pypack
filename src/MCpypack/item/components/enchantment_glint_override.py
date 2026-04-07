# This file contains the enchantment_glint_override component

from .components import ItemComponent

class EnchantmentGlintOverride(ItemComponent):
    """
    Enchantment glint override item component.
    Overrides the enchantment glint effect on this item.
    """

    @property
    def TYPE(self) -> str:
        return "minecraft:enchantment_glint_override"

    def __init__(self, enchantment_glint_override: bool) -> None:
        """
        Init an EnchantmentGlintOverride component.

        Parameters
        ----------
        enchantment_glint_override:
            True -> always show enchantment glint.
            False -> never show enchantment glint.
        """

        super().__init__()

        self.enchantment_glint_override = enchantment_glint_override

    def to_value(self) -> bool:
        return self.enchantment_glint_override


