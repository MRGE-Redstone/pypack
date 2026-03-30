# This file contains the CratfingTransmute class

from .recipe import Recipe


class CratfingTransmute(Recipe):
    
    @property
    def TYPE(self) -> str:
        return "crafting_transmute"
