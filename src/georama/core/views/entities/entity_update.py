from django.apps import apps
from django.urls import reverse

from georama.core.menu import BreadCrumb
from georama.core.views.entities.entity_base import TypingHelperClass
from georama.core.views.generic.update import GeoramaUpdateView


class GeoramaEntityUpdateView(GeoramaUpdateView):
    model: TypingHelperClass
    entity_name: str

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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["delete_view_name"] = f"{self.model._meta.app_label}:{self.entity_name}-delete"
        context["permission_view_name"] = (
            f"{self.model._meta.app_label}:{self.entity_name}-permission-list"
        )
        context["perm_manage_permission"] = self.request.user.has_perm(
            self.model.perm_manage_permissions()
        )
        context["perm_delete"] = self.request.user.has_perm(self.model.perm_delete())
        return context
