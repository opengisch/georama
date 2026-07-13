from dataclasses import dataclass, field
from enum import StrEnum


@dataclass
class MenuItem:
    title: str
    app_name: str
    app_label: str
    app_index: str
    app_description: str
    order: int = 100
    permissions: list[str] = field(default_factory=list)


MENU_ITEMS: list[MenuItem] = []


def register_menu_item(item: MenuItem):
    if get_menu_item_by_app_name(item.app_name) is not None:
        raise LookupError(f"Menu item was already registered. {item}")
    MENU_ITEMS.append(item)
    MENU_ITEMS.sort(key=lambda i: i.order)


def get_menu_item_by_app_name(app_name: str) -> MenuItem | None:
    for item in MENU_ITEMS:
        if item.app_name == app_name:
            return item
    return None


@dataclass
class Breadcrumb:
    title: str
    view_name: str | None = None


class ActionType(StrEnum):
    """The type of breadcrumb action, meaning how the action will be rendered. In the
    resulting HTML.

    Attributes:
        LINKED: The breadcrumb action is a link which actually reloads the full page
            with the new content.
        EMBEDDED: The breadcrumb action will be used to load partial content and
            show it in a modal layover on the same page. This is useful where items
            from an existing list should be selected (e.g. publishing workflow).
    """

    LINKED = "linked"
    EMBEDDED = "embedded"


@dataclass
class BreadcrumbAction:
    """Represents the configurable part of the actionable breadcrumb item.

    Attributes:
        url: The target of the action, when it's clicked on.
        tooltip: A helpful and translated text which is shown when the user hovers over
            the item with the mouse.
        title: The text which will be shown in the rendered button (should be translated
            as well).
        type: See docs of `ActionType`
        icon: Icon classes which are then shown next to the title. If not set, only the
            title will be shown.
    """

    url: str
    tooltip: str
    hint: str
    title: str
    type: ActionType
    icon: str | None = field(default=None)
