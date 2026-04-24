import pytest

from MCpypack.item.components import MinimumAttackCharge

def test_correct_type():
    assert MinimumAttackCharge(1.0).TYPE == "minecraft:minimum_attack_charge"

def test_to_value():
    assert MinimumAttackCharge(1.0).to_value() == 1.0

@pytest.mark.parametrize("minimum_attack_charge", [
    (0.0),
    (1.0),
    (0.5),
])
def test_valid_values(minimum_attack_charge: int):
    MinimumAttackCharge(minimum_attack_charge)

def test_invalid_type():
    with pytest.raises(TypeError):
        MinimumAttackCharge("string")

@pytest.mark.parametrize("minimum_attack_charge", [
    (-0.7),
    (1.5),
])
def test_invalid_values(minimum_attack_charge: int):
    with pytest.raises(ValueError):
        MinimumAttackCharge(minimum_attack_charge)
