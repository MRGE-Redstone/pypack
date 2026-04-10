# This file contains the bucket_entity_data component

from .components import ItemComponent

class BucketEntityData(ItemComponent):
    """
    Bucket entity data item component.
    NBT applied to an entity when placed from this bucket.
    """

    @property
    def TYPE(self) -> str:
        return "minecraft:bucket_entity_data"

    def __init__(self,
                 *,
                 no_ai: bool,
                 silent: bool,
                 no_gravity: bool,
                 glowing: bool,
                 invulnerable: bool,
                 age_locked: bool,
                 health: float,
                 age: int,
                 hunting_cooldown: int,
                 ) -> None:
        """
        Init bucket entity data item component.

        Parameters
        ----------
        no_ai:
            Turns into NoAI entity tag for all bucketable entities.
        silent:
            Turns into Silent entity tag for all bucketable entities.
        no_gravity:
            Turns into NoGravity entity tag for all bucketable entities.
        glowing:
            Turns into Glowing entity tag for all bucketable entities.
        invulnerable:
            Turns into Invulnerable entity tag for all bucketable entities.
        age_locked:
            Turns into AgeLocked entity tag for axolotls and tadpoles.
        health:
            Turns into Health entity tag for all bucketable entities.
        age:
            Turns into Age entity tag for axolotls and tadpoles.
        hunting_cooldown:
            Turns into the expiry time of the memory module has_hunting_cooldown for axolotls.
        """

        super().__init__()

        self.no_ai = no_ai
        self.silent = silent
        self.no_gravity = no_gravity
        self.glowing = glowing
        self.invulnerable = invulnerable
        self.age_locked = age_locked

        self.health = health
        self.age = age
        self.hunting_cooldown = hunting_cooldown

    def to_value(self) -> dict:
        return {
            "NoAI": self.no_ai,
            "Silent": self.silent,
            "NoGravity": self.no_gravity,
            "Glowing": self.glowing,
            "Invulnerable": self.invulnerable,
            "AgeLocked": self.age_locked,
            "Health": self.health,
            "Age": self.age,
            "HuntingCooldown": self.hunting_cooldown,
        }
