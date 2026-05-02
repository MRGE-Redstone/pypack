import pytest

from MCpypack.item.components import ItemComponents
from MCpypack.item.components.glider import Glider
from MCpypack.item.components.unbreakable import Unbreakable
from MCpypack.utils import ItemStack
from MCpypack.item.final import Item
from MCpypack import components

def test_item_stack_default_count():
    stack = ItemStack(item_id=Item.STONE)

    assert stack.item_count == 1
    assert stack.to_dict() == {
        "id": "minecraft:stone"
    }

def test_item_stack_with_count():
    stack = ItemStack(item_id=Item.STONE, count=5)

    assert stack.item_count == 5
    assert stack.to_dict() == {
        "id": "minecraft:stone",
        "count": 5
    }

def test_item_stack_with_components():
    stack = ItemStack(
        item_id=Item.DIAMOND,
        count=2,
        components=components.ItemComponents(
            components.Glider()
        )
    )

    assert stack.to_dict() == {
        "id": "minecraft:diamond",
        "count": 2,
        "components": {
            "minecraft:glider": {}
        }
    }

@pytest.mark.parametrize("invalid_count", [0, -1, 100, 999])
def test_count_validation_invalid(invalid_count):
    with pytest.raises(ValueError):
        ItemStack(item_id=Item.EMERALD, count=invalid_count)

def test_count_validation_valid_lower_bound():
    assert ItemStack(item_id=Item.EMERALD, count=1).item_count == 1

def test_count_validation_valid_upper_bound():
    assert ItemStack(item_id=Item.EMERALD, count=99).item_count == 99

def test_require_kwargs():
    with pytest.raises(TypeError):
        ItemStack(Item.EMERALD)

def test_item_must_be_item():
    with pytest.raises(TypeError):
        ItemStack(
            item_id=1, 
        )

def test_count_must_be_int():
    with pytest.raises(TypeError):
        ItemStack(
            item_id=Item.EMERALD, 
            count="lol",
        )

def test_components_must_components_or_none():
    with pytest.raises(TypeError):
        ItemStack(
            item_id=Item.EMERALD, 
            components=1,
        )

def test_item_method():
    sword1 = ItemStack.item(Item.COPPER_SWORD)
    sword2 = ItemStack(item_id=Item.COPPER_SWORD)

    assert sword1.item == sword2.item

def test_chain_count():
    sword = ItemStack.item(Item.COPPER_SWORD) \
                .count(5)

    assert sword.item_count == 5

def test_chain_component():
    sword = ItemStack.item(Item.COPPER_SWORD) \
            .component(Glider())

    if isinstance(sword.components, type(None)):
        raise TypeError("Should not be None")

    assert sword.components.config == ItemComponents(Glider()).config

def test_chain_components():
    sword = ItemStack.item(Item.COPPER_SWORD) \
        .component(Glider()) \
        .component(Unbreakable())

    if isinstance(sword.components, type(None)):
        raise TypeError("Should not be None")

    assert sword.components.config == ItemComponents(
        Glider(),
        Unbreakable()
    ).config

def test_chain_remove_component():
    sword = ItemStack.item(Item.COPPER_SWORD) \
        .component(~Glider)

    if isinstance(sword.components, type(None)):
        raise TypeError("Should not be None")

    assert sword.components.config == {"!minecraft:glider": {}}
