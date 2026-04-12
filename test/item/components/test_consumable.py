import pytest

from MCpypack.item.components import Consumable

def test_correct_type():
    assert Consumable().TYPE == "minecraft:consumable"

def test_to_value():
    assert Consumable().to_value() == {}
