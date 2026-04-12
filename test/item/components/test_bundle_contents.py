import pytest

from MCpypack.item.components import BundleContents
from MCpypack.item.final import Item
from MCpypack.utils import CountedResult

def test_correct_type():
    assert BundleContents([CountedResult(item_id=Item.DIAMOND)]).TYPE == "minecraft:bundle_contents"

def test_to_value():
    bc = BundleContents(
        [
            CountedResult(Item.EMERALD),
            CountedResult(Item.STONE),
        ]
    )

    assert bc.to_value() == [
        {
            "id": "minecraft:emerald"
        },
        {
            "id": "minecraft:stone"
        }
    ]

