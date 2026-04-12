import pytest

from MCpypack.item.components import BaseColor
from MCpypack.utils import Color

def test_correct_type():
    assert BaseColor(color=Color.BLACK).TYPE == "minecraft:base_color"


@pytest.mark.parametrize("color", [
    (Color.PINK),
    (Color.YELLOW),
    (Color.LIGHT_BLUE)
])
def test_correct_color(color: Color):
    bc = BaseColor(color=color)

    assert bc.color == color

@pytest.mark.parametrize("color, color_str", [
    (Color.BLACK, "black"),
    (Color.LIGHT_GREY, "light_gray"),
    (Color.WHITE, "white"),
    (Color.PURPLE, "purple"),
])
def test_to_value(color: Color, color_str: str):
    bc = BaseColor(color=color)

    assert bc.to_value() == color_str
