import uuid

from django.conf import settings
from django.db import models
from django.templatetags.static import static
from django.urls import reverse
from django.utils.translation import gettext as _
from guardian.managers import GroupObjectPermissionManager, UserObjectPermissionManager
from guardian.models import GroupObjectPermissionBase, UserObjectPermissionBase
from qgis_server_light.interface.common import BBox
from qgis_server_light.interface.exporter.extract import Config, DataSet, TreeGroup
from xsdata.formats.dataclass.parsers import DictDecoder
from xsdata.formats.dataclass.parsers.config import ParserConfig
from xsdata.formats.dataclass.serializers import DictEncoder

from georama.core.common.managers import OrganisationalManager
from georama.integration.models import Datasource, Project
from georama.maps.apps import central_app_label
from georama.webgis.interfaces.geomapfish.themes_json_2_8.dataclasses import (
    LayerGroup as GGLayerGroup,
)
from georama.webgis.interfaces.geomapfish.themes_json_2_8.dataclasses import MetaData as GGMetaData
from georama.webgis.interfaces.geomapfish.themes_json_2_8.dataclasses import Theme as GGTheme
from georama.webgis.managers.theme import ThemeManager
from georama.webgis.models.metadata import Metadata
from georama.webgis.models.wms_layer import WmsLayer


class Theme(models.Model):
    ORGANISATION_FIELD_NAME = "project__organisation"

    class Meta:
        ordering = ["ordering"]
        verbose_name = _("Theme")
        verbose_name_plural = _("Themes")
        permissions = [
            # permission which is used on the model
            ("manage_object_permissions", "Can manage object permissions"),
            # permission which is used for the object permission evaluation on the published themes
            ("view_published_theme", "Can view published theme"),
        ]

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    project = models.ForeignKey(
        Project,
        related_name="themes",
        on_delete=models.CASCADE,
    )
    metadata = models.ForeignKey(
        Metadata,
        related_name="themes",
        on_delete=models.CASCADE,
    )
    public = models.BooleanField(default=False)
    ordering = models.IntegerField()
    location = models.JSONField(null=True)
    zoom = models.IntegerField(null=True)
    theme_json = models.JSONField()

    objects = ThemeManager()

    @property
    def icon_default(self):
        return static("webgis/images/georama-logo-geogirafe.svg")

    def __str__(self):
        return f"{self.metadata.title} ({self.id})"

    def as_dataclass(self) -> GGTheme:
        config = ParserConfig(fail_on_unknown_properties=False)
        return DictDecoder(config).decode(self.theme_json, GGTheme)

    def set_from_dataclass(self, theme: GGTheme):
        self.theme_json = DictEncoder().encode(theme)

    def assign_theme_public_to_all_theme_layers(self):
        WmsLayer.objects.filter(theme=self).update(public=self.public)

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        if self.metadata.title is None:
            self.metadata.title = self.project.name

        self.assign_theme_public_to_all_theme_layers()

        super().save(
            force_insert=force_insert,
            force_update=force_update,
            using=using,
            update_fields=update_fields,
        )

    def get_absolute_url(self):
        return reverse(f"{central_app_label}:theme-detail", kwargs={"pk": self.pk})

    @property
    def endpoint_url(self):
        return (
            f"{settings.WEBGISURL}?themes={self.metadata.title}&map_zoom="
            f"{self.zoom}&map_x={self.location[0]}&map_y={self.location[1]}"
        )

    @staticmethod
    def extend_bbox(bbox: BBox, bbox_extension: BBox):
        if bbox_extension.x_min < bbox.x_min or bbox.x_min == 0:
            bbox.x_min = bbox_extension.x_min
        if bbox_extension.y_min < bbox.y_min or bbox.y_min == 0:
            bbox.y_min = bbox_extension.y_min
        if bbox_extension.x_max > bbox.x_max or bbox.x_max == 0:
            bbox.x_max = bbox_extension.x_max
        if bbox_extension.y_max > bbox.y_max or bbox.y_max == 0:
            bbox.y_max = bbox_extension.y_max

    @staticmethod
    def handle_dataset(
        dataset: DataSet, config: Config, gg_children: list[GGLayerGroup], bbox: BBox
    ):
        db = Datasource()  # noqa: F841
        if dataset.bbox is not None:
            Theme.extend_bbox(bbox, dataset.bbox)

    @staticmethod
    def unwrap_group(group: TreeGroup, config: Config, gg_children: list[GGLayerGroup], bbox: BBox):
        for child in group.children:
            tree_match = config.tree.find_by_name(child)
            if tree_match:
                # its a group again
                Theme.unwrap_group(tree_match, config, gg_children, bbox)
            else:
                ds = config.datasets.find_dataset_by_id(child)
                if ds:
                    Theme.handle_dataset(ds, config, gg_children, bbox)
                else:
                    raise LookupError(f"Dataset with id {child} was not found in config!")

    def theme_json_from_project_config(self):
        project_config = self.project.config_as_dataclass
        bbox = BBox(0.0, 0.0, 0.0, 0.0)
        children = []
        Theme.unwrap_group(project_config.tree.root, project_config, children, bbox)
        theme_json = GGTheme(  # noqa: F841
            id=self.id,
            name=project_config.project.name,
            icon=self.icon_default,
            metadata=GGMetaData(),
            children=[],
            zoom=4,
        )


class UserManager(UserObjectPermissionManager, OrganisationalManager): ...


class GroupManager(GroupObjectPermissionManager, OrganisationalManager): ...


class ThemeUserObjectPermission(UserObjectPermissionBase):
    ORGANISATION_FIELD_NAME = "content_object__project__organisation"
    content_object = models.ForeignKey(
        Theme, on_delete=models.CASCADE, related_name="user_object_permissions"
    )
    time_created = models.DateTimeField(auto_now_add=True)

    objects = UserManager()


class ThemeGroupObjectPermission(GroupObjectPermissionBase):
    ORGANISATION_FIELD_NAME = "content_object__project__organisation"
    content_object = models.ForeignKey(
        Theme, on_delete=models.CASCADE, related_name="group_object_permissions"
    )
    time_created = models.DateTimeField(auto_now_add=True)

    objects = GroupManager()
