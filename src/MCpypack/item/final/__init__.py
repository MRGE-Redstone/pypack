# Export Item enum
# Export Tags enum
# Export TrimPattern enum
# Export TrimMaterial enum
# Export Enchantment enum
# Export DamageType enum
# Export JukeboxSong enum

from .items import Item
from.tags import Tag
from.trim_patterns import TrimPattern
from .trim_materials import TrimMaterial
from .enchantments import Enchantment
from .damage_types import DamageType
from .jukebox_songs import JukeboxSong

type ItemLike = Item | Tag.ITEM | list[Item] | list[Tag.ITEM] | list[Item | Tag.ITEM]

__all__: list[str] = [
    "Item",
    "Tag",
    "ItemLike",
    "TrimPattern",
    "TrimMaterial",
    "Enchantment",
    "DamageType",
    "JukeboxSong",
]
