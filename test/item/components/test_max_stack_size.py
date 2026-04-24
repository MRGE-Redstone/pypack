import pytest

from MCpypack.item.components import MaxStackSize

def test_correct_type():
    assert MaxStackSize(1).TYPE == "minecraft:max_stack_size"

def test_to_value():
    assert MaxStackSize(1).to_value() == 1

@pytest.mark.parametrize("max_stack_size", [
    (1),
    (35),
    (99),
])
def test_valid_values(max_stack_size: int):
    MaxStackSize(max_stack_size)

def test_invalid_type():
    with pytest.raises(TypeError):
        MaxStackSize("string")

@pytest.mark.parametrize("max_stack_size", [
    (0),
    (-1),
    (100),
])
def test_invalid_values(max_stack_size: int):
    with pytest.raises(ValueError):
        MaxStackSize(max_stack_size)
