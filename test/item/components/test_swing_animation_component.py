import pytest

from MCpypack.item.components import SwingAnimation
from MCpypack import utils

def test_correct_type():
    assert SwingAnimation().TYPE == "minecraft:swing_animation"

def test_default_values():
    sa = SwingAnimation()

    assert sa.animation_type == "whack"
    assert sa.duration == 6

def test_to_value():
    sa = SwingAnimation()

    assert sa.to_value() == {
        "type": "whack",
        "duration": 6,
    }

def test_kwargs_required():
    with pytest.raises(TypeError):
        sa = SwingAnimation(utils.SwingAnimation.NONE, 1)

@pytest.mark.parametrize("duration", [
    (0),
    (-1),
])
def test_duration_invalid_int(duration: int):
    with pytest.raises(ValueError):
        sa = SwingAnimation(duration=duration)

@pytest.mark.parametrize("duration", [
    ("string"),
    (0.5),
])
def test_duration_invalid_type(duration: int):
    with pytest.raises(TypeError):
        sa = SwingAnimation(duration=duration)
