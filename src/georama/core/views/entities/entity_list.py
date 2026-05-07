from django.apps import apps
from django.urls import reverse
from django.utils.translation import gettext as _

from georama.core.entities.models import PublishedAs
from georama.core.menu import BreadCrumb
from georama.core.views.generic.list import GeoramaListView


class GeoramaEntityListView(GeoramaListView):
    model: PublishedAs
    template_name = "core/entity_list.html"
    entity_name: str

    def get_breadcrumbs(self):
        app_menu = apps.get_app_config(self.model._meta.app_label).app_menu()
        return [
            BreadCrumb(app_menu.title, reverse(f"{app_menu.app_label}:index")),
            BreadCrumb(self.model._meta.verbose_name_plural),
        ]

    def get_breadcrumb_action(self):
        return {
            "breadcrumb_action_url": (
                f"{self.model._meta.app_label}:{self.entity_name}-add-list"
            ),
            "breadcrumb_action_icon": "fa fa-circle-plus",
            "breadcrumb_action_title": _("Publish"),
            "breadcrumb_action_tooltip": _("Publish a new item"),
        }

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.user.has_perm(self.model.perm_add()):
            context.update(self.get_breadcrumb_action())
        context["model_perm_manage"] = self.request.user.has_perm(
            f"{self.model._meta.app_label}.can_manage_object_permissions"
        )
        context["model_perm_view"] = self.request.user.has_perm(
            f"{self.model._meta.app_label}.view_{self.model._meta.model_name}"
        )
        context["model_perm_add"] = self.request.user.has_perm(
            f"{self.model._meta.app_label}.add_{self.model._meta.model_name}"
        )
        context["model_perm_change"] = self.request.user.has_perm(
            f"{self.model._meta.app_label}.change_{self.model._meta.model_name}"
        )
        context["model_perm_delete"] = self.request.user.has_perm(
            f"{self.model._meta.app_label}.delete_{self.model._meta.model_name}"
        )
        view_name_discriminator = f"{self.model._meta.app_label}:{self.entity_name}"
        context["view_name_detail"] = f"{view_name_discriminator}-detail"
        context["view_name_update"] = f"{view_name_discriminator}-update"
        context["view_name_permission_list"] = f"{view_name_discriminator}-permission-list"
        context["view_name_delete"] = f"{view_name_discriminator}-delete"
        return context
