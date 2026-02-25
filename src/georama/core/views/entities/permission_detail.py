from django.apps import apps
from django.contrib.auth.models import Permission
from django.urls import reverse

from georama.core.entities.models import PublishedAs
from georama.core.menu import BreadCrumb
from georama.core.services.permission import DBService
from georama.core.views.generic.detail import GeoramaDetailView


class GeoramaPermissionDetailView(GeoramaDetailView):
    model = Permission
    model_entity: PublishedAs
    template_name = "core/permission.html"
    entity_name: str

    def get_object(self, queryset=None):
        object_pk = self.kwargs.get("pk")
        dbs_permission = DBService(self.model_entity, self.model_entity._meta.app_label)
        return dbs_permission.get_permission_lookup(object_pk)

    def get_breadcrumbs(self):
        app_menu = apps.get_app_config(self.model_entity._meta.app_label).app_menu()
        related_object = self.model_entity.objects.get(pk=self.kwargs.get("pk"))
        return [
            BreadCrumb(app_menu.title, reverse(f"{app_menu.app_label}:index")),
            BreadCrumb(
                self.model_entity._meta.verbose_name_plural,
                reverse(f"{app_menu.app_label}:{self.entity_name}-list"),
            ),
            BreadCrumb(
                related_object.title or related_object.name,
                reverse(
                    f"{app_menu.app_label}:{self.entity_name}-detail",
                    kwargs={"pk": self.kwargs.get("pk")},
                ),
            ),
            BreadCrumb(self.model._meta.verbose_name),
        ]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["add_user_url"] = reverse(
            f"{self.model_entity._meta.app_label}:{self.entity_name}-permission-user-list",
            kwargs={"pk": self.kwargs.get("pk")},
        )
        context["add_group_url"] = reverse(
            f"{self.model_entity._meta.app_label}:{self.entity_name}-permission-group-list",
            kwargs={"pk": self.kwargs.get("pk")},
        )
        return context
