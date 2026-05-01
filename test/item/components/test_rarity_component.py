import pytest

from MCpypack.item.components import Rarity
from MCpypack.utils import Rarity as ERarity

def test_correct_type():
    assert Rarity(rarity=ERarity.COMMON).TYPE == "minecraft:rarity"


@pytest.mark.parametrize("rarity", [
    (ERarity.COMMON),
    (ERarity.UNCOMMON),
    (ERarity.RARE),
    (ERarity.EPIC),
])
def test_correct_color(rarity: ERarity):
    bc = Rarity(rarity=rarity)

    assert bc.rarity == rarity

@pytest.mark.parametrize("rarity, rarity_str", [
    (ERarity.COMMON, "common"),
    (ERarity.UNCOMMON, "uncommon"),
    (ERarity.RARE, "rare"),
    (ERarity.EPIC, "epic"),
])
def test_to_value(rarity: ERarity, rarity_str: str):
    bc = Rarity(rarity=rarity)

    assert bc.to_value() == rarity_str
