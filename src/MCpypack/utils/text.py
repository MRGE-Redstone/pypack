# This file contains classes for the Minecraft text component.
# It represents a Minecraft text.
# The text component format is used for rich-text formatting.
# See more on https://minecraft.wiki/w/Text_component_format

from MCpypack.utils import TextColor, HexColor

class Formatting:
    """
    Class for text formatting.
    """

    @property
    def color(self) -> HexColor | TextColor:
        return self._color

    @color.setter
    def color(self, value: HexColor | TextColor) -> None:
        if not isinstance(value, (HexColor, TextColor)):
            raise ValueError(f"color must be of type HexColor | TextColor, got: {type(value)}")

        self._color = value

    @property
    def bold(self) -> bool:
        return self._bold

    @bold.setter
    def bold(self, value: bool) -> None:
        if not isinstance(value, bool):
            raise ValueError(f"bold must be of type bool, got: {type(value)}")

        self._bold = value

    @property
    def italic(self) -> bool:
        return self._italic

    @italic.setter
    def italic(self, value: bool) -> None:
        if not isinstance(value, bool):
            raise ValueError(f"italic must be of type bool, got: {type(value)}")

        self._italic = value

    @property
    def underlined(self) -> bool:
        return self._underlined

    @underlined.setter
    def underlined(self, value: bool) -> None:
        if not isinstance(value, bool):
            raise ValueError(f"underlined must be of type bool, got: {type(value)}")

        self._underlined = value

    @property
    def strikethrough(self) -> bool:
        return self._strikethrough

    @strikethrough.setter
    def strikethrough(self, value: bool) -> None:
        if not isinstance(value, bool):
            raise ValueError(f"strikethrough must be of type bool, got: {type(value)}")

        self._strikethrough = value

    @property
    def obfuscated(self) -> bool:
        return self._obfuscated

    @obfuscated.setter
    def obfuscated(self, value: bool) -> None:
        if not isinstance(value, bool):
            raise ValueError(f"obfuscated must be of type bool, got: {type(value)}")

        self._obfuscated = value

    @property
    def shadow_color(self) -> int:
        return self._shadow_color

    @shadow_color.setter
    def shadow_color(self, value: int) -> None:
        if not isinstance(value, int):
            raise ValueError(f"shadow_color must be of type int, got: {type(value)}")

        if value < 0:
            raise ValueError(f"shadow_color must be at least 0, got: {value}")

        self._shadow_color = value

    def __init__(self,
                 *,
                 color: HexColor | TextColor,
                 bold: bool = False,
                 italic: bool = False,
                 underlined: bool = False,
                 strikethrough: bool = False,
                 obfuscated: bool = False,
                 shadow_color: int | None,
                 ) -> None:
        """
        Init text formatting object.

        Parameters
        ----------
        color:
            Color the text should have.
        bold:
            Whether the text should be bold.
        italic:
            Whether the should be italic.
        underlined:
            Whether the text should be underlined.
        strikethrough:
            Whether the text should be strikethrough.
        obfuscated:
            Whether the text should be obfuscated.
        shadow_color:
            The color and opacity of the shadow. If omitted, the shadow is 25% the brightness of the text color and 100% the opacity.
        """

        self.color = color
        self.bold = bold
        self.italic = italic
        self.underlined = underlined
        self.strikethrough = strikethrough
        self.obfuscated = obfuscated
        if shadow_color is not None:
            self.shadow_color = shadow_color

    def to_dict(self) -> dict[str, str | bool | int]:
        result: dict[str, str | bool | int] = {}

        if isinstance(self.color, TextColor):
            result["color"] = self.color.value
        elif isinstance(self.color, HexColor):
            result["color"] = self.color.color

        result["bold"] = self.bold
        result["italic"] = self.italic
        result["underlined"] = self.underlined
        result["strikethrough"] = self.strikethrough
        result["obfuscated"] = self.obfuscated

        if self.shadow_color is not None:
            result["shadow_color"] = self.shadow_color

        return result

class PlainText:
    """
    Class representing texts components of the type 'text'.
    """

    @property
    def text(self) -> str:
        return self._text

    @text.setter
    def text(self, value: str) -> None:
        if not isinstance(value, str):
            raise ValueError(f"text must be of type str, got: {type(value)}")

        self._text = value

    @property
    def formatting(self) -> Formatting | None:
        return self._formatting

    @formatting.setter
    def formatting(self, value: Formatting | None) -> None:
        if not isinstance(value, (Formatting, type(None))):
            raise ValueError(f"formatting must be of type Formatting or None, got: {type(value)}")

        self._formatting = value

    def __init__(self,
                 text: str,
                 *,
                 formatting: Formatting | None = None
                 ) -> None:
        """
        Init a PlainText.

        Parameters
        ----------
        text:
            Text which should be displayed.
        formatting:
            Formatting for the text.
            Optional.
        """

        self.text = text

        self.formatting = formatting

    def to_dict(self) -> dict[str, str | bool | int]:
        result: dict[str, str | bool | int] = {}

        result["type"] = "text"
        result["text"] = self.text
        if self.formatting is not None:
            result.update(self.formatting.to_dict())

        return result
