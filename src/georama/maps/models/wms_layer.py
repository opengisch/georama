import base64
import json
import logging
import uuid
from dataclasses import fields
from pathlib import Path

from django.db import models
from django.templatetags.static import static
from django.urls import reverse
from django.utils.http import urlencode
from django.utils.translation import gettext_lazy as _
from guardian.managers import GroupObjectPermissionManager, UserObjectPermissionManager
from guardian.models import GroupObjectPermissionBase, UserObjectPermissionBase
from osgeo import osr as osgeo_osr
from qgis_server_light.interface.common import BBox
from qgis_server_light.interface.job.common.input import QslJobLayer

from georama.core.common.managers import OrganisationalManager
from georama.integration.models import Datasource
from georama.maps.interfaces.georama.requests import (
    GetMapRequestParams,
    RequestType,
    ServiceType,
    Version,
)
from georama.maps.managers.wms_layer import WmsLayerManager
from georama.maps.models.metadata import Metadata

LOGGER = logging.getLogger(__name__)


class WmsLayerAbstract(models.Model):
    class Meta:
        abstract = True

    id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, help_text=_("Identifier of the wms layer.")
    )

    extent_buffer = models.FloatField(
        default=0.0,
        help_text=_("Extent buffer size of the layer"),
    )
    queryable = models.BooleanField(
        default=True,
        help_text=_("Whether GetFeature requests are allowed on this layer."),
    )

    extent = models.CharField(
        max_length=1000,
        null=True,
        blank=True,
        help_text=_("Extent of the layer in its stored CRS."),
    )
    extent_wgs84 = models.CharField(
        max_length=1000,
        null=True,
        blank=True,
        help_text=_("Extent of the layer in WGS84 CRS."),
    )
    preview = models.BinaryField(
        null=True,
        blank=True,
        help_text=_("Preview image of the layer."),
    )
    min_resolution_hint = models.FloatField(
        default=0.0,
        help_text=_("Below this resolution the layer won't be drawn."),
    )
    max_resolution_hint = models.FloatField(
        default=999999999.0,
        help_text=_("Above this scale the layer won't be drawn."),
    )

    preview_dimensions: tuple[int, int] = (250, 250)
    preview_dimensions_new_tab: tuple[int, int] = (1500, 1500)
    crs_transform_to_wgs84 = None

    @property
    def identifier(self):
        return str(self.id)

    @property
    def get_metadata(self) -> Metadata:
        raise NotImplementedError()

    @property
    def get_datasource(self) -> Datasource:
        raise NotImplementedError()

    @property
    def extent_in_axis_order(self) -> BBox:
        """The extent in the axis order of its crs, as WMS 1.3.0 expects it for BBOX and
        BoundingBox (e.g. lat/lon for EPSG:4326). The stored extent is always x/y as QSL
        delivers it.
        """
        extent = BBox.from_string(self.extent)
        if not self.get_datasource.crs_to_qsl.axis_inverted:
            return extent
        return BBox(
            x_min=extent.y_min,
            y_min=extent.x_min,
            z_min=extent.z_min,
            x_max=extent.y_max,
            y_max=extent.x_max,
            z_max=extent.z_max,
        )

    @property
    def queryable_type(self) -> bool:
        return self.get_datasource.type in ["vector"]

    @property
    def is_queryable(self) -> bool:
        # Currently we do allow querying on Vectordatasources only
        if self.queryable_type:
            return self.queryable
        else:
            return False

    @property
    def create_wms_url_params(self) -> str:
        params = GetMapRequestParams(
            SERVICE=ServiceType.wms.value,
            REQUEST=RequestType.get_map.value,
            VERSION=Version.v_1_3_0.value,
            LAYERS=",".join([self.identifier]),
            BBOX=self.extent_in_axis_order.to_string(),
            CRS=self.get_datasource.crs_to_qsl.auth_id,
            WIDTH=self.preview_dimensions_new_tab[0],
            HEIGHT=self.preview_dimensions_new_tab[1],
            FORMAT="image/png",
            TRANSPARENT=True,
            STYLES="",
            DPI=72,
            FILTER=None,
            MAP_RESOLUTION=72,
            FORMAT_OPTIONS="dpi%3A72",
        )
        url_params = {}
        for field in fields(GetMapRequestParams):
            field_value = getattr(params, field.name)
            if isinstance(field_value, list):
                field_value = ",".join([str(value) for value in field_value])
            if field_value is not None:
                url_params[field.name] = field_value
        return urlencode(url_params)

    def create_wfs_url_params(self, output_format: str = "text/xml") -> str:
        from georama.maps.services.wfs_2_0_0 import WfsOperation

        url_params = {
            "SERVICE": "WFS",
            "REQUEST": "GetFeature",
            "VERSION": "2.0.0",
            "TYPENAMES": f"{WfsOperation.own_namespace}:"
            f"{WfsOperation.encode_layer_name(self.identifier)}",
            "SRSNAME": self.get_datasource.crs_to_qsl.ogc_urn,
            "OUTPUTFORMAT": output_format,
        }
        return urlencode(url_params)

    @staticmethod
    def create_wms_capabilities_url_params():
        url_params = {
            "SERVICE": "WMS",
            "REQUEST": "GetCapabilities",
            "VERSION": "1.3.0",
        }
        return urlencode(url_params)

    @staticmethod
    def create_wfs_capabilities_url_params():
        url_params = {
            "SERVICE": "WFS",
            "REQUEST": "GetCapabilities",
            "VERSION": "2.0.0",
        }
        return urlencode(url_params)

    @property
    def endpoint_url_wms(self):
        url = reverse(f"{self._meta.app_label}:maps_ogc_entry")
        return f"{url}?{self.create_wms_url_params}"

    @property
    def endpoint_url_wfs(self):
        url = reverse(f"{self._meta.app_label}:maps_ogc_entry")
        return f"{url}?{self.create_wfs_url_params()}"

    @property
    def endpoint_url(self):
        return self.endpoint_url_wms

    def _prepare_save(self):
        datasource = self.get_datasource
        if not self.extent:
            self.extent = datasource.bbox_2d_string
        if self.has_datasource_extent(datasource):
            # QSL calculated the wgs84 extent of the datasource already on export
            self.extent_wgs84 = BBox.from_string(datasource.bbox_wgs84).to_2d_string()
        elif datasource.crs_to_qsl.auth_id:
            # we do not handle layers which have no CRS definition!
            bbox_wgs84 = self._to_wgs84_extent(BBox.from_string(self.extent))
            self.extent_wgs84 = bbox_wgs84.to_2d_string()

    def has_datasource_extent(self, datasource: Datasource) -> bool:
        if not datasource.bbox or not datasource.bbox_wgs84:
            return False
        extent = BBox.from_string(self.extent).to_2d_list()
        return extent == BBox.from_string(datasource.bbox).to_2d_list()

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        self._prepare_save()

        super().save(
            force_insert=force_insert,
            force_update=force_update,
            using=using,
            update_fields=update_fields,
        )

    async def asave(
        self,
        *,
        force_insert=False,
        force_update=False,
        using=None,
        update_fields=None,
    ):
        self._prepare_save()

        await super().asave(
            force_insert=force_insert,
            force_update=force_update,
            using=using,
            update_fields=update_fields,
        )

    def _to_wgs84_extent(self, bbox: BBox) -> BBox:
        if not self.crs_transform_to_wgs84:
            source = self._get_spatial_ref(self.get_datasource.crs_to_qsl.auth_id)
            target = self._get_spatial_ref(4326)
            self.crs_transform_to_wgs84 = osgeo_osr.CoordinateTransformation(source, target)
        ll_corner = self.crs_transform_to_wgs84.TransformPoint(bbox.x_min, bbox.y_min)
        ur_corner = self.crs_transform_to_wgs84.TransformPoint(bbox.x_max, bbox.y_max)
        return BBox.from_list([*ll_corner, *ur_corner])

    @staticmethod
    def _get_spatial_ref(epsg_code: int | str):
        if isinstance(epsg_code, str):
            epsg_code = int(epsg_code.split(":")[1])
        spatial_ref = osgeo_osr.SpatialReference()
        # extents are always x/y (east/north) as QSL delivers them, independent of the
        # axis order of the crs, the wgs84 extent is lon/lat
        spatial_ref.SetAxisMappingStrategy(osgeo_osr.OAMS_TRADITIONAL_GIS_ORDER)
        spatial_ref.ImportFromEPSG(epsg_code)
        return spatial_ref

    @property
    def preview_image(self):
        """Encodes a preview image.

        Returns:
            The data encoded preview image or the absolute path to the static fallback
            image.
        """
        if self.preview is not None:
            return f"data:image/png;base64,{base64.b64encode(self.preview).decode()}"
        else:
            return static("core/images/main_plain.svg")

    @property
    def preview_width(self):
        return self.preview_dimensions[0]

    @property
    def preview_height(self):
        return self.preview_dimensions[1]

    def to_qsl_job_layer(self, style_name: str | None = None) -> QslJobLayer:
        datasource = self.get_datasource
        source_definition = datasource.source_to_qsl.definition
        if style_name is not None:
            style = datasource.get_style_by_name(style_name)
        else:
            style = datasource.get_default_style()
        return QslJobLayer(
            id=self.identifier,
            name=self.get_metadata.title,
            source=json.dumps(source_definition.to_qgis_decoded_uri),  # noqa: F821
            driver=datasource.driver,
            style=style,
            remote=source_definition.remote,
            folder_name=str(
                Path(datasource.project.organisation_folder) / Path(datasource.project.path).parent
            ),
        )


class WmsLayer(WmsLayerAbstract):
    ORGANISATION_FIELD_NAME = "datasource__project__organisation"

    PERMISSIONS = {
        "can_view": "view_published_wms_layer",
    }

    ACTION_MAP = {
        "grant": (True, [PERMISSIONS["can_view"]], "grant access"),
        "revoke": (False, list(PERMISSIONS.values()), "revoke access"),
    }

    class Meta:
        verbose_name = _("wms layer")
        verbose_name_plural = _("wms layers")
        permissions = [
            # permission which is used on the model
            ("manage_object_permissions", "Can manage object permissions"),
            # permission which is used for the object permission evaluation on the published themes
            ("view_published_wms_layer", "Can view published WMS Layer"),
        ]

    public = models.BooleanField(default=False)

    datasource = models.ForeignKey(
        Datasource,
        related_name="wms_layers",
        related_query_name="wms_layers",
        on_delete=models.CASCADE,
    )

    metadata = models.OneToOneField(
        Metadata,
        related_name="wms_layer",
        on_delete=models.CASCADE,
    )

    objects = WmsLayerManager()

    def __str__(self):
        return self.metadata.title

    @property
    def get_metadata(self) -> Metadata:
        return self.metadata

    @property
    def get_datasource(self) -> Datasource:
        return self.datasource

    def get_absolute_url(self):
        return reverse(f"{self._meta.app_label}:layer-detail", kwargs={"pk": self.pk})


class UserManager(UserObjectPermissionManager, OrganisationalManager): ...


class GroupManager(GroupObjectPermissionManager, OrganisationalManager): ...


class WmsLayerUserObjectPermission(UserObjectPermissionBase):
    ORGANISATION_FIELD_NAME = "content_object__datasource__project__organisation"
    content_object = models.ForeignKey(
        WmsLayer, on_delete=models.CASCADE, related_name="user_object_permissions"
    )
    time_created = models.DateTimeField(auto_now_add=True)

    objects = UserManager()


class WmsLayerGroupObjectPermission(GroupObjectPermissionBase):
    ORGANISATION_FIELD_NAME = "content_object__datasource__project__organisation"
    content_object = models.ForeignKey(
        WmsLayer, on_delete=models.CASCADE, related_name="group_object_permissions"
    )
    time_created = models.DateTimeField(auto_now_add=True)

    objects = GroupManager()
