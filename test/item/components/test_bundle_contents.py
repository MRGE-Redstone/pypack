import pytest

from MCpypack.item.components import BundleContents
from MCpypack.item.final import Item
from MCpypack.utils import ItemStack

def test_correct_type():
    assert BundleContents([ItemStack(item_id=Item.DIAMOND)]).TYPE == "minecraft:bundle_contents"

def test_to_value():
    bc = BundleContents(
        [
            ItemStack(item_id=Item.EMERALD),
            ItemStack(item_id=Item.STONE),
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

