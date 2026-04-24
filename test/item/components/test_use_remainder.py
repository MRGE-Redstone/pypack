import pytest

from MCpypack.item.components import UseRemainder
from MCpypack.utils import ItemStack
from MCpypack.item.final import Item

def test_correct_type():
    assert UseRemainder(ItemStack(item_id=Item.EMERALD)).TYPE == "minecraft:use_remainder"

def test_to_value():
    stack = ItemStack(item_id=Item.EMERALD)
    assert UseRemainder(stack).to_value() == stack.to_dict()

def test_invalid_value():
    with pytest.raises(ValueError):
        UseRemainder("hello")
