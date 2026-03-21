# This file contains the Time class
# It also contains other time related classes

from dataclasses import dataclass
from typing import TypeAlias

# Real life time classes
@dataclass
class Milliseconds:
    value: int

@dataclass
class Seconds:
    value: int

@dataclass
class Minutes:
    value: int

@dataclass
class Hours:
    value: int

RealLifeTime: TypeAlias = Milliseconds | Seconds | Minutes | Hours

# Minecraft time class
@dataclass
class Ticks:
    value: int

MinecraftTime: TypeAlias = Ticks


class Time:
    """
    Represents time.
    Can be initialized with multiple real-life time units.
    """

    def __init__(self, *rlTimes: RealLifeTime) -> None:
        """
        Initialize time with real-life time values.

        Parameters
        ----------
        *rlTimes: RealLifeTime
            Real-life time units (Milliseconds, Seconds, Minutes, Hours)
        """

        self.milliseconds: Milliseconds = Milliseconds(0)
        self.seconds: Seconds = Seconds(0)
        self.minutes: Minutes = Minutes(0)
        self.hours: Hours = Hours(0)

        for t in rlTimes:
            match t:
                case Milliseconds():
                    self.milliseconds.value += t.value
                case Seconds():
                    self.seconds.value += t.value
                case Minutes():
                    self.minutes.value += t.value
                case Hours():
                    self.hours.value += t.value
                case _:
                    raise ValueError(f"Unsupported time unit: {t}")

    @property
    def ticks(self) -> Ticks:
        """
        Return time as Minecraft ticks.
        """

        return Ticks(
            int(self.milliseconds.value /1000 *20)
            + (self.seconds.value *20)
            + (self.minutes.value *60 *20)
            + (self.hours.value *3600 *20)
        )
