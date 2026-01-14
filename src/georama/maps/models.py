import base64
import logging
from typing import List, Tuple

from dataclasses import fields
from asgiref.sync import async_to_sync, sync_to_async
from django.db import models
from django.utils.translation import gettext_lazy as _
from osgeo import osr as osgeo_osr
from qgis_server_light.interface.dispatcher import RedisQueue
from qgis_server_light.interface.job import QslGetMapJob, WmsGetMapParams
from qgis_server_light.interface.qgis import BBox
from django.utils.http import urlencode

from georama.core.entities.models import PermissionInterface, PublishedAs
from georama.data_integration.models import CustomDataSet, RasterDataSet, VectorDataSet
from georama.maps.maps_config import Config
from georama.maps.interfaces.georama.requests import (
    QslGetMapRequest,
    RequestType,
    ServiceType,
    Version,
)

LOGGER = logging.getLogger(__name__)


class PublishedAsWmsAbstract(PublishedAs):
    class Meta:
        abstract = True

    published_as_type = "maps"
    extent_buffer = models.FloatField(
        verbose_name=_("extent buffer"),
        default=0.0,
        null=False,
        help_text=_(
            "The extent buffer defines a border around the layer"
        ),  # TODO PI: Tooltip missing
    )
    queryable = models.BooleanField(
        verbose_name=_("queryable"),
        default=True,
        null=True,
        blank=True,
        help_text=_("Set the layer to be queried via a GetFeatureInfo request"),
    )

    extent = models.CharField(
        verbose_name=_("extent"),
        max_length=1000,
        null=True,
        blank=True,
        help_text=_("Limit the layer to an extent"),
    )
    extent_wgs84 = models.CharField(
        verbose_name=_("extent WGS84"),
        max_length=1000,
        null=True,
        blank=True,
        help_text=_("The specified extent in WGS84 coordinates"),
    )
    preview = models.BinaryField(
        verbose_name=_("preview"),
        null=True,
        blank=True,
        help_text=_("Small image preview to display display in the administration"),
    )

    preview_dimensions: Tuple[int, int] = (250, 250)
    preview_dimensions_new_tab: Tuple[int, int] = (1500, 1500)
    crs_transform_to_wgs84 = None

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
    def preview_as_base64(self):
        return "data:image/png;base64,{}".format(base64.b64encode(self.preview).decode())

    @property
    def is_queryable(self):
        # Currently we do allow querying on VectorDatasets only
        if isinstance(self.bound_dataset, VectorDataSet):
            return self.queryable
        else:
            return False

    @property
    def create_wms_url_params(self) -> str:
        dataset = self.bound_dataset
        bbox = BBox.from_string(self.extent).to_2d_list()
        params = QslGetMapRequest(
            SERVICE=ServiceType.wms.value,
            REQUEST=RequestType.get_map.value,
            VERSION=Version.v_1_3_0.value,
            LAYERS=[self.name],
            BBOX=bbox,
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
        for field in fields(QslGetMapRequest):
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

    @property
    def readable_identifier(self) -> str:
        dataset = self.bound_dataset
        return f"{dataset.project.mandant.name}.{dataset.project.name}.{dataset.name}.{self.identifier}"

    @property
    def permissions(self) -> List[PermissionInterface]:
        # No need for Update or delete with WMS...
        return self.read_permissions

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        dataset = self.bound_dataset
        if self.name is None:
            # TODO: maybe we want this to be configurable?
            self.name = dataset.name
        if self.title is None:
            self.title = dataset.title
        if not self.extent:
            self.extent = BBox.from_string(dataset.bbox).to_2d_string()
        if dataset.crs_to_qsl.auth_id:
            # we do not handle layers which have no CRS definition!
            bbox_wgs84 = self._to_wgs84_extent(BBox.from_string(self.extent))
            self.extent_wgs84 = bbox_wgs84.to_2d_string()

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
        # We have to call the following @properties a bit awkward because they contain sync django orm actions
        dataset = await sync_to_async(lambda: self.bound_dataset)()
        qsl_instance = await sync_to_async(lambda: dataset.to_qsl)()
        # this way we always set a style, or it will fail if list has no styles
        # we could make that configurable in admin gui easily
        default_style = qsl_instance.get_style_by_name("default")
        if default_style is None:
            default_style = qsl_instance.styles[0]
        qsl_instance.style_name = default_style.name
        service_params = WmsGetMapParams(
            BBOX=self.extent,
            CRS=dataset.crs_to_qsl.auth_id,
            WIDTH=str(self.preview_dimensions[0]),
            HEIGHT=str(self.preview_dimensions[1]),
            DPI="72",
            FORMAT_OPTIONS="dpi%3A72",
            LAYERS=self.name,
            FORMAT="image/png",
        )
        get_map_job = QslGetMapJob(
            extent_buffer=0.0,
            service_params=service_params,
            raster_layers=[qsl_instance] if isinstance(dataset, RasterDataSet) else [],
            vector_layers=[qsl_instance] if isinstance(dataset, VectorDataSet) else [],
            custom_layers=[qsl_instance] if isinstance(dataset, CustomDataSet) else [],
        )
        try:
            redis_queue = await RedisQueue.create(Config().redis_url)
            result = await redis_queue.post(get_map_job, Config().job_timeout)
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


class PublishedAsWms(PublishedAsWmsAbstract):
    class Meta:
        verbose_name = _("WMS Layer")
        verbose_name_plural = _("WMS Layers")

    raster_dataset = models.ForeignKey(
        RasterDataSet,
        # TODO: this seems wrong => only because error:
        #  It is impossible to add a non-nullable field 'dataset' to ... without
        #  specifying a default. This is because the database needs something to populate existing rows.
        null=True,
        related_name="published_ogc_wms",
        related_query_name="published_ogc_wms",
        on_delete=models.CASCADE,
    )
    vector_dataset = models.ForeignKey(
        VectorDataSet,
        # TODO: this seems wrong => only because error:
        #  It is impossible to add a non-nullable field 'dataset' to ... without
        #  specifying a default. This is because the database needs something to populate existing rows.
        null=True,
        related_name="published_ogc_wms",
        related_query_name="published_ogc_wms",
        on_delete=models.CASCADE,
    )
    custom_dataset = models.ForeignKey(
        CustomDataSet,
        # TODO: this seems wrong => only because error:
        #  It is impossible to add a non-nullable field 'dataset' to ... without
        #  specifying a default. This is because the database needs something to populate existing rows.
        null=True,
        related_name="published_ogc_wms",
        related_query_name="published_ogc_wms",
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.title or self.name

    @property
    def get_raster_dataset(self) -> RasterDataSet:
        return self.raster_dataset

    @property
    def get_vector_dataset(self) -> VectorDataSet:
        return self.vector_dataset

    @property
    def get_custom_dataset(self) -> CustomDataSet:
        return self.custom_dataset
