import base64
import logging
import uuid
from dataclasses import fields

from asgiref.sync import sync_to_async
from django.db import models
from django.urls import reverse
from django.utils.http import urlencode
from django.utils.translation import gettext_lazy as _
from guardian.managers import GroupObjectPermissionManager, UserObjectPermissionManager
from guardian.models import GroupObjectPermissionBase, UserObjectPermissionBase
from osgeo import osr as osgeo_osr
from qgis_server_light.interface.common import BBox
from qgis_server_light.interface.job.render.input import QslJobParameterRender

from georama.core.common.managers import OrganisationalManager
from georama.integration.models import Custom, Datasource, Raster, Vector
from georama.maps.apps import qsl_redis_queue
from georama.maps.interfaces.georama.requests import (
    GetMapRequestParams,
    RequestType,
    ServiceType,
    Version,
)
from georama.maps.managers.wms_layer import WmsLayerManager
from georama.maps.maps_config import Config
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

    preview_dimensions: tuple[int, int] = (250, 250)
    preview_dimensions_new_tab: tuple[int, int] = (1500, 1500)
    crs_transform_to_wgs84 = None

    @property
    def get_raster_datasource(self) -> Raster:
        raise NotImplementedError()

    @property
    def get_vector_datasource(self) -> Vector:
        raise NotImplementedError()

    @property
    def get_custom_datasource(self) -> Custom:
        raise NotImplementedError()

    @property
    def get_datasource(self) -> Datasource:
        raise NotImplementedError()

    @property
    def create_preview(self) -> bool:
        return True

    @property
    def is_queryable(self):
        # Currently we do allow querying on Vectordatasources only
        if isinstance(self.get_datasource, Vector):
            return self.queryable
        else:
            return False

    @property
    def create_wms_url_params(self) -> str:
        params = GetMapRequestParams(
            SERVICE=ServiceType.wms.value,
            REQUEST=RequestType.get_map.value,
            VERSION=Version.v_1_3_0.value,
            LAYERS=",".join([self.name]),
            BBOX=BBox.from_string(self.extent).to_string(),
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

    @property
    def create_wfs_url_params(self, output_format: str = "text/xml") -> str:
        url_params = {
            "SERVICE": "WFS",
            "REQUEST": "GetFeature",
            "VERSION": "2.0.0",
            # TODO PI: Can't use WfsOperation, circular reference
            # "TYPENAMES": f"{WfsOperation.own_namespace}:{self.name}",
            "TYPENAMES": f"georama:{self.name}",
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
        return f"{url}?{self.create_wfs_url_params}"

    @property
    def endpoint_url(self):
        return self.endpoint_url_wms

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        datasource = self.get_datasource
        if not self.extent:
            self.extent = datasource.bbox_2d_string
        if datasource.crs_to_qsl.auth_id:
            # we do not handle layers which have no CRS definition!
            bbox_wgs84 = self._to_wgs84_extent(BBox.from_string(self.extent))
            self.extent_wgs84 = bbox_wgs84.to_2d_string()
            # TODO@maps: add back
            # if self.create_preview:
            #     # Generate layer preview image
            #     generate_preview_image_sync = async_to_sync(self.generate_preview_image)
            #     self.preview = generate_preview_image_sync()

        super().save(
            force_insert=force_insert,
            force_update=force_update,
            using=using,
            update_fields=update_fields,
        )

    async def generate_preview_image(self) -> bytes | None:
        # We have to call the following @properties a bit awkward because
        # they contain sync django orm actions
        datasource = await sync_to_async(lambda: self.get_datasource)()
        qsl_job_layer = await sync_to_async(lambda: datasource.to_qsl_job_layer())()
        # this way we always set a style, or it will fail if list has no styles
        # we could make that configurable in admin gui easily
        get_map_job = QslJobParameterRender(
            bbox=BBox.from_string(self.extent),
            crs=datasource.crs_to_qsl.auth_id,
            width=self.preview_dimensions[0],
            height=self.preview_dimensions[1],
            dpi=72,
            format="image/png",
            layers=[qsl_job_layer],
        )
        try:
            result_tuple = await qsl_redis_queue.post(get_map_job, Config().job_timeout)
            result, _ = result_tuple
            return result.data
        except ValueError as e:
            LOGGER.error(f"Error while generating preview image: {e}")
        except PermissionError as e:
            LOGGER.error(f"Permission error while generating preview image: {e}")
        return None

    def _to_wgs84_extent(self, bbox: BBox) -> BBox:
        if not self.crs_transform_to_wgs84:
            source = self._get_spatial_ref(self.get_datasource.crs_to_qsl.auth_id)
            target = self._get_spatial_ref(4326)
            self.crs_transform_to_wgs84 = osgeo_osr.CoordinateTransformation(source, target)
        llCorner = self.crs_transform_to_wgs84.TransformPoint(bbox.x_min, bbox.y_min)
        urCorner = self.crs_transform_to_wgs84.TransformPoint(bbox.x_max, bbox.y_max)
        return BBox.from_list([*llCorner, *urCorner])

    @staticmethod
    def _get_spatial_ref(epsg_code: int | str):
        if isinstance(epsg_code, str):
            epsg_code = int(epsg_code.split(":")[1])
        axis_order = osgeo_osr.OAMS_AUTHORITY_COMPLIANT
        if epsg_code == 4326:
            axis_order = osgeo_osr.OAMS_TRADITIONAL_GIS_ORDER
        spatial_ref = osgeo_osr.SpatialReference()
        spatial_ref.SetAxisMappingStrategy(axis_order)
        spatial_ref.ImportFromEPSG(epsg_code)
        return spatial_ref

    @property
    def preview_as_base64(self):
        if self.preview is not None:
            return f"data:image/png;base64,{base64.b64encode(self.preview).decode()}"
        else:
            return None

    @property
    def preview_width(self):
        return self.preview_dimensions[0]

    @property
    def preview_height(self):
        return self.preview_dimensions[1]


class WmsLayer(WmsLayerAbstract):
    ORGANISATION_FIELD_NAME = "datasource__project__organisation"

    @property
    def name(self) -> str:
        return str(self.id)

    class Meta:
        verbose_name = _("wms layer")
        verbose_name_plural = _("wms layers")

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

    @property
    def get_datasource(self) -> Datasource:
        return self.datasource

    @property
    def get_raster_datasource(self) -> Raster:
        return self.datasource.raster

    @property
    def get_vector_datasource(self) -> Vector:
        return self.datasource.vector

    @property
    def get_custom_datasource(self) -> Custom:
        return self.datasource.custom

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
