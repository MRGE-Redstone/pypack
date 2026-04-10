import pytest
from unittest.mock import MagicMock

from pathlib import Path
from packaging.version import Version
import json

from MCpypack.core import Datapack, Namespace

def test_name():

    assert Datapack("name", "d", version="1.20.1").name == "name"

def test_description():

    assert Datapack("n", "description", version="1.20.1").description == "description"

def test_version():

    assert Datapack("n", "d", version="1.20.1").version == Version("1.20.1")

@pytest.mark.parametrize("version, expected", [
    ("1.20.1", 15),
    ("1.19", 10),
    ("1.19.3", 10),
    ("1.19.1", 10),
])
def test_version_mapping(version, expected):
    assert Datapack("n", "d", version).version_value == expected

def test_invalid_version():
    with pytest.raises(ValueError):
        Datapack("n", "d", "0.0.1")


def test_default_icon_path():
    assert Datapack("n", "d", "1.20.1").icon_path is None

def test_icon_path(tmp_path: Path, monkeypatch: pytest.MonkeyPatch):
    monkeypatch.chdir(tmp_path)

    pack = Datapack(
        "n",
        "d",
        "1.20.1",
        relative_icon_path="icon.png"
    )
    assert pack.icon_path == tmp_path / "icon.png"

def test_default_export_dir(tmp_path: Path, monkeypatch: pytest.MonkeyPatch):
    monkeypatch.chdir(tmp_path)

    assert Datapack("n", "d", "1.20.1").export_dir == tmp_path / "export"

def test_custom_export_dir(tmp_path: Path, monkeypatch: pytest.MonkeyPatch):
    monkeypatch.chdir(tmp_path)

    pack = Datapack(
        "n",
        "d",
        "1.20.1",
        relative_export_dir="build"
    )
    assert pack.export_dir == tmp_path / "build"

def test_empty_namespaces():
    assert Datapack("n", "d", "1.20.1").namespaces == []

def test_add_namespaces():
    pack = Datapack("n", "d", "1.20.1")

    pack.add_namespaces(
        ns1 := Namespace("ns1"),
        ns2 := Namespace("ns2")
    )

    assert pack.namespaces == [ns1, ns2]

def test_duplicate_namespaces():
    pack = Datapack("n", "d", "1.20.1")

    with pytest.raises(ValueError):
        pack.add_namespaces(Namespace("ns1"), Namespace("ns1"))

def test_export_creates_structure(tmp_path: Path, monkeypatch: pytest.MonkeyPatch):
    monkeypatch.chdir(tmp_path)

    dp = Datapack("testpack", "desc", "1.20.1")
    dp.export()

    base = tmp_path / "export" / "testpack"

    assert base.exists()
    assert (base / "pack.mcmeta").exists()

def test_pack_mcmeta_content(tmp_path: Path, monkeypatch: pytest.MonkeyPatch):
    monkeypatch.chdir(tmp_path)

    dp = Datapack("testpack", "desc", "1.20.1")
    dp.export()

    file = tmp_path / "export" / "testpack" / "pack.mcmeta"

    with open(file) as f:
        data = json.load(f)

    assert data["pack"]["description"] == "desc"
    assert data["pack"]["pack_format"] == 15

def test_overwrite_true(tmp_path, monkeypatch):
    monkeypatch.chdir(tmp_path)

    dp = Datapack("testpack", "desc", "1.20.1")

    dp.export()
    dp.export(overwrite=True)

    base = tmp_path / "export" / "testpack"

    assert base.exists()

def test_overwrite_false_creates_new_folder(tmp_path: Path, monkeypatch: pytest.MonkeyPatch):
    monkeypatch.chdir(tmp_path)

    dp = Datapack("testpack", "desc", "1.20.1")

    dp.export(overwrite=False)
    dp.export(overwrite=False)

    export_dir = tmp_path / "export"

    assert (export_dir / "testpack").exists()
    assert (export_dir / "testpack_1").exists()

def test_zip_export(tmp_path: Path, monkeypatch: pytest.MonkeyPatch):
    monkeypatch.chdir(tmp_path)

    dp = Datapack("testpack", "desc", "1.20.1")
    dp.export(zip=True)

    zip_file = tmp_path / "export" / "testpack.zip"

    assert zip_file.exists()

def test_icon_copy(tmp_path, monkeypatch):
    monkeypatch.chdir(tmp_path)

    icon = tmp_path / "icon.png"
    icon.write_bytes(b"fake image")

    dp = Datapack(
        "testpack",
        "desc",
        "1.20.1",
        relative_icon_path="icon.png"
    )

    dp.export()

    assert (tmp_path / "export" / "testpack" / "pack.png").exists()

def test_namespace_export_called(tmp_path, monkeypatch):
    monkeypatch.chdir(tmp_path)

    dp = Datapack("testpack", "desc", "1.20.1")

    ns = MagicMock()
    dp.add_namespaces(ns)

    dp.export()

    ns.export.assert_called_once()
