import datetime
import logging
import os.path
from typing import List

from django.db import models
from qgis_server_light.interface.qgis import BBox, Crs, Custom, DataSource
from qgis_server_light.interface.qgis import Field as QslField
from qgis_server_light.interface.qgis import Raster, Style, Vector
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
    def get_parser_config(self):
        return ParserConfig(fail_on_unknown_attributes=False, fail_on_unknown_properties=False)

    @property
    def source_to_qsl(self) -> tuple[DataSource, str]:
        # TODO: Implement an ENV Django app to manipulate datasources in a hookable way
        datasource = DictDecoder(config=self.get_parser_config).decode(self.source, DataSource)
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
        return DictDecoder(config=self.get_parser_config).decode(self.crs, Crs)

    @property
    def styles_to_qsl(self) -> List[Style]:
        return DictDecoder(config=self.get_parser_config).decode(self.styles, List[Style])

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
    def fields_to_qsl(self) -> List[QslField]:
        fields = []
        for field in self.fields.all():
            fields.append(field.to_qsl)
        return fields

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
            styles=self.styles_to_qsl,
            id=self.qgis_layer_id,
            crs=self.crs_to_qsl,
            minimum_scale=self.minimum_scale,
            maximum_scale=self.maximum_scale,
            geometry_type_simple=self.geometry_type_simple,
            geometry_type_wkb=self.geometry_type_wkb,
            fields=self.fields_to_qsl,
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
    is_primary_key = models.BooleanField(null=False, default=True)
    type_wfs = models.CharField(null=False, default="UNSET", max_length=1000)
    type_oapif = models.CharField(null=False, default="UNSET", max_length=1000)
    type_oapif_format = models.CharField(null=True, default="UNSET", max_length=1000)
    alias = models.CharField(null=False, default="UNSET", max_length=1000)
    nullable = models.BooleanField(null=False, default=True)
    length = models.IntegerField(null=True)
    precision = models.IntegerField(null=True)

    vector_dataset = models.ForeignKey(
        VectorDataSet,
        related_name="fields",
        related_query_name="field",
        on_delete=models.CASCADE,
    )

    @property
    def to_qsl(self) -> QslField:
        return QslField(
            name=self.name,
            type=self.type,
            is_primary_key=self.is_primary_key,
            type_wfs=self.type_wfs,
            type_oapif=self.type_oapif,
            type_oapif_format=self.type_oapif_format,
            alias=self.alias,
            nullable=self.nullable,
            length=self.length,
            precision=self.precision,
        )
