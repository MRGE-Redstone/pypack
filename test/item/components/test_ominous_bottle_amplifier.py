import pytest

from MCpypack.item.components import OminousBottleAmplifier

def test_correct_type():
    assert OminousBottleAmplifier.TYPE == "minecraft:ominous_bottle_amplifier"

def test_to_value():
    assert OminousBottleAmplifier(1).to_value() == 1

def test_invalid_type():
    with pytest.raises(TypeError):
        OminousBottleAmplifier(1.5)

@pytest.mark.parametrize("value", [
    (1),
    (2),
    (3),
    (4),
])
def test_valid_values(value: int):
    OminousBottleAmplifier(value)

@pytest.mark.parametrize("value", [
    (-1),
    (5),
])
def test_invalid_values(value: int):
    with pytest.raises(ValueError):
        OminousBottleAmplifier(value)
