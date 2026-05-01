import pytest

from MCpypack.item.components import ItemComponents
from MCpypack.item.components.components import ItemComponent
from MCpypack.item.components import Glider, Unbreakable

def test_add_one_component():
    assert ItemComponents(Glider()).config == {"minecraft:glider": {}}

def test_add_multiple_components():
    ic = ItemComponents(
        Glider(),
        Unbreakable()
    )

    assert ic.config == {
        "minecraft:glider": {},
        "minecraft:unbreakable": {}
    }

def test_requires_TYPE():
    with pytest.raises(TypeError):

        class NoType(ItemComponent):
            def to_value(self) -> str:
                return "to_value"

def test_TYPE_correct_type():
    with pytest.raises(TypeError):

        class NoType(ItemComponent):
            TYPE = 5

def test_requires_to_value():
    class NoToValue(ItemComponent):
        TYPE = "type"

    with pytest.raises(TypeError):
        t = NoToValue()

def test_remove_component():
    class TestComponent(ItemComponent):
        TYPE = "test_component"

    assert ~TestComponent == "!test_component"
