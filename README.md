# MCpypack

[![Python](https://img.shields.io/badge/python-3.14%2B-blue)](https://www.python.org/)
[![PyPI](https://img.shields.io/pypi/v/MCpypack)](https://pypi.org/project/MCpypack/)
[![License](https://img.shields.io/badge/license-GPLv3-red)](LICENSE)
[![Downloads](https://img.shields.io/pypi/dm/MCpypack)](https://pypi.org/project/MCpypack/)

- Create Minecraft Datapacks easily using Python

> [!WARNING]
> This project is still in early development. Features may change and bugs may occur.

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
from MCpypack.core import Datapack, Namespace
from MCpypack.recipe import CraftingShapeless
from MCpypack.utils import ItemStack, Rarity, SwingAnimation, PlainText, TextColor, Formatting
from MCpypack import components
from MCpypack.item.final import Item, Enchantment, DamageType

# Create a new datapack
pack = Datapack(name="mcpypack", description='mcpypack yay', version='26.1')

# Create a new namespace
ns1 = Namespace('recipes')

# Add recipes to the namespace
ns1.add_recipes(
    CraftingShapeless(
        name="python",
        ingredients=[Item.DIAMOND_SWORD, Item.COPPER_INGOT],
        result=ItemStack(
            item_id=Item.COPPER_SWORD,
            count=1,
            components=components.ItemComponents(
                components.EnchantmentGlintOverride(True),
                components.AttackRange(
                    max_reach=25
                ),
                components.DamageType(
                    DamageType.LIGHTNING_BOLT
                ),
                components.Rarity(
                    Rarity.EPIC
                ),
                components.Weapon(
                    item_damage_per_attack=0,
                    disable_blocking_for_seconds=5.0
                ),
                components.Unbreakable(),
                components.Enchantments(
                    {
                        Enchantment.KNOCKBACK: 50,
                        Enchantment.SHARPNESS: 5,
                    }
                ),
                components.SwingAnimation(
                    animation_type=SwingAnimation.STAB,
                    duration=10,
                ),
                components.ItemName(PlainText(
                    text="MCpypack Sword",
                    formatting=Formatting(
                        color=TextColor.AQUA,
                        bold=True,
                    )
                ))
            )
        )
    ),
)

# Add the namespace to the datapack
pack.add_namespaces(ns1)

# Export the datapack
pack.export()
```

## Website
- See documentation about MCpypack under our [Website](https://mcpypack.kenolej.de)

## Tests
- We use [pytest](https://pytest.org)
- See an overview of the tests [here](test/TESTS.md)

## Roadmap
- See our [Roadmap](ROADMAP.md)

## License
- This project is licensed under the [GNU General Public License v3.0](LICENSE) (GPL-3.0).
