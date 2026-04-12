import pytest

from MCpypack.utils import SwingAnimation

def test_values_contains_all_colors():
    values = SwingAnimation.values()

    expected = [
        "none",
        "whack",
        "stab"
    ]

    assert values == expected

@pytest.mark.parametrize("string, animation", [
    ("none", SwingAnimation.NONE),
    ("whack", SwingAnimation.WHACK),
    ("stab", SwingAnimation.STAB),
])
def test_from_str_valid_values(string: str, animation: SwingAnimation):
    assert SwingAnimation.from_str(string) == animation

def test_from_str_invalid_value():
    with pytest.raises(ValueError):
        SwingAnimation.from_str("invalid_animation")
