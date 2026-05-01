import pytest

from MCpypack.item.final import Item, Tag
from MCpypack.recipe import Stonecutting
from MCpypack import ItemStack

def test_correct_type():
    assert Stonecutting.TYPE == \
    "minecraft:stonecutting"

def test_config():
    s = Stonecutting(
        name="s",
        ingredient=Item.DIAMOND,
        result=ItemStack(
            item_id=Item.EMERALD,
        )
    )

    assert s.config == {
        "type": "minecraft:stonecutting",
        "ingredient": "minecraft:diamond",
        "result": {
            "id": "minecraft:emerald",
        }
    }

def test_ingredient_list():
    s = Stonecutting(
        name="s",
        ingredient=[Item.DIAMOND, Item.GOLD_INGOT],
        result=ItemStack(
            item_id=Item.EMERALD,
        )
    )

    assert s.config == {
        "type": "minecraft:stonecutting",
        "ingredient": ["minecraft:diamond", "minecraft:gold_ingot"],
        "result": {
            "id": "minecraft:emerald",
        }
    }

def test_ingredient_tag():
    s = Stonecutting(
        name="s",
        ingredient=Tag.ITEM.DOORS,
        result=ItemStack(
            item_id=Item.EMERALD,
        )
    )

    assert s.config == {
        "type": "minecraft:stonecutting",
        "ingredient": "#minecraft:doors",
        "result": {
            "id": "minecraft:emerald",
        }
    }
