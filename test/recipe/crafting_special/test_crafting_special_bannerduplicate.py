import pytest

from MCpypack.item.final import Item, Tag
from MCpypack.recipe import CraftingSpecialBannerDuplicate
from MCpypack import ItemStack

def test_correct_type():
    assert CraftingSpecialBannerDuplicate.TYPE == \
    "minecraft:crafting_special_bannerduplicate"

def test_config():
    csbd = CraftingSpecialBannerDuplicate(
        name="csbd",
        banner=Item.WHITE_BANNER,
        result=ItemStack(
            item_id=Item.WHITE_BANNER,
        )
    )

    assert csbd.config == {
        "type": "minecraft:crafting_special_bannerduplicate",
        "banner": "minecraft:white_banner",
        "result": {
            "id": "minecraft:white_banner",
        }
    }

def test_banner_list():
    csbd = CraftingSpecialBannerDuplicate(
        name="csbd",
        banner=[Item.WHITE_BANNER, Item.BLACK_BANNER],
        result=ItemStack(
            item_id=Item.WHITE_BANNER,
        )
    )

    assert csbd.config == {
        "type": "minecraft:crafting_special_bannerduplicate",
        "banner": ["minecraft:white_banner", "minecraft:black_banner"],
        "result": {
            "id": "minecraft:white_banner",
        }
    }

def test_banner_tag():
    csbd = CraftingSpecialBannerDuplicate(
        name="csbd",
        banner=Tag.ITEM.BANNERS,
        result=ItemStack(
            item_id=Item.WHITE_BANNER,
        )
    )

    assert csbd.config == {
        "type": "minecraft:crafting_special_bannerduplicate",
        "banner": "#minecraft:banners",
        "result": {
            "id": "minecraft:white_banner",
        }
    }

