import pytest

from MCpypack.item.components import Glider

def test_correct_type():
    assert Glider().TYPE == "minecraft:glider"

def test_to_value():
    assert Glider().to_value() == {}
