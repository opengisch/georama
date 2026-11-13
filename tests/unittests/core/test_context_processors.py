import pytest
from django.test import RequestFactory

from georama.core.common.menu import MENU_ITEMS
from georama.core.context_processors import menu_items


class TestMenuItems:
    # every registered app is its own case, a new app is checked without touching the test
    @pytest.mark.parametrize("item", MENU_ITEMS, ids=lambda item: item.app_name)
    def test_request_without_user_keeps_the_public_items(self, item):
        # an error before the authentication middleware (e.g. a 400 for a host which is
        # not allowed) is rendered without any user
        request = RequestFactory().get("/")
        offered = menu_items(request)["menu_items"]
        if item.permissions:
            # the app asks for permissions, nobody holds them without a user
            assert item not in offered
        else:
            # the app is public, it stays in the menu
            assert item in offered
