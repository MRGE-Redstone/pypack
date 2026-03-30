# This file contains regular expressions for validation

from typing import Final
from re import Pattern, compile

# Namespace:
NAMESPACE_PATTERN: Final[Pattern[str]] = compile(r"^[a-z_][a-z0-9_-]*$")

# Recipes:
RECIPE_PATTERN: Final[Pattern[str]] = compile(r"^(?:[a-z0-9_]+/)*[a-z0-9_]+$")
