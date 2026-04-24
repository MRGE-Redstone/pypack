import pytest

from MCpypack.utils import Color, HexColor, TextColor

# ===== Color ===== #

def test_color_values_contains_all_colors():
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

@pytest.mark.parametrize("string, color", [
    ("red", Color.RED),
    ("blue", Color.BLUE),
    ("light_gray", Color.LIGHT_GREY),
])
def test_color_from_str_valid_values(string: str, color: Color):
    assert Color.from_str(string) == color

def test_color_from_str_invalid_value():
    with pytest.raises(ValueError):
        Color.from_str("invalid_color")

# ===== HexColor ===== #

def test_hex_color_right_value():
    assert HexColor("12aB4E").color == "#12aB4E".upper()

def test_hex_color_invalid_type():
    with pytest.raises(ValueError):
        HexColor(15)

def test_hex_color_invalid_length():
    with pytest.raises(ValueError):
        HexColor("aabbccdd")

def test_hex_color_invalid_chars():
    with pytest.raises(ValueError):
        HexColor("11qea3")

def test_hex_color_from_str():
    assert HexColor.from_str("12aB4E").color == "#12aB4E".upper()

# ===== TextColor ===== #

def test_text_color_values_contains_all_colors():
    values = TextColor.values()

    expected = [
        "black",
        "dark_blue",
        "dark_green",
        "dark_aqua",
        "dark_red",
        "dark_purple",
        "gold",
        "gray",
        "dark_gray",
        "blue",
        "green",
        "aqua",
        "red",
        "light_purple",
        "yellow",
        "white"
    ]

    assert values == expected

@pytest.mark.parametrize("string, color", [
    ("red", TextColor.RED),
    ("blue", TextColor.BLUE),
    ("aqua", TextColor.AQUA),
])
def test_text_color_from_str_valid_values(string: str, color: Color):
    assert TextColor.from_str(string) == color

def test_text_color_from_str_invalid_value():
    with pytest.raises(ValueError):
        Color.from_str("invalid_color")
