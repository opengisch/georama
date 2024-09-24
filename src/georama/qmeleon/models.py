import logging
import datetime
from django.core import serializers
from django.db import models
from qgis_server_light.interface.qgis import (
    Vector, BBox, Raster, Crs, OgrSource, PostgresSource, GdalSource, WmtsSource, WmsSource, DataSource,
    Custom
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
        null=True
    )

    class Meta:
        unique_together = ('name', 'version', 'mandant',)


class DataSet(models.Model):

    class Meta:
        abstract = True

    name = models.CharField(null=False, max_length=1000)
    qgis_layer_id = models.CharField(null=False, max_length=1000)
    title = models.CharField(max_length=1000)
    bbox = models.CharField(max_length=1000)
    bbox_wgs84 = models.CharField(max_length=1000)
    path = models.CharField(max_length=10000)
    source = models.JSONField(
        default=dict
    )
    style = models.TextField()
    # TODO: implement ENUM (wms, ogr, gdal, etc.)
    driver = models.CharField(max_length=50)
    # TODO: implement ENUM (raster, vector)
    crs = models.JSONField(
        default=dict
    )


class VectorDataSet(DataSet):

    class Meta:
        unique_together = ('name', 'project',)

    project = models.ForeignKey(
        Project,
        related_name="vector_datasets",
        related_query_name="vector_dataset",
        on_delete=models.CASCADE
    )

    @property
    def to_qsl(self) -> Vector:
        return Vector(
            name=self.name,
            title=self.title,
            bbox=BBox.from_string(self.bbox),
            bbox_wgs84=BBox.from_string(self.bbox_wgs84),
            path=self.path,
            style=self.style,
            driver=self.driver,
            source=DictDecoder().decode(self.source, DataSource),
            id=self.qgis_layer_id,
            crs=DictDecoder().decode(self.crs, Crs)
        )


class RasterDataSet(DataSet):

    class Meta:
        unique_together = ('name', 'project',)

    project = models.ForeignKey(
        Project,
        related_name="raster_datasets",
        related_query_name="raster_dataset",
        on_delete=models.CASCADE
    )

    @property
    def to_qsl(self) -> Raster:
        return Raster(
            name=self.name,
            title=self.title,
            bbox=BBox.from_string(self.bbox),
            bbox_wgs84=BBox.from_string(self.bbox_wgs84),
            path=self.path,
            style=self.style,
            driver=self.driver,
            source=DictDecoder().decode(self.source, DataSource),
            id=self.qgis_layer_id,
            crs=DictDecoder().decode(self.crs, Crs)
        )


class CustomDataSet(DataSet):

    class Meta:
        unique_together = ('name', 'project',)

    project = models.ForeignKey(
        Project,
        related_name="custom_datasets",
        related_query_name="custom_dataset",
        on_delete=models.CASCADE
    )

    @property
    def to_qsl(self) -> Custom:
        return Custom(
            name=self.name,
            title=self.title,
            bbox=BBox.from_string(self.bbox),
            bbox_wgs84=BBox.from_string(self.bbox_wgs84),
            path=self.path,
            style=self.style,
            driver=self.driver,
            source=DictDecoder().decode(self.source, DataSource),
            id=self.qgis_layer_id,
            crs=DictDecoder().decode(self.crs, Crs)
        )


class Field(models.Model):

    class Meta:
        unique_together = ('name', 'vector_dataset',)

    name = models.CharField(null=False, max_length=1000)
    type = models.CharField(null=False, max_length=1000)
    vector_dataset = models.ForeignKey(
        VectorDataSet,
        related_name="fields",
        related_query_name="field",
        on_delete=models.CASCADE
    )
