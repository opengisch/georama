import datetime
import logging
import os.path
from typing import List

from django.db import models
from qgis_server_light.interface.qgis import (
    BBox,
    Crs,
    Custom,
    DataSource,
    Raster,
    Style,
    Vector,
)
from xsdata.formats.dataclass.parsers import DictDecoder
from xsdata.formats.dataclass.parsers.config import ParserConfig

log = logging.getLogger(__name__)


class Mandant(models.Model):
    name = models.CharField(unique=True)
    description = models.TextField(null=True)

    def __str__(self):
        return self.name


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
    styles = models.JSONField(default=dict)
    # TODO: implement ENUM (wms, ogr, gdal, etc.)
    driver = models.CharField(max_length=50)
    # TODO: implement ENUM (raster, vector)
    crs = models.JSONField(default=dict)
    minimum_scale = models.FloatField(null=True)
    maximum_scale = models.FloatField(null=True)

    @property
    def source_to_qsl(self) -> tuple[DataSource, str]:
        config = ParserConfig(
            fail_on_unknown_attributes=False, fail_on_unknown_properties=False
        )
        datasource = DictDecoder(config).decode(self.source, DataSource)
        path = self.path
        if datasource.postgres:
            path = path
        elif datasource.ogr:
            path = os.path.join(self.project.mandant.name, path)
        elif datasource.gdal:
            path = os.path.join(self.project.mandant.name, path)

        return datasource, path

    @property
    def crs_to_qsl(self) -> Crs:
        config = ParserConfig(
            fail_on_unknown_attributes=False, fail_on_unknown_properties=False
        )
        return DictDecoder(config=config).decode(self.crs, Crs)

    def __str__(self):
        return f"{self.title} ({self.name})"


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
    geometry_type_simple = models.CharField(max_length=1000, null=False, default="UNSET")
    geometry_type_wkb = models.CharField(max_length=1000, null=False, default="UNSET")

    @property
    def to_qsl(self) -> Vector:
        datasource, path = self.source_to_qsl
        return Vector(
            name=self.name,
            title=self.title,
            bbox=BBox.from_string(self.bbox),
            bbox_wgs84=BBox.from_string(self.bbox_wgs84),
            path=path,
            driver=self.driver,
            source=datasource,
            styles=DictDecoder().decode(self.styles, List[Style]),
            id=self.qgis_layer_id,
            crs=self.crs_to_qsl,
            minimum_scale=self.minimum_scale,
            maximum_scale=self.maximum_scale,
            geometry_type_simple=self.geometry_type_simple,
            geometry_type_wkb=self.geometry_type_wkb,
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

    @property
    def to_qsl(self) -> Raster:
        datasource, path = self.source_to_qsl
        return Raster(
            name=self.name,
            title=self.title,
            bbox=BBox.from_string(self.bbox),
            bbox_wgs84=BBox.from_string(self.bbox_wgs84),
            path=path,
            driver=self.driver,
            source=datasource,
            styles=DictDecoder().decode(self.styles, List[Style]),
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

    @property
    def to_qsl(self) -> Custom:
        datasource, path = self.source_to_qsl
        return Custom(
            name=self.name,
            title=self.title,
            bbox=BBox.from_string(self.bbox),
            bbox_wgs84=BBox.from_string(self.bbox_wgs84),
            path=path,
            driver=self.driver,
            source=datasource,
            styles=DictDecoder().decode(self.styles, List[Style]),
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
    type_simple = models.CharField(null=False, default="UNSET", max_length=1000)
    alias = models.CharField(null=False, default="UNSET", max_length=1000)
    nullable = models.BooleanField(null=False, default=True)
    vector_dataset = models.ForeignKey(
        VectorDataSet,
        related_name="fields",
        related_query_name="field",
        on_delete=models.CASCADE,
    )
