from django.conf import settings

from georama.core.common.menu import MENU_ITEMS


def menu_items(request):
    # errors before the authentication middleware (e.g. a 400 for a host which is not
    # allowed) are rendered without a user, nobody holds a permission then
    user = getattr(request, "user", None)
    permitted_menu_items = []
    for item in MENU_ITEMS:
        if len(item.permissions) > 0:
            # we have permissions to check
            if user is not None and (
                user.is_superuser or any(user.has_perm(perm) for perm in item.permissions)
            ):
                permitted_menu_items.append(item)
        else:
            permitted_menu_items.append(item)
    return {"menu_items": permitted_menu_items}


def site_title(request):
    return {"site_title": settings.SITE_TITLE, "docs_url": settings.DOCUMENTATION_URL}
