from django.apps import apps
from django.db.models import Model
from django.urls import reverse
from django.utils.translation import gettext as _

from georama.core.entities.models import PublishedAs
from georama.core.menu import BreadCrumb
from georama.core.views.generic.list import GeoramaListView


class GeoramaEntityPublishListView(GeoramaListView):
    model: Model
    model_publish: PublishedAs
    template_name = "core/entity_publish_list.html"
    entity_name: str

    def get_breadcrumbs(self):
        app_menu = apps.get_app_config(self.model_publish._meta.app_label).app_menu()
        return [
            BreadCrumb(app_menu.title, reverse(f"{self.model_publish._meta.app_label}:index")),
            BreadCrumb(
                self.model_publish._meta.verbose_name_plural,
                reverse(f"{self.model_publish._meta.app_label}:{self.entity_name}-list"),
            ),
            BreadCrumb(_("Publish")),
        ]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["view_name_add"] = (
            f"{self.model_publish._meta.app_label}:{self.entity_name}-add"
        )
        return context
