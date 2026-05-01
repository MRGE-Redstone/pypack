import pytest

from MCpypack.item.final import Item, Tag
from MCpypack.recipe import CampfireCooking
from MCpypack import ItemStack, Time
from MCpypack.utils.times import Seconds

def test_correct_type():
    assert CampfireCooking.TYPE == \
    "minecraft:campfire_cooking"

def test_config():
    cc = CampfireCooking(
        name="cc",
        ingredient=Item.EMERALD,
        result=ItemStack(
            item_id=Item.DIAMOND,
        )
    )

    assert cc.config == {
        "type": "minecraft:campfire_cooking",
        "ingredient": "minecraft:emerald",
        "result": {
            "id": "minecraft:diamond",
        }
    }

def test_ingredient_list():
    cc = CampfireCooking(
        name="cc",
        ingredient=[Item.DIAMOND, Item.GOLD_INGOT],
        result=ItemStack(
            item_id=Item.EMERALD,
        )
    )

    assert cc.config == {
        "type": "minecraft:campfire_cooking",
        "ingredient": ["minecraft:diamond", "minecraft:gold_ingot"],
        "result": {
            "id": "minecraft:emerald",
        }
    }

def test_ingredient_tag():
    cc = CampfireCooking(
        name="cc",
        ingredient=Tag.ITEM.BEDS,
        result=ItemStack(
            item_id=Item.DIAMOND,
        )
    )

    assert cc.config == {
        "type": "minecraft:campfire_cooking",
        "ingredient": "#minecraft:beds",
        "result": {
            "id": "minecraft:diamond",
        }
    }

def test_cooking_time():
    cc = CampfireCooking(
        name="cc",
        ingredient=Item.DIAMOND,
        result=ItemStack(
            item_id=Item.DIAMOND,
        ), 
        cookingtime=Time(Seconds(1))
    )

    assert cc.config["cookingtime"] == 20

def test_experience():
    cc = CampfireCooking(
        name="cc",
        ingredient=Item.DIAMOND,
        result=ItemStack(
            item_id=Item.DIAMOND,
        ), 
        experience=5
    )

    assert cc.config["experience"] == 5

def test_complete_config():
    cc = CampfireCooking(
        name="cc",
        ingredient=Item.EMERALD,
        result=ItemStack(
            item_id=Item.DIAMOND,
        ),
        cookingtime=Time(Seconds(1)),
        experience=5,
    )

    assert cc.config == {
        "type": "minecraft:campfire_cooking",
        "ingredient": "minecraft:emerald",
        "result": {
            "id": "minecraft:diamond",
        },
        "cookingtime": 20,
        "experience": 5.
    }
