# This file contains the ItemComponent class

from abc import abstractmethod, ABC, ABCMeta

class ItemComponents:
    """
    Item components.
    """

    def __init__(self, *components: ItemComponent | RemoveItemComponent) -> None:
        """
        Init new components for an item.

        Parameters
        ----------
        *components:
            Components to add.
        """

        self.config: dict = {}

        for component in components:
            if isinstance(component, ItemComponent):
                self.config[f"{component.TYPE}"] = component.to_value()
            elif isinstance(component, str):
                self.config[f"{component}"] = {}
            else:
                raise TypeError(f"component must be ItemComponent or RemoveItemComponent, got: {type(component)}")

    def __iadd__(self, component: ItemComponent | RemoveItemComponent) -> ItemComponents:

        if isinstance(component, ItemComponent):
            self.config[f"{component.TYPE}"] = component.to_value()
        elif isinstance(component, str):
            self.config[f"{component}"] = {}
        else:
            raise TypeError(f"component must be ItemComponent or RemoveItemComponent, got: {type(component)}")

        return self

type RemoveItemComponent = str

class ComponentMeta(ABCMeta):
    """
    ABCMeta class to allow class level __invert__.
    """

    def __invert__(cls) -> RemoveItemComponent:
        """
        Remove an ItemComponent.
        """

        return f"!{cls.TYPE}"

class ItemComponent(ABC, metaclass=ComponentMeta):
    """
    Item component.
    """

    TYPE: str

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)

        if "TYPE" not in cls.__dict__:
            raise TypeError(f"{cls.__name__} must define TYPE")

        if not isinstance(cls.TYPE, str):
            raise TypeError(f"{cls.__name__}.TYPE must be a string")

    def __init__(self) -> None:
        """
        New item component.
        """

        self.config: dict[str, str | bool]

    @abstractmethod
    def to_value(self) -> dict[str, str] | bool | dict[str, list[str] | str] | int | float | str | dict[str, int] | list[dict]:
        """
        Convert component to dictionary.
        """

