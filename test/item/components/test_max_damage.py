import pytest

from MCpypack.item.components import MaxDamage

def test_correct_type():
    assert MaxDamage(1).TYPE == "minecraft:max_damage"

def test_to_value():
    assert MaxDamage(1).to_value() == 1

@pytest.mark.parametrize("max_damage", [
    (1),
    (64),
])
def test_valid_values(max_damage: int):
    MaxDamage(max_damage)

def test_invalid_type():
    with pytest.raises(TypeError):
        MaxDamage("string")

@pytest.mark.parametrize("max_damage", [
    (0),
    (-1),
])
def test_invalid_values(max_damage: int):
    with pytest.raises(ValueError):
        MaxDamage(max_damage)
