# This file contains the jukebox_playable component

from .components import ItemComponent

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from MCpypack.item.final import JukeboxSong

class JukeboxPlayable(ItemComponent):
    """
    Jukebox playable item component.
    """

    @property
    def TYPE(self) -> str:
        return "minecraft:jukebox_playable"

    def __init__(self, jukebox_playable: JukeboxSong) -> None:
        """
        Init jukebox_playable component.
        
        Parameters
        ----------
        jukebox_playable:
            One jukebox song to play when inserted into a jukebox.
        """

        super().__init__()

        self.jukebox_playable = jukebox_playable

    def to_value(self) -> str:
        return self.jukebox_playable.value
