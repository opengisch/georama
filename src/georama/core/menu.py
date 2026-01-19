from dataclasses import dataclass


@dataclass
class MenuItem:
    label: str
    url_name: str
    order: int = 100


MENU_ITEMS: list[MenuItem] = []


def register_menu_item(item: MenuItem):
    MENU_ITEMS.append(item)
    MENU_ITEMS.sort(key=lambda i: i.order)
