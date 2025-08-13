import logging
from typing import List
from asgiref.sync import async_to_sync
from django.db import models
from django.utils.translation import gettext_lazy as _
from qgis_server_light.interface.dispatcher import RedisQueue
from qgis_server_light.interface.job import WmsGetMapParams, QslGetMapJob
from qgis_server_light.interface.qgis import BBox

from georama.core.entities.models import PermissionInterface, PublishedAs
from georama.data_integration.models import CustomDataSet, RasterDataSet, VectorDataSet

from georama.maps.maps_config import Config


LOGGER = logging.getLogger(__name__)


class PublishedAsWmsAbstract(PublishedAs):
    class Meta:
        abstract = True

    published_as_type = "maps"
    extent_buffer = models.FloatField(default=0.0, null=False)
    queryable = models.BooleanField(default=True, null=True, blank=True)

    extent = models.CharField(max_length=1000, null=True, blank=True)
    preview = models.BinaryField(null=True, blank=True)

    preview_dimensions = (250, 250)

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
            bbox = BBox.from_string(dataset.bbox)
            self.extent = ",".join(
                [str(b) for b in [bbox.x_min, bbox.y_min, bbox.x_max, bbox.y_max]]
            )

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
        dataset = self.bound_dataset
        service_params = WmsGetMapParams(
            BBOX=self.extent,
            CRS=dataset.crs_to_qsl.auth_id,
            WIDTH=str(self.preview_dimensions[0]),
            HEIGHT=str(self.preview_dimensions[1]),
            DPI="72",
            FORMAT_OPTIONS="dpi%3A72",
            LAYERS=self.name,
            STYLES="default",
            FORMAT="image/png",
        )
        get_map_job = QslGetMapJob(
            extent_buffer=0.0,
            service_params=service_params,
            raster_layers=[dataset.to_qsl] if isinstance(dataset, RasterDataSet) else [],
            vector_layers=[dataset.to_qsl] if isinstance(dataset, VectorDataSet) else [],
            custom_layers=[dataset.to_qsl] if isinstance(dataset, CustomDataSet) else [],
        )
        try:
            redis_queue = RedisQueue(Config().redis_url)
            result = await redis_queue.post(get_map_job, Config().job_timeout)
            return result.data
        except ValueError as e:
            LOGGER.error(f"Error while generating preview image: {e}")
        except PermissionError as e:
            LOGGER.error(f"Permission error while generating preview image: {e}")
        return None


class PublishedAsWms(PublishedAsWmsAbstract):
    class Meta:
        verbose_name = f'WMS {_("Layer")}'
        verbose_name_plural = f'WMS {_("Layers")}'

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

    @property
    def get_raster_dataset(self) -> RasterDataSet:
        return self.raster_dataset

    @property
    def get_vector_dataset(self) -> VectorDataSet:
        return self.vector_dataset

    @property
    def get_custom_dataset(self) -> CustomDataSet:
        return self.custom_dataset
