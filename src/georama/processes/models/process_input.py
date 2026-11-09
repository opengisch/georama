import uuid

from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from guardian.managers import GroupObjectPermissionManager, UserObjectPermissionManager
from guardian.models import GroupObjectPermissionBase, UserObjectPermissionBase
from qgis_server_light.interface.job.common.input import QslJobLayer
from qgis_server_light.interface.job.process.description import QslLayerKind, QslLayerMarker

from georama.core.common.managers import OrganisationalManager
from georama.integration.models import Datasource
from georama.processes.apps import central_app_label
from georama.processes.managers.process_input import ProcessInputManager


class ProcessInput(models.Model):
    ORGANISATION_FIELD_NAME = "datasource__project__organisation"

    PERMISSIONS = {
        "can_view": "use_as_process_input",
    }

    ACTION_MAP = {
        "grant": (True, [PERMISSIONS["can_view"]], "grant access"),
        "revoke": (False, list(PERMISSIONS.values()), "revoke access"),
    }

    DATASOURCE_TYPE_BY_LAYER_KIND = {
        QslLayerKind.VECTOR: "vector",
        QslLayerKind.RASTER: "raster",
    }

    class Meta:
        verbose_name = f"{_('Process input')}"
        verbose_name_plural = f"{_('Process inputs')}"
        permissions = [
            ("manage_object_permissions", "Can manage object permissions"),
            ("use_as_process_input", "Can use as process input"),
        ]
        constraints = [
            models.UniqueConstraint(
                fields=["datasource"],
                name="unique_process_input_per_datasource",
            ),
        ]

    objects = ProcessInputManager()

    id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, help_text=_("Identifier of the process input.")
    )

    public = models.BooleanField(default=False)

    datasource = models.ForeignKey(
        Datasource,
        related_name="process_inputs",
        related_query_name="process_inputs",
        on_delete=models.CASCADE,
        help_text=_("Datasource which is offered as layer input to processes."),
    )

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse(f"{central_app_label}:process-input-manager-detail", kwargs={"pk": self.pk})

    @property
    def identifier(self) -> str:
        return str(self.id)

    @property
    def title(self) -> str:
        return self.datasource.name

    def to_qsl_job_layer(self) -> QslJobLayer:
        return self.datasource.to_qsl_job_layer(identifier=self.identifier, name=self.title)

    def fits(self, marker: QslLayerMarker) -> bool:
        if self.datasource.type != self.DATASOURCE_TYPE_BY_LAYER_KIND[marker.kind]:
            return False
        if marker.kind is QslLayerKind.VECTOR:
            return self.datasource.vector.geometry_type_simple in marker.geometry_types
        return True


class UserManager(UserObjectPermissionManager, OrganisationalManager): ...


class GroupManager(GroupObjectPermissionManager, OrganisationalManager): ...


class ProcessInputUserObjectPermission(UserObjectPermissionBase):
    ORGANISATION_FIELD_NAME = "content_object__datasource__project__organisation"
    content_object = models.ForeignKey(
        ProcessInput, on_delete=models.CASCADE, related_name="user_object_permissions"
    )
    time_created = models.DateTimeField(auto_now_add=True)

    objects = UserManager()


class ProcessInputGroupObjectPermission(GroupObjectPermissionBase):
    ORGANISATION_FIELD_NAME = "content_object__datasource__project__organisation"
    content_object = models.ForeignKey(
        ProcessInput, on_delete=models.CASCADE, related_name="group_object_permissions"
    )
    time_created = models.DateTimeField(auto_now_add=True)

    objects = GroupManager()
