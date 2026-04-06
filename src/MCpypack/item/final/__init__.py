# Export Item enum
# Export Tags enum
# Export TrimPattern enum

from .items import Item
from.tags import Tag
from.trim_patterns import TrimPattern

type ItemLike = Item | Tag.ITEM | list[Item] | list[Tag.ITEM] | list[Item | Tag.ITEM]

__all__: list[str] = [
    "Item",
    "Tag",
    "ItemLike",
    "TrimPattern",
]
