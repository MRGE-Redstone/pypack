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
    class NoType(ItemComponent):
        def to_value(self) -> str:
            return "to_value"

    with pytest.raises(TypeError):
        t = NoType()

def test_requires_to_value():
    class NoToValue(ItemComponent):
        @property
        def TYPE(self) -> str:
            return "type"

    with pytest.raises(TypeError):
        t = NoToValue()
