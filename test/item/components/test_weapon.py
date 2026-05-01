import pytest

from MCpypack.item.components import Weapon

def test_correct_type():
    assert Weapon.TYPE == "minecraft:weapon"

def test_to_value():

    weapon = Weapon(
        item_damage_per_attack=5,
        disable_blocking_for_seconds=7.0
    )

    assert weapon.to_value() == {
        "item_damage_per_attack": 5,
        "disable_blocking_for_seconds": 7.0
    }

def test_default_values():
    weapon = Weapon()

    assert weapon.item_damage_per_attack == 1
    assert weapon.disable_blocking_for_seconds == 0.0

def test_invalid_type_item_damage_per_attack():
    with pytest.raises(TypeError):
        Weapon(item_damage_per_attack="hello")

def test_invalid_type_disable_blocking_for_seconds():
    with pytest.raises(TypeError):
        Weapon(disable_blocking_for_seconds="hello")

@pytest.mark.parametrize("value", [
    (-1),
])
def test_invalid_value_item_damage_per_attack(value: int):
    with pytest.raises(ValueError):
        Weapon(item_damage_per_attack=value)

@pytest.mark.parametrize("value", [
    (-1),
])
def test_invalid_value_disable_blocking_for_seconds(value: int):
    with pytest.raises(ValueError):
        Weapon(item_damage_per_attack=value)
