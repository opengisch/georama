import datetime
import logging
import os.path

from django.db import models
from qgis_server_light.interface.qgis import (
    BBox,
    Crs,
    Custom,
    DataSource,
    Raster,
    Vector,
)
from xsdata.formats.dataclass.parsers import DictDecoder

log = logging.getLogger(__name__)


class Mandant(models.Model):
    name = models.CharField(unique=True)
    description = models.TextField(null=True)


class Project(models.Model):
    name = models.CharField(null=False, max_length=1000)
    title = models.CharField(max_length=1000)
    version = models.CharField(max_length=1000)
    hash = models.CharField(max_length=20000, null=True, blank=True)
    integration_date = models.DateTimeField(default=datetime.datetime.now)
    mandant = models.ForeignKey(
        Mandant,
        related_name="mandants",
        related_query_name="mandant",
        on_delete=models.CASCADE,
        null=True,
    )

    class Meta:
        unique_together = (
            "name",
            "version",
            "mandant",
        )


class DataSet(models.Model):
    class Meta:
        abstract = True

    name = models.CharField(null=False, max_length=1000)
    qgis_layer_id = models.CharField(null=False, max_length=1000, unique=True)
    title = models.CharField(max_length=1000)
    bbox = models.CharField(max_length=1000)
    bbox_wgs84 = models.CharField(max_length=1000)
    path = models.CharField(max_length=10000)
    source = models.JSONField(default=dict)
    style = models.TextField()
    # TODO: implement ENUM (wms, ogr, gdal, etc.)
    driver = models.CharField(max_length=50)
    # TODO: implement ENUM (raster, vector)
    crs = models.JSONField(default=dict)
    minimum_scale = models.FloatField(null=True)
    maximum_scale = models.FloatField(null=True)

    @property
    def source_to_qsl(self) -> tuple[DataSource, str]:
        # TODO: Implement an ENV Django app to manipulate datasources in a hookable way
        datasource = DictDecoder().decode(self.source, DataSource)
        path = self.path
        if datasource.postgres:
            datasource.postgres.host = "georama-test_data"
            datasource.postgres.port = "5432"
            path = path.replace("host=localhost", f"host={datasource.postgres.host}")
            path = path.replace("port=54322", f"port={datasource.postgres.port}")
            path = path.replace("host='localhost'", f"host={datasource.postgres.host}")
            path = path.replace("port='54322'", f"port={datasource.postgres.port}")
            print(path)
        elif datasource.ogr:
            path = os.path.join(self.project.mandant.name, path)
        elif datasource.gdal:
            path = os.path.join(self.project.mandant.name, path)

        return datasource, path

    @property
    def crs_to_qsl(self) -> Crs:
        return DictDecoder().decode(self.crs, Crs)


class VectorDataSet(DataSet):
    class Meta:
        unique_together = (
            "name",
            "project",
        )

    project = models.ForeignKey(
        Project,
        related_name="vector_datasets",
        related_query_name="vector_dataset",
        on_delete=models.CASCADE,
    )

    def to_qsl(self, published_layer_name: str) -> Vector:
        datasource, path = self.source_to_qsl
        return Vector(
            name=published_layer_name,
            title=self.title,
            bbox=BBox.from_string(self.bbox),
            bbox_wgs84=BBox.from_string(self.bbox_wgs84),
            path=path,
            style=self.style,
            driver=self.driver,
            source=datasource,
            id=self.qgis_layer_id,
            crs=self.crs_to_qsl,
            minimum_scale=self.minimum_scale,
            maximum_scale=self.maximum_scale,
        )


class RasterDataSet(DataSet):
    class Meta:
        unique_together = (
            "name",
            "project",
        )

    project = models.ForeignKey(
        Project,
        related_name="raster_datasets",
        related_query_name="raster_dataset",
        on_delete=models.CASCADE,
    )

    def to_qsl(self, published_layer_name: str) -> Raster:
        datasource, path = self.source_to_qsl
        return Raster(
            name=published_layer_name,
            title=self.title,
            bbox=BBox.from_string(self.bbox),
            bbox_wgs84=BBox.from_string(self.bbox_wgs84),
            path=path,
            style=self.style,
            driver=self.driver,
            source=datasource,
            id=self.qgis_layer_id,
            crs=self.crs_to_qsl,
            minimum_scale=self.minimum_scale,
            maximum_scale=self.maximum_scale,
        )


class CustomDataSet(DataSet):
    class Meta:
        unique_together = (
            "name",
            "project",
        )

    project = models.ForeignKey(
        Project,
        related_name="custom_datasets",
        related_query_name="custom_dataset",
        on_delete=models.CASCADE,
    )

    def to_qsl(self, published_layer_name: str) -> Custom:
        datasource, path = self.source_to_qsl
        return Custom(
            name=published_layer_name,
            title=self.title,
            bbox=BBox.from_string(self.bbox),
            bbox_wgs84=BBox.from_string(self.bbox_wgs84),
            path=path,
            style=self.style,
            driver=self.driver,
            source=datasource,
            id=self.qgis_layer_id,
            crs=self.crs_to_qsl,
            minimum_scale=self.minimum_scale,
            maximum_scale=self.maximum_scale,
        )


class Field(models.Model):
    class Meta:
        unique_together = (
            "name",
            "vector_dataset",
        )

    name = models.CharField(null=False, max_length=1000)
    type = models.CharField(null=False, max_length=1000)
    vector_dataset = models.ForeignKey(
        VectorDataSet,
        related_name="fields",
        related_query_name="field",
        on_delete=models.CASCADE,
    )
