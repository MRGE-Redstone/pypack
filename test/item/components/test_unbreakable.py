import pytest

from MCpypack.item.components import Unbreakable

def test_correct_type():
    assert Unbreakable().TYPE == "minecraft:unbreakable"

def test_to_value():
    assert Unbreakable().to_value() == {}
