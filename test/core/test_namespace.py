import pytest
from unittest.mock import MagicMock

from pathlib import Path
from packaging.version import Version

from MCpypack.core import Namespace, Datapack
from MCpypack.recipe.recipe import Recipe

@pytest.mark.parametrize("name", [
    ("normal"),
    ("_under"),
    ("middle_under"),
    ("numberafterstart1"),
])
def test_name(name: str):
    assert Namespace(name).name == name

@pytest.mark.parametrize("name", [
    ("spa ce"),
    ("sl/ash"),
    ("do.t"),
    ("UPPER"),
    ("exclamation!"),
    ("@"),
    ("#"),
    ("$"),
    ("%"),
    ("^"),
    ("*"),
    ("("),
    (")"),
    ("+"),
    ("-"),
    ("="),
    (":"),
    (","),
    (";"),
    ("?"),
    ("<"),
    (">"),
    ("|"),
    ("\\"),
    ("\""),
    ("'"),
    (""),
    ("1"),
])
def test_invalid_name(name: str):
    with pytest.raises(ValueError):
        Namespace(name)

def test_empty_recipes():
    assert Namespace("ns").recipes == []

def test_add_recipes():
    ns = Namespace("ns")

    class FakeRecipe(Recipe):
        TYPE = "fake_recipe"
        
        def check_version(self, version: Version) -> bool:
            return True

        def export(self, namespace_dir: Path, version: Version) -> None:
            pass

    ns.add_recipes(
        r1 := FakeRecipe("r1"),
        r2 := FakeRecipe("r2")
    )

    assert ns.recipes == [r1, r2]

def test_namespace_path(tmp_path: Path, monkeypatch: pytest.MonkeyPatch):
    monkeypatch.chdir(tmp_path)

    pack = Datapack("n", "d", "1.20.1")
    pack.add_namespaces(Namespace("test"))

    pack.export()

    assert (tmp_path / "export" / "n" / "data" / "test").is_dir()

def test_recipe_export_called(tmp_path: Path):
    ns = Namespace("ns")

    recipe = MagicMock()
    ns.add_recipes(recipe)

    ns.export(tmp_path, Version("1.20.1"))

    recipe.export.assert_called_once()
