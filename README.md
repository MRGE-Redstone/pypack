# MCpypack

[![Python](https://img.shields.io/badge/python-3.14%2B-blue)](https://www.python.org/)
[![PyPI](https://img.shields.io/pypi/v/MCpypack)](https://pypi.org/project/MCpypack/)
[![License](https://img.shields.io/badge/license-GPLv3-red)](LICENSE)
[![Downloads](https://img.shields.io/pypi/dm/MCpypack)](https://pypi.org/project/MCpypack/)

- Create Minecraft Datapacks easily using Python

## Features
- Easy datapack creation
- Namespaces
- Recipes

## Installation
```bash
pip intall MCpypack
```

## Example
```python
from MCpypack import *

# Create a new datapack
pack = Datapack(name="useful_recipes", description='Adds useful recipes like GOD Apple and grass blocks', version='1.21.10')

# Create a new namespace
ns1 = Namespace('recipes')

# Add recipes to the namespace
ns1.add_recipes(
    Smelting("burning_gundpowder", Item.GUNPOWDER, SimpleResult(Item.FIRE_CHARGE), Time(Seconds(2),Milliseconds(500))),
    Smoking("tearing_eyes", Item.ENDER_PEARL, SimpleResult(Item.ENDER_EYE), Time(Minutes(2),Seconds(30)),experience=5),
    Blasting("blasting_obsidian_until_it_cries", Item.OBSIDIAN, SimpleResult(Item.CRYING_OBSIDIAN), Time(Seconds(10)),experience=1),
    
    CraftingShapeless(
        name="grass_block",
        ingredients=[[Item.SHORT_GRASS,Item.SHORT_DRY_GRASS,Item.TALL_DRY_GRASS,Item.TALL_GRASS], Item.DIRT],
        result=CountedResult(Item.GRASS_BLOCK)
    ),
    Stonecutting(
        name="wooden_chair",
        ingredient=Item.OAK_PLANKS,
        result=CountedResult(Item.OAK_STAIRS, count=1)
    ),
    CampfireCooking(
        name="wood_coal",
        ingredient=[Item.OAK_LOG, Item.ACACIA_LOG, Item.BIRCH_LOG, Item.CHERRY_LOG, Item.DARK_OAK_LOG, Item.JUNGLE_LOG, Item.MANGROVE_LOG, Item.PALE_OAK_LOG, Item.SPRUCE_LOG],
        result=SimpleResult(Item.CHARCOAL),
        cookingtime=Time(Seconds(5)),
        experience=0.5
    ),
    CampfireCooking(
        name="weedy_bread",
        ingredient=Item.WHEAT,
        result=SimpleResult(Item.BREAD),
        cookingtime=Time(Minutes(1),Seconds(30)),
        experience=3
    ),
    CraftingShaped(
        name="god_apple",
        pattern=["AAA", "ABA", "AAA"],
        key={"A": Item.GOLD_BLOCK, "B": Item.APPLE},
        result=CountedResult(Item.ENCHANTED_GOLDEN_APPLE)
    ),
    CraftingShaped(
        name="totem_of_dying",
        pattern=["ABA", "AAA", " A "],
        key={"A": Item.GOLD_BLOCK, "B": [Item.DIAMOND, Item.EMERALD]},
        result=CountedResult(Item.TOTEM_OF_UNDYING)
    )
)

# Add the namespace to the datapack
pack.add_namespaces(ns1)

# Export the datapack
pack.export(overwrite=True)
```

## License
- This project is licensed under the [GNU General Public License v3.0](LICENSE) (GPL-3.0).
