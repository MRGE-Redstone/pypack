# This file contains the swing_animation component

from .components import ItemComponent
from MCpypack import utils

class SwingAnimation(ItemComponent):
    """
    Swing animation item component.
    Allows modification of the swinging animation.
    """

    TYPE = "minecraft:swing_animation"

    @property
    def duration(self) -> int:
        return self._duration

    @duration.setter
    def duration(self, value: int) -> None:
        if not isinstance(value, int):
            raise TypeError("duration must be an integer, got: type(duration) = {type(duration)}")

        if not 0 < value:
            raise ValueError(f"duration must be greater than 0, got: duration {value}")

        self._duration = value

    def __init__(self,
                 *,
                 animation_type: utils.SwingAnimation = utils.SwingAnimation.WHACK,
                 duration: int = 6,
                 ) -> None:
        """
        Init a swing_animation item component.

        Parameters
        ----------
        type:
            The type of swinging animation. Can be none, whack, stab. Defaults to whack.
        duration:
            A positive integer that determines the animation's duration in ticks. Defaults to 6.
        """
        super().__init__()

        self.animation_type: str = animation_type.value
        self.duration = duration

    def to_value(self) -> dict:
        return {
            "type": self.animation_type,
            "duration": self.duration,
        }
