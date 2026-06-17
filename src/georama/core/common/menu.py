from dataclasses import dataclass, field


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
