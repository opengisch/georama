from abc import ABC

from django.apps import AppConfig

from georama.core.common.menu import MenuItem, register_menu_item


class GeoramaAbstractConfig(AppConfig, ABC):
    label: str = "abstract_base_class"
    name: str = "georama.abstract_base_class"
    menu_order: int = 10

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
            app_index=f"{self.label}:index",
            app_description=self.description,
            order=self.menu_order,
            permissions=self.app_permissions(),
        )
        print(me)
        return me

    def app_permissions(self):
        return []

    def ready(self):
        register_menu_item(self.app_menu())
