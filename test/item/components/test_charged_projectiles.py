import pytest

from MCpypack.item.components import ChargedProjectiles
from MCpypack.utils import ItemStack
from MCpypack.item.final import Item

def test_correct_type():
    assert ChargedProjectiles([ItemStack(item_id=Item.EMERALD)]).TYPE == "minecraft:charged_projectiles"

def test_to_value():
    stacks = [ItemStack(item_id=Item.EMERALD), ItemStack(item_id=Item.DIAMOND)]
    assert ChargedProjectiles(stacks).to_value() == [i.to_dict() for i in stacks]

def test_invalid_value():
    with pytest.raises(TypeError):
        ChargedProjectiles("hello")

