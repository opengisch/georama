from georama.core.common.menu import MENU_ITEMS


def menu_items(request):
    permitted_menu_items = []
    for item in MENU_ITEMS:
        if len(item.permissions) > 0 and not request.user.is_superuser:
            # we have permissions to check
            if request.user.has_perms(item.permissions):
                permitted_menu_items.append(item)
        else:
            permitted_menu_items.append(item)
    return {"menu_items": permitted_menu_items}
