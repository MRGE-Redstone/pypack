import pytest

from MCpypack.item.final import Item, Tag
from MCpypack.recipe import CraftingSpecialShieldDecoration
from MCpypack import ItemStack

def test_correct_type():
    assert CraftingSpecialShieldDecoration.TYPE == \
    "minecraft:crafting_special_shielddecoration"

def test_config():
    cssd = CraftingSpecialShieldDecoration(
        name="cssd",
        banner=Item.WHITE_BANNER,
        target=Item.SHIELD,
        result=ItemStack(
            item_id=Item.WHITE_BANNER,
        )
    )

    assert cssd.config == {
        "type": "minecraft:crafting_special_shielddecoration",
        "banner": "minecraft:white_banner",
        "target": "minecraft:shield",
        "result": {
            "id": "minecraft:white_banner",
        }
    }

def test_banner_list():
    cssd = CraftingSpecialShieldDecoration(
        name="cssd",
        banner=[Item.WHITE_BANNER, Item.BLACK_BANNER],
        target=Item.SHIELD,
        result=ItemStack(
            item_id=Item.WHITE_BANNER,
        )
    )

    assert cssd.config == {
        "type": "minecraft:crafting_special_shielddecoration",
        "banner": ["minecraft:white_banner", "minecraft:black_banner"],
        "target": "minecraft:shield",
        "result": {
            "id": "minecraft:white_banner",
        }
    }

def test_banner_tag():
    cssd = CraftingSpecialShieldDecoration(
        name="cssd",
        banner=Tag.ITEM.BANNERS,
        target=Item.SHIELD,
        result=ItemStack(
            item_id=Item.WHITE_BANNER,
        )
    )

    assert cssd.config == {
        "type": "minecraft:crafting_special_shielddecoration",
        "banner": "#minecraft:banners",
        "target": "minecraft:shield",
        "result": {
            "id": "minecraft:white_banner",
        }
    }
