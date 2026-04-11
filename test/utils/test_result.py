import pytest

from MCpypack.utils import SimpleResult, CountedResult
from MCpypack.item.final import Item
from MCpypack import components

def test_simple_result_to_dict_minimal():
    result = SimpleResult(item_id=Item.STONE)

    assert result.to_dict() == {
        "id": "minecraft:stone"
    }

def test_simple_result_with_components():
    result = SimpleResult(
        item_id=Item.DIAMOND,
        components=components.ItemComponents(
            components.Glider()
        )
    )

    assert result.to_dict() == {
        "id": "minecraft:diamond",
        "components": {
            "minecraft:glider": {}
        }
    }

def test_counted_result_default_count():
    result = CountedResult(item_id=Item.STONE)

    assert result.count == 1
    assert result.to_dict() == {
        "id": "minecraft:stone"
    }

def test_counted_result_with_count():
    result = CountedResult(item_id=Item.STONE, count=5)

    assert result.count == 5
    assert result.to_dict() == {
        "id": "minecraft:stone",
        "count": 5
    }

def test_counted_result_with_components():
    result = CountedResult(
        item_id=Item.DIAMOND,
        count=2,
        components=components.ItemComponents(
            components.Glider()
        )
    )

    assert result.to_dict() == {
        "id": "minecraft:diamond",
        "count": 2,
        "components": {
            "minecraft:glider": {}
        }
    }

@pytest.mark.parametrize("invalid_count", [0, -1, 100, 999])
def test_count_validation_invalid(invalid_count):
    with pytest.raises(ValueError):
        CountedResult(item_id=Item.EMERALD, count=invalid_count)

def test_count_validation_valid_lower_bound():
    assert CountedResult(item_id=Item.EMERALD, count=1).count == 1

def test_count_validation_valid_upper_bound():
    assert CountedResult(item_id=Item.EMERALD, count=99).count == 99
