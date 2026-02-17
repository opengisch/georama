from dataclasses import dataclass


@dataclass
class MenuItem:
    title: str
    app_name: str
    app_label: str
    app_index: str
    order: int = 100


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
class BreadCrumb:
    title: str
    view_name: str | None = None
