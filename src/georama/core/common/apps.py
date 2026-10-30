from abc import ABC

from django.apps import AppConfig

from georama.core.common.menu import MenuItem, register_menu_item


class GeoramaAbstractConfig(AppConfig, ABC):
    """Represents a configuration which also provides a menu item which is added in
    the base templates top menu bar.

    Attributes:
        label: The label of the app. This is django mechanic and only documented here,
            since the menu item relies on it.
        name: The unique name of the app. This is django mechanic and only documented
            here, since the menu item relies on it.
        menu_order: This defines an ordering index which is used when rendering all
            loaded menu items in the base templates top menu bar.
        app_index_page: The view name which should be shown when someone clicks
            on the entry in the base templates top menu bar. It defaults to:
                e.g. <label>:index when it's not overwritten so, e.g. core:index for the
                app core.
    """

    label: str = "abstract_base_class"
    name: str = "georama.abstract_base_class"
    menu_order: int = 10
    app_index_page: str | None = None

    @classmethod
    def get_simple_appname(cls) -> str | None:
        if cls.name is not None:
            return cls.name.split(".")[-1]
        else:
            return None

    def app_menu(self):
        me = MenuItem(
            title=self.verbose_name,
            app_label=self.label,
            app_name=self.name,
            app_index=self.app_index_page or f"{self.label}:index",
            app_description=self.description,
            order=self.menu_order,
            permissions=self.app_permissions(),
        )
        return me

    def app_permissions(self):
        return []

    def ready(self):
        register_menu_item(self.app_menu())
