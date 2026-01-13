import datetime
import logging
import os.path
from typing import List

from django.db import models
from django.utils.translation import gettext_lazy as _
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
    name = models.CharField(
        null=False,
        max_length=1000,
        verbose_name=_("name"),
        help_text=_("Name of the project file"),
    )
    title = models.CharField(
        max_length=1000, verbose_name=_("title"), help_text=_("Title of the QGIS project")
    )
    version = models.CharField(
        max_length=1000,
        verbose_name=_("version"),
        help_text=_("QGIS version of the project file"),
    )
    hash = models.CharField(
        max_length=20000,
        null=True,
        blank=True,
        verbose_name=_("file hash"),
        help_text=_("Unique file hash of the QGIS project file"),
    )
    modification_date = models.DateTimeField(
        default=datetime.datetime.now,
        verbose_name=_("modification date"),
        help_text=_("Last time the QGIS project file was modified"),
    )
    integration_date = models.DateTimeField(
        default=datetime.datetime.now,
        verbose_name=_("integration date"),
        help_text=_("Last integration of the QGIS project"),
    )

    mandant = models.ForeignKey(
        Mandant,
        related_name="mandants",
        related_query_name="mandant",
        on_delete=models.CASCADE,
        null=True,
        verbose_name=_("origin"),
        help_text=_("Location of the project on disk"),
    )

    class Meta:
        verbose_name = _("Project")
        verbose_name_plural = _("Projects")
        unique_together = (
            "name",
            "version",
            "mandant",
        )

    @property
    def is_outdated(self):
        # TODO PI: This is a Mock. Should originate from a comparison between JSON and QGIS File on disk
        return self.pk % 2 == 0

    @property
    def has_processing_error(self):
        # TODO PI: This is a Mock. Should originate from analysing log output from extraction and integration
        return False

    def __str__(self):
        return self.title or self.name


class DataSet(models.Model):
    class Meta:
        abstract = True
        verbose_name = _("dataset")
        verbose_name_plural = _("datasets")

    name = models.CharField(
        null=False, max_length=1000, verbose_name=_("name"), help_text=_("Name of the dataset")
    )
    qgis_layer_id = models.CharField(
        null=False,
        max_length=1000,
        unique=True,
        verbose_name=_("qgis layer id"),
        help_text=_("Layer ID of the dataset in the QGIS project"),
    )
    title = models.CharField(
        max_length=1000, verbose_name=_("title"), help_text=_("Title of the dataset")
    )
    bbox = models.CharField(
        max_length=1000, verbose_name=_("bounding box"), help_text=_("Extent of the dataset")
    )
    bbox_wgs84 = models.CharField(
        max_length=1000,
        verbose_name=_("bounding box WGS84"),
        help_text=_("Extent of the dataset in WGS84"),
    )
    path = models.CharField(
        max_length=10000,
        verbose_name=_("file path"),
        help_text=_("File path or connection string"),
    )
    source = models.JSONField(
        default=dict, verbose_name=_("source"), help_text=_("Source definition")
    )
    styles = models.JSONField(default=dict, verbose_name=_("styles"), help_text=_("Symbology"))
    # TODO: implement ENUM (wms, ogr, gdal, etc.)
    driver = models.CharField(
        max_length=50,
        verbose_name=_("driver"),
        help_text=_("Software-Driver to read the dataset"),
    )
    crs = models.JSONField(
        default=dict,
        verbose_name=_("crs"),
        help_text=_("Coordinate Reference System, as EPSG-Code"),
    )
    minimum_scale = models.FloatField(
        null=True,
        verbose_name=_("minimum scale"),
        help_text=_("Minimum scale at which dataset is visible"),
    )
    maximum_scale = models.FloatField(
        null=True,
        verbose_name=_("maximum scale"),
        help_text=_("Maximum scale at which dataset is visible"),
    )

    @property
    def get_parser_config(self):
        return ParserConfig(fail_on_unknown_attributes=False, fail_on_unknown_properties=False)

    @property
    def source_to_qsl(self) -> tuple[DataSource, str]:
        # TODO: Implement an ENV Django app to manipulate datasources in a hookable way
        datasource = DictDecoder(config=self.get_parser_config).decode(self.source, DataSource)
        path = self.path
        if datasource.postgres:
            path = path
        elif datasource.ogr:
            path = os.path.join(self.project.mandant.name, path)
        elif datasource.gdal:
            path = os.path.join(self.project.mandant.name, path)
        elif datasource.vector_tile:
            if not datasource.vector_tile.remote:
                path = os.path.join(self.project.mandant.name, datasource.vector_tile.url)
        return datasource, path

    @property
    def crs_to_qsl(self) -> Crs:
        return DictDecoder(config=self.get_parser_config).decode(self.crs, Crs)

    @property
    def styles_to_qsl(self) -> List[Style]:
        return DictDecoder(config=self.get_parser_config).decode(self.styles, List[Style])

    @property
    def icon(self):
        return "fa fa-question"

    def __str__(self):
        return f"{self.title} ({self.name})"


class VectorDataSet(DataSet):
    class Meta:
        verbose_name = _("Vector Dataset")
        verbose_name_plural = _("Vector Datasets")
        unique_together = (
            "name",
            "project",
        )

    project = models.ForeignKey(
        Project,
        related_name="vector_datasets",
        related_query_name="vector_dataset",
        on_delete=models.CASCADE,
        verbose_name=_("project"),
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

    @property
    def icon(self):
        return "fa fa-bezier-curve"


class RasterDataSet(DataSet):
    class Meta:
        verbose_name = _("Raster Dataset")
        verbose_name_plural = _("Raster Datasets")
        unique_together = (
            "name",
            "project",
        )

    project = models.ForeignKey(
        Project,
        related_name="raster_datasets",
        related_query_name="raster_dataset",
        on_delete=models.CASCADE,
        verbose_name=_("project"),
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

    @property
    def icon(self):
        return "fa fa-grid"


class CustomDataSet(DataSet):
    class Meta:
        verbose_name = _("Custom Dataset")
        verbose_name_plural = _("Custom Datasets")
        unique_together = (
            "name",
            "project",
        )

    project = models.ForeignKey(
        Project,
        related_name="custom_datasets",
        related_query_name="custom_dataset",
        on_delete=models.CASCADE,
        verbose_name=_("project"),
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

    @property
    def icon(self):
        return "fa fa-flask"


class Field(models.Model):
    class Meta:
        unique_together = (
            "name",
            "vector_dataset",
        )

    name = models.CharField(null=False, max_length=1000)
    type = models.CharField(null=False, max_length=1000)
    is_primary_key = models.BooleanField(null=False, default=False)
    type_wfs = models.CharField(null=False, default="UNSET", max_length=1000)
    type_oapif = models.CharField(null=False, default="UNSET", max_length=1000)
    type_oapif_format = models.CharField(null=True, default="UNSET", max_length=1000)
    alias = models.CharField(null=False, default="UNSET", max_length=1000)
    comment = models.CharField(null=False, default="UNSET", max_length=1000)
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
            comment=self.comment,
            nullable=self.nullable,
            length=self.length,
            precision=self.precision,
        )

    def __str__(self):
        return f"{self.alias} ({self.name})"
