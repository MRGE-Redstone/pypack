import pytest

from MCpypack.item.final import Item, Tag
from MCpypack.recipe import CraftingTransmute
from MCpypack import ItemStack, Category

def test_correct_type():
    assert CraftingTransmute.TYPE == \
    "minecraft:crafting_transmute"

def test_config():
    ct = CraftingTransmute(
        name="ct",
        input=Item.DIAMOND,
        material=Item.GOLD_INGOT,
        result=ItemStack(
            item_id=Item.EMERALD,
        )
    )

    assert ct.config == {
        "type": "minecraft:crafting_transmute",
        "input": "minecraft:diamond",
        "material": "minecraft:gold_ingot",
        "result": {
            "id": "minecraft:emerald",
        },
        "category": "misc",
    }

def test_input_list():
    ct = CraftingTransmute(
        name="ct",
        input=[Item.DIAMOND, Item.GOLD_INGOT],
        material=Item.NETHERITE_INGOT,
        result=ItemStack(
            item_id=Item.EMERALD,
        )
    )

    assert ct.config == {
        "type": "minecraft:crafting_transmute",
        "input": ["minecraft:diamond", "minecraft:gold_ingot"],
        "material": "minecraft:netherite_ingot",
        "result": {
            "id": "minecraft:emerald",
        },
        "category": "misc"
    }

def test_input_tag():
    ct = CraftingTransmute(
        name="ct",
        input=Tag.ITEM.DOORS,
        material=Item.NETHERITE_INGOT,
        result=ItemStack(
            item_id=Item.EMERALD,
        )
    )

    assert ct.config == {
        "type": "minecraft:crafting_transmute",
        "input": "#minecraft:doors",
        "material": "minecraft:netherite_ingot",
        "result": {
            "id": "minecraft:emerald",
        },
        "category": "misc",
    }

def test_material_list():
    ct = CraftingTransmute(
        name="ct",
        material=[Item.DIAMOND, Item.GOLD_INGOT],
        input=Item.NETHERITE_INGOT,
        result=ItemStack(
            item_id=Item.EMERALD,
        )
    )

    assert ct.config == {
        "type": "minecraft:crafting_transmute",
        "material": ["minecraft:diamond", "minecraft:gold_ingot"],
        "input": "minecraft:netherite_ingot",
        "result": {
            "id": "minecraft:emerald",
        },
        "category": "misc"
    }

def test_material_tag():
    ct = CraftingTransmute(
        name="ct",
        material=Tag.ITEM.DOORS,
        input=Item.NETHERITE_INGOT,
        result=ItemStack(
            item_id=Item.EMERALD,
        )
    )

    assert ct.config == {
        "type": "minecraft:crafting_transmute",
        "material": "#minecraft:doors",
        "input": "minecraft:netherite_ingot",
        "result": {
            "id": "minecraft:emerald",
        },
        "category": "misc",
    }

def test_category():
    ct = CraftingTransmute(
        name="ct",
        material=Item.DIAMOND,
        input=Item.NETHERITE_INGOT,
        result=ItemStack(
            item_id=Item.EMERALD,
        ),
        category=Category.REDSTONE,
    )

    assert ct.config == {
        "type": "minecraft:crafting_transmute",
        "material": "minecraft:diamond",
        "input": "minecraft:netherite_ingot",
        "result": {
            "id": "minecraft:emerald",
        },
        "category": "redstone",
    }

def test_group():
    ct = CraftingTransmute(
        name="ct",
        material=Item.DIAMOND,
        input=Item.NETHERITE_INGOT,
        result=ItemStack(
            item_id=Item.EMERALD,
        ),
        group="test_group"
    )

    assert ct.config == {
        "type": "minecraft:crafting_transmute",
        "material": "minecraft:diamond",
        "input": "minecraft:netherite_ingot",
        "result": {
            "id": "minecraft:emerald",
        },
        "category": "misc",
        "group": "test_group",
    }
