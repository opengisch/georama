import base64
import logging
from dataclasses import fields
from numbers import Real
from typing import Literal

from asgiref.sync import async_to_sync, sync_to_async
from django.db import models
from django.urls import reverse
from django.utils.http import urlencode
from django.utils.translation import gettext_lazy as _
from osgeo import osr as osgeo_osr
from qgis_server_light.interface.common import BBox
from qgis_server_light.interface.job.render.input import QslJobParameterRender

from georama.core.entities.models import PermissionInterface, PublishedAs
from georama.core.models.mixins import GeoramaPermissionMixin
from georama.data_integration.models import CustomDataSet, RasterDataSet, VectorDataSet
from georama.maps.apps import central_app_label, qsl_redis_queue
from georama.maps.interfaces.georama.requests import (
    GetMapRequestParams,
    RequestType,
    ServiceType,
    Version,
)
from georama.maps.maps_config import Config

LOGGER = logging.getLogger(__name__)


class PublishedAsWmsAbstract(PublishedAs):
    class Meta:
        abstract = True

    published_as_type = central_app_label
    extent_buffer = models.FloatField(default=0.0, null=False)
    queryable = models.BooleanField(default=True, null=True, blank=True)

    extent = models.CharField(max_length=1000, null=True, blank=True)
    extent_wgs84 = models.CharField(max_length=1000, null=True, blank=True)
    preview = models.BinaryField(null=True, blank=True)

    preview_dimensions: tuple[int, int] = (250, 250)
    preview_dimensions_new_tab: tuple[int, int] = (1500, 1500)
    crs_transform_to_wgs84 = None
    preview_pixel_size_m = 0.00028

    @property
    def get_raster_dataset(self) -> RasterDataSet:
        raise NotImplementedError()

    @property
    def get_vector_dataset(self) -> VectorDataSet:
        raise NotImplementedError()

    @property
    def get_custom_dataset(self) -> CustomDataSet:
        raise NotImplementedError()

    @property
    def bound_dataset(self) -> VectorDataSet | RasterDataSet | CustomDataSet:
        if isinstance(self.get_raster_dataset, RasterDataSet):
            return self.get_raster_dataset
        elif isinstance(self.get_vector_dataset, VectorDataSet):
            return self.get_vector_dataset
        elif isinstance(self.get_custom_dataset, CustomDataSet):
            return self.get_custom_dataset
        else:
            raise NotImplementedError(
                "linked dataset has to be RasterDataSet|VectorDataSet|CustomDataSet!"
            )

    @property
    def create_preview(self) -> bool:
        return True

    @property
    def bound_dataset_type(self) -> Literal["raster", "vector", "custom"] | None:
        bound_dataset = self.bound_dataset
        if isinstance(bound_dataset, RasterDataSet):
            return "raster"
        elif isinstance(bound_dataset, VectorDataSet):
            return "vector"
        elif isinstance(bound_dataset, CustomDataSet):
            return "custom"
        return None

    @property
    def is_queryable(self):
        # Currently we do allow querying on VectorDatasets only
        if isinstance(self.bound_dataset, VectorDataSet):
            return self.queryable
        else:
            return False

    @staticmethod
    def _linear_units_m(crs_auth_id: str | None) -> float | None:
        if not crs_auth_id:
            return None

        spatial_reference = osgeo_osr.SpatialReference()
        try:
            result = spatial_reference.SetFromUserInput(crs_auth_id)
        except RuntimeError:
            return None

        if result != 0 or not spatial_reference.IsProjected():
            return None

        linear_units = spatial_reference.GetLinearUnits()
        if linear_units is None or linear_units <= 0:
            return None
        return linear_units

    @staticmethod
    def _scale_denominator(extent: BBox, pixel_width: int, linear_units_m: float) -> float | None:
        bbox_width = extent.x_max - extent.x_min
        if pixel_width <= 0 or bbox_width <= 0:
            return None

        bbox_width_m = bbox_width * linear_units_m
        return bbox_width_m / (pixel_width * PublishedAsWmsAbstract.preview_pixel_size_m)

    @staticmethod
    def _normalize_scale_denominator(value) -> float | None:
        if not isinstance(value, Real):
            return None
        if value <= 0:
            return None
        return float(value)

    def get_default_extent(self) -> BBox | None:
        try:
            return BBox.from_string(self.extent)
        except (TypeError, ValueError):
            return None

    def get_preview_extent(self, pixel_width: int) -> BBox | None:
        extent = self.get_default_extent()
        if extent is None:
            return None

        dataset = self.bound_dataset
        linear_units_m = self._linear_units_m(dataset.crs_to_qsl.auth_id)
        if linear_units_m is None:
            return extent

        current_scale = self._scale_denominator(extent, pixel_width, linear_units_m)
        if current_scale is None:
            return extent

        min_scale = self._normalize_scale_denominator(dataset.minimum_scale)
        max_scale = self._normalize_scale_denominator(dataset.maximum_scale)
        if max_scale is not None and max_scale <= 1:
            max_scale = None

        target_scale = None
        if min_scale is not None and current_scale > min_scale:
            target_scale = min_scale
        elif max_scale is not None and current_scale < max_scale:
            target_scale = max_scale

        if target_scale is None:
            return extent

        current_width = extent.x_max - extent.x_min
        current_height = extent.y_max - extent.y_min
        if current_width <= 0:
            return extent

        target_width_m = target_scale * pixel_width * self.preview_pixel_size_m
        target_width = target_width_m / linear_units_m
        scale_factor = target_width / current_width
        target_height = current_height * scale_factor if current_height > 0 else target_width

        center_x = extent.x_min + current_width / 2
        center_y = extent.y_min + current_height / 2
        half_width = target_width / 2
        half_height = target_height / 2

        return BBox(
            x_min=center_x - half_width,
            x_max=center_x + half_width,
            y_min=center_y - half_height,
            y_max=center_y + half_height,
            z_min=extent.z_min,
            z_max=extent.z_max,
        )

    def get_preview_extent_or_default(self, pixel_width: int) -> BBox | None:
        return self.get_preview_extent(pixel_width) or self.get_default_extent()

    @property
    def create_wms_url_params(self) -> str | None:
        extent = self.get_preview_extent_or_default(self.preview_dimensions_new_tab[0])
        if extent is None:
            return None

        dataset = self.bound_dataset
        params = GetMapRequestParams(
            SERVICE=ServiceType.wms.value,
            REQUEST=RequestType.get_map.value,
            VERSION=Version.v_1_3_0.value,
            LAYERS=",".join([self.name]),
            BBOX=extent.to_string(),
            CRS=dataset.crs_to_qsl.auth_id,
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
            "SRSNAME": self.bound_dataset.crs_to_qsl.ogc_urn,
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
    def readable_identifier(self) -> str:
        dataset = self.bound_dataset
        return f"{dataset.project.mandant.name}.{dataset.project.name}.{dataset.name}.{self.identifier}"  # noqa: E501

    @property
    def permissions(self) -> list[PermissionInterface]:
        # No need for Update or delete with WMS...
        return self.read_permissions

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
        dataset = self.bound_dataset
        if self.name is None:
            # TODO: maybe we want this to be configurable?
            self.name = dataset.name
        if self.title is None:
            self.title = dataset.title
        if not self.extent:
            self.extent = dataset.bbox_2d_string
        if dataset.crs_to_qsl.auth_id:
            # we do not handle layers which have no CRS definition!
            bbox_wgs84 = self._to_wgs84_extent(BBox.from_string(self.extent))
            self.extent_wgs84 = bbox_wgs84.to_2d_string()
            if self.create_preview:
                # Generate layer preview image
                generate_preview_image_sync = async_to_sync(self.generate_preview_image)
                self.preview = generate_preview_image_sync()

        super().save(
            force_insert=force_insert,
            force_update=force_update,
            using=using,
            update_fields=update_fields,
        )

    async def generate_preview_image(self) -> bytes | None:
        extent = self.get_preview_extent_or_default(self.preview_dimensions[0])
        if extent is None:
            return None

        # We have to call the following @properties a bit awkward because
        # they contain sync django orm actions
        dataset = await sync_to_async(lambda: self.bound_dataset)()
        qsl_job_layer = await sync_to_async(lambda: dataset.to_qsl_job_layer())()
        # this way we always set a style, or it will fail if list has no styles
        # we could make that configurable in admin gui easily
        get_map_job = QslJobParameterRender(
            bbox=extent,
            crs=dataset.crs_to_qsl.auth_id,
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
            source = self._get_spatial_ref(self.bound_dataset.crs_to_qsl.auth_id)
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


class PublishedAsWms(GeoramaPermissionMixin, PublishedAsWmsAbstract):
    class Meta:
        verbose_name = f"WMS {_('Layer')}"
        verbose_name_plural = f"WMS {_('Layers')}"
        permissions = [("can_manage_object_permissions", "Can manage object permissions")]

    raster_dataset = models.ForeignKey(
        RasterDataSet,
        # TODO: this seems wrong => only because error:
        #  It is impossible to add a non-nullable field 'dataset' to ... without
        #  specifying a default. This is because the database needs something
        #  to populate existing rows.
        null=True,
        related_name="published_ogc_wms",
        related_query_name="published_ogc_wms",
        on_delete=models.CASCADE,
    )
    vector_dataset = models.ForeignKey(
        VectorDataSet,
        # TODO: this seems wrong => only because error:
        #  It is impossible to add a non-nullable field 'dataset' to ... without
        #  specifying a default. This is because the database needs something
        #  to populate existing rows.
        null=True,
        related_name="published_ogc_wms",
        related_query_name="published_ogc_wms",
        on_delete=models.CASCADE,
    )
    custom_dataset = models.ForeignKey(
        CustomDataSet,
        # TODO: this seems wrong => only because error:
        #  It is impossible to add a non-nullable field 'dataset' to ... without
        #  specifying a default. This is because the database needs something
        #  to populate existing rows.
        null=True,
        related_name="published_ogc_wms",
        related_query_name="published_ogc_wms",
        on_delete=models.CASCADE,
    )

    @property
    def get_raster_dataset(self) -> RasterDataSet:
        return self.raster_dataset

    @property
    def get_vector_dataset(self) -> VectorDataSet:
        return self.vector_dataset

    @property
    def get_custom_dataset(self) -> CustomDataSet:
        return self.custom_dataset

    def get_absolute_url(self):
        return reverse(f"{self._meta.app_label}:layer-detail", kwargs={"pk": self.pk})
