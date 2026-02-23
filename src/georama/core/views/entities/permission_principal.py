from django.apps import apps
from django.contrib.auth.models import Permission
from django.db import models
from django.urls import reverse
from django.utils.translation import gettext as _

from georama.core.entities.models import PublishedAs
from georama.core.menu import BreadCrumb
from georama.core.services.permission import DBService
from georama.core.views.generic.list import GeoramaListView


class GeoramaPrincipalListView(GeoramaListView):
    model: models.Model
    model_entity: PublishedAs
    template_name: str
    entity_name: str

    def get_breadcrumbs(self):
        app_menu = apps.get_app_config(self.model_entity._meta.app_label).app_menu()
        related_object = self.model_entity.objects.get(pk=self.kwargs.get("pk"))
        return [
            BreadCrumb(app_menu.title, reverse(f"{app_menu.app_label}:index")),
            BreadCrumb(
                _("Manage Layers"), reverse(f"{app_menu.app_label}:{self.entity_name}-list")
            ),
            BreadCrumb(
                related_object.title or related_object.name,
                reverse(
                    f"{app_menu.app_label}:{self.entity_name}-detail",
                    kwargs={"pk": self.kwargs.get("pk")},
                ),
            ),
            BreadCrumb(
                Permission._meta.verbose_name,
                reverse(
                    f"{app_menu.app_label}:{self.entity_name}-permission-list",
                    kwargs={"pk": self.kwargs.get("pk")},
                ),
            ),
            BreadCrumb(self.model._meta.verbose_name),
        ]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        dbs_permission = DBService(self.model_entity, self.model_entity._meta.app_label)
        context["read_permission_id"] = (
            dbs_permission.get_by_object_pk(self.kwargs.get("pk"))
            .filter(codename__icontains="read")
            .get()
            .pk
        )
        context["success_url"] = reverse(
            f"{self.model_entity._meta.app_label}:{self.entity_name}-permission-list",
            kwargs={"pk": self.kwargs.get("pk")},
        )
        return context
