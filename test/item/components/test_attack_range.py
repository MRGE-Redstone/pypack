import pytest

from MCpypack.item.components import AttackRange

def test_correct_type():
    assert AttackRange().TYPE == "minecraft:attack_range"

def test_default_arguments():
    ar = AttackRange()

    assert ar.to_value() == {
        "min_reach": 0.0,
        "max_reach": 3.0,
        "min_creative_reach": 0.0,
        "max_creative_reach": 5.0,
        "hitbox_margin": 0.3,
        "mob_factor": 1.0,
    }

@pytest.mark.parametrize("min_reach", [
    (0.0),
    (64.0),
    (31.7),
])
def test_min_reach(min_reach: float):
    ar = AttackRange(min_reach=min_reach)

    assert ar.min_reach == min_reach

@pytest.mark.parametrize("min_reach", [
    (-0.1),
    (-5),
    (64.1),
    (120),
])
def test_min_reach_invalid(min_reach: float):
    with pytest.raises(ValueError):
        AttackRange(min_reach=min_reach)

@pytest.mark.parametrize("max_reach", [
    (0.0),
    (64.0),
    (31.7),
])
def test_max_reach(max_reach: float):
    ar = AttackRange(max_reach=max_reach)

    assert ar.max_reach == max_reach

@pytest.mark.parametrize("max_reach", [
    (-0.1),
    (-5),
    (64.1),
    (120),
])
def test_max_reach_invalid(max_reach: float):
    with pytest.raises(ValueError):
        AttackRange(max_reach=max_reach)


@pytest.mark.parametrize("min_creative_reach", [
    (0.0),
    (64.0),
    (31.7),
])
def test_min_creative_reach(min_creative_reach: float):
    ar = AttackRange(min_creative_reach=min_creative_reach)

    assert ar.min_creative_reach == min_creative_reach

@pytest.mark.parametrize("min_creative_reach", [
    (-0.1),
    (-5),
    (64.1),
    (120),
])
def test_min_creative_reach_invalid(min_creative_reach: float):
    with pytest.raises(ValueError):
        AttackRange(min_creative_reach=min_creative_reach)

@pytest.mark.parametrize("max_creative_reach", [
    (0.0),
    (64.0),
    (31.7),
])
def test_max_creative_reach(max_creative_reach: float):
    ar = AttackRange(max_creative_reach=max_creative_reach)

    assert ar.max_creative_reach == max_creative_reach

@pytest.mark.parametrize("max_creative_reach", [
    (-0.1),
    (-5),
    (64.1),
    (120),
])
def test_max_creative_reach_invalid(max_creative_reach: float):
    with pytest.raises(ValueError):
        AttackRange(max_creative_reach=max_creative_reach)


@pytest.mark.parametrize("hitbox_margin", [
    (0.0),
    (1.0),
    (0.5),
])
def test_hitbox_margin(hitbox_margin: float):
    ar = AttackRange(hitbox_margin=hitbox_margin)

    assert ar.hitbox_margin == hitbox_margin

@pytest.mark.parametrize("hitbox_margin", [
    (-0.1),
    (1.1),
    (69.0),
])
def test_hitbox_margin_invalid(hitbox_margin: float):
    with pytest.raises(ValueError):
        AttackRange(hitbox_margin=hitbox_margin)

@pytest.mark.parametrize("mob_factor", [
    (0.0),
    (2.0),
    (1.5),
])
def test_mob_factor(mob_factor: float):
    ar = AttackRange(mob_factor=mob_factor)

    assert ar.mob_factor == mob_factor

@pytest.mark.parametrize("mob_factor", [
    (-0.1),
    (2.1),
    (69.0),
])
def test_mob_factor_invalid(mob_factor: float):
    with pytest.raises(ValueError):
        AttackRange(mob_factor=mob_factor)

def test_custom_values():
    ar = AttackRange(
        min_reach=10.0,
        max_reach=15.0,
        min_creative_reach=22.0,
        max_creative_reach=64.0,
        hitbox_margin=0.5,
        mob_factor=1.7,
    )

    assert ar.to_value() == {
        "min_reach": 10.0,
        "max_reach": 15.0,
        "min_creative_reach": 22.0,
        "max_creative_reach": 64.0,
        "hitbox_margin": 0.5,
        "mob_factor": 1.7,
    }
