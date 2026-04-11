import pytest

from MCpypack.utils import Color

def test_values_contains_all_colors():
    values = Color.values()

    expected = [
        "white",
        "light_gray",
        "gray",
        "black",
        "brown",
        "red",
        "orange",
        "yellow",
        "lime",
        "green",
        "cyan",
        "light_blue",
        "blue",
        "purple",
        "magenta",
        "pink",
    ]

    assert values == expected

def test_from_str_valid_values():
    assert Color.from_str("red") == Color.RED
    assert Color.from_str("blue") == Color.BLUE
    assert Color.from_str("light_gray") == Color.LIGHT_GREY

def test_from_str_invalid_value():
    with pytest.raises(ValueError):
        Color.from_str("invalid_color")

