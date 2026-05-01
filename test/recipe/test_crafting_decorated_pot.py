import pytest

from MCpypack.item.final import Item, Tag
from MCpypack.recipe import CraftingDecoratedPot
from MCpypack import ItemStack

def test_correct_type():
    assert CraftingDecoratedPot.TYPE == \
    "minecraft:crafting_decorated_pot"

def test_config():
    cdp = CraftingDecoratedPot(
        name="cdp",
        left=Item.DIAMOND,
        right=Item.DIAMOND,
        front=Item.DIAMOND,
        back=Item.DIAMOND,
        result=ItemStack(
            item_id=Item.EMERALD,
        )
    )

    assert cdp.config == {
        "type": "minecraft:crafting_decorated_pot",
        "left": "minecraft:diamond",
        "right": "minecraft:diamond",
        "front": "minecraft:diamond",
        "back": "minecraft:diamond",
        "result": {
            "id": "minecraft:emerald",
        }
    }

def test_list():
    cdp = CraftingDecoratedPot(
        name="cdp",
        left=[Item.DIAMOND, Item.GOLD_INGOT],
        right=[Item.DIAMOND, Item.GOLD_INGOT],
        front=[Item.DIAMOND, Item.GOLD_INGOT],
        back=[Item.DIAMOND, Item.GOLD_INGOT],
        result=ItemStack(
            item_id=Item.EMERALD,
        )
    )

    assert cdp.config == {
        "type": "minecraft:crafting_decorated_pot",
        "left": ["minecraft:diamond", "minecraft:gold_ingot"],
        "right": ["minecraft:diamond", "minecraft:gold_ingot"],
        "front": ["minecraft:diamond", "minecraft:gold_ingot"],
        "back": ["minecraft:diamond", "minecraft:gold_ingot"],
        "result": {
            "id": "minecraft:emerald",
        }
    }

def test_tag():
    cdp = CraftingDecoratedPot(
        name="cdp",
        left=Tag.ITEM.BUTTONS,
        right=Tag.ITEM.BUTTONS,
        front=Tag.ITEM.BUTTONS,
        back=Tag.ITEM.BUTTONS,
        result=ItemStack(
            item_id=Item.EMERALD,
        )
    )

    assert cdp.config == {
        "type": "minecraft:crafting_decorated_pot",
        "left": "#minecraft:buttons",
        "right": "#minecraft:buttons",
        "front": "#minecraft:buttons",
        "back": "#minecraft:buttons",
        "result": {
            "id": "minecraft:emerald",
        }
    }

def test_mixed():
    cdp = CraftingDecoratedPot(
        name="cdp",
        left=Tag.ITEM.BUTTONS,
        right=Item.EMERALD,
        front=Tag.ITEM.ANVIL,
        back=[Item.GOLD_INGOT, Item.IRON_INGOT, Item.NETHERITE_INGOT],
        result=ItemStack(
            item_id=Item.EMERALD,
        )
    )

    assert cdp.config == {
        "type": "minecraft:crafting_decorated_pot",
        "left": "#minecraft:buttons",
        "right": "minecraft:emerald",
        "front": "#minecraft:anvil",
        "back": [
            "minecraft:gold_ingot",
            "minecraft:iron_ingot",
            "minecraft:netherite_ingot"
        ],
        "result": {
            "id": "minecraft:emerald",
        }
    }
