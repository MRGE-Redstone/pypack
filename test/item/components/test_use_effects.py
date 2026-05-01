import pytest

from MCpypack.item.components import UseEffects

def test_correct_type():
    assert UseEffects.TYPE == "minecraft:use_effects"

def test_to_value():
    
    use_effects = UseEffects(
        can_sprint=True,
        speed_multiplier=0.3,
        interact_vibrations=True,
    )

    assert use_effects.to_value() == {
        "can_sprint": True,
        "speed_multiplier": 0.3,
        "interact_vibrations": True,
    }

def test_default_values():

    use_effects = UseEffects()

    assert use_effects.can_sprint == False
    assert use_effects.speed_multiplier == 0.2
    assert use_effects.interact_vibrations == True

def test_invalid_type_can_sprint():
    with pytest.raises(TypeError):
        UseEffects(can_sprint=5)

def test_invalid_type_speed_multiplier():
    with pytest.raises(TypeError):
        UseEffects(speed_multiplier="invalid")

def test_invalid_type_interact_vibrations():
    with pytest.raises(TypeError):
        UseEffects(interact_vibrations=[])

@pytest.mark.parametrize("value", [
    (-1.0),
    (1.5),
])
def test_invalid_type_speed_multiplier(value: float):
    with pytest.raises(ValueError):
        UseEffects(speed_multiplier=value)
