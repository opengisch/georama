from georama.core.menu import MENU_ITEMS


def menu_items(request):
    # TODO RU: Check permissions of menu item
    return {"menu_items": MENU_ITEMS}
