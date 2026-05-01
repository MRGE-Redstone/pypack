import pytest

from MCpypack.recipe import CraftingSpecialRepairItem

def test_correct_type():
    assert CraftingSpecialRepairItem.TYPE == \
    "minecraft:crafting_special_repairitem"

def test_config():
    csri = CraftingSpecialRepairItem(
        name="csri",
    )

    assert csri.config == {
        "type": "minecraft:crafting_special_repairitem",
    }
