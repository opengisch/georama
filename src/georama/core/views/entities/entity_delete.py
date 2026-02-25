from django.apps import apps
from django.urls import reverse

from georama.core.entities.models import PublishedAs
from georama.core.menu import BreadCrumb
from georama.core.views.generic.delete import GeoramaDeleteView


class GeoramaEntityDeleteView(GeoramaDeleteView):
    model: PublishedAs
    entity_name: str

    def get_success_url(self):
        return reverse(f"{self.model._meta.app_label}:{self.entity_name}-list")

    def get_breadcrumbs(self):
        app_menu = apps.get_app_config(self.model._meta.app_label).app_menu()
        return [
            BreadCrumb(app_menu.title, reverse(f"{self.model._meta.app_label}:index")),
            BreadCrumb(
                self.model._meta.verbose_name_plural,
                reverse(f"{self.model._meta.app_label}:{self.entity_name}-list"),
            ),
            BreadCrumb(
                self.object.title or self.object.name,
                reverse(
                    f"{self.model._meta.app_label}:{self.entity_name}-detail",
                    kwargs={"pk": self.kwargs["pk"]},
                ),
            ),
        ]
