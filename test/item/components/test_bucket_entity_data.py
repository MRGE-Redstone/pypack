import pytest

from MCpypack.item.components import BucketEntityData

def test_correct_type():
    bed = BucketEntityData(
        no_ai=True,
        silent=True,
        no_gravity=True,
        glowing=True,
        invulnerable=True,
        age_locked=True,
        health=5.0,
        age=1,
        hunting_cooldown=1,
    )

    assert bed.TYPE == "minecraft:bucket_entity_data"

def test_requires_kwargs():
    with pytest.raises(TypeError):
        BucketEntityData(
            True, 
            True,
            True,
            True,
            True,
            True,
            5.0,
            1,
            1,
        )

def test_to_value():
    bed = BucketEntityData(
        no_ai=True,
        silent=True,
        no_gravity=True,
        glowing=True,
        invulnerable=True,
        age_locked=True,
        health=5.0,
        age=1,
        hunting_cooldown=1,
    )

    assert bed.to_value() == {
        "NoAI": True,
        "Silent": True,
        "NoGravity": True,
        "Glowing": True,
        "Invulnerable": True,
        "AgeLocked": True,
        "Health": 5.0,
        "Age": 1,
        "HuntingCooldown":1,
    }
