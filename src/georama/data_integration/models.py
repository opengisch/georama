import datetime
import json
import logging
from dataclasses import fields

from django.db import models
from django.utils.translation import gettext as _
from qgis_server_light.interface.common import BBox
from qgis_server_light.interface.exporter.extract import Crs, Custom, DataSource
from qgis_server_light.interface.exporter.extract import Field as QslField
from qgis_server_light.interface.exporter.extract import Raster, Style, Vector
from qgis_server_light.interface.job.common.input import QslJobLayer
from xsdata.formats.dataclass.parsers import DictDecoder
from xsdata.formats.dataclass.parsers.config import ParserConfig

from georama.core.models.mixins import GeoramaPermissionMixin

log = logging.getLogger(__name__)


class Mandant(models.Model):

    class Meta:
        verbose_name = _("Mandant")
        verbose_name_plural = _("Mandants")

    name = models.CharField(unique=True)
    description = models.TextField(null=True)

    def __str__(self):
        return self.name


class Project(GeoramaPermissionMixin, models.Model):

    class Meta:
        unique_together = (
            "name",
            "version",
            "mandant",
        )
        verbose_name = _("Project")
        verbose_name_plural = _("Projects")

    name = models.CharField(null=False, max_length=1000, verbose_name="name")
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


class DataSet(models.Model):
    class Meta:
        abstract = True

    name = models.CharField(null=False, max_length=1000)
    qgis_layer_id = models.CharField(null=False, max_length=1000, unique=True)
    title = models.CharField(max_length=1000)
    bbox = models.CharField(max_length=1000)
    bbox_wgs84 = models.CharField(max_length=1000)
    source = models.JSONField(default=dict)
    styles = models.JSONField(default=dict)
    driver = models.CharField(max_length=50)
    crs = models.JSONField(default=dict)
    minimum_scale = models.FloatField(null=True)
    maximum_scale = models.FloatField(null=True)

    @property
    def dataset_type(self):
        raise NotImplementedError("This is a abstract base class")

    @property
    def get_parser_config(self):
        return ParserConfig(fail_on_unknown_attributes=False, fail_on_unknown_properties=False)

    @property
    def source_to_qsl(self) -> DataSource:
        # TODO: Implement an ENV Django app to manipulate datasources in a hookable way
        datasource = DictDecoder(config=self.get_parser_config).decode(self.source, DataSource)
        return datasource

    @property
    def driver_name(self):
        datasource = self.source_to_qsl
        for field in fields(datasource):
            value = getattr(datasource, field.name)
            if value is not None:
                return field.name
        return None

    @property
    def crs_to_qsl(self) -> Crs:
        return DictDecoder(config=self.get_parser_config).decode(self.crs, Crs)

    @property
    def styles_to_qsl(self) -> list[Style]:
        return DictDecoder(config=self.get_parser_config).decode(self.styles, list[Style])

    @property
    def bbox_to_list(self) -> list:
        return BBox.from_string(self.bbox).to_list()

    @property
    def bbox_2d_string(self) -> str:
        return BBox.from_string(self.bbox).to_2d_string()

    @property
    def bbox_wgs84_to_list(self) -> list:
        return BBox.from_string(self.bbox_wgs84).to_list()

    def to_qsl_job_layer(self, style_name: str | None = None) -> QslJobLayer:
        source_definition = self.source_to_qsl.definition
        if style_name is not None:
            style = self.get_style_by_name(style_name)
        else:
            style = self.get_default_style()
        return QslJobLayer(
            id=self.qgis_layer_id,
            name=self.name,
            source=json.dumps(source_definition.to_qgis_decoded_uri),  # noqa: F821
            driver=self.driver,
            style=style,
            remote=source_definition.remote,
            folder_name=self.project.mandant.name,
        )

    def get_style_by_name(self, name: str) -> Style:
        styles = self.styles_to_qsl
        for style in styles:
            if style.name == name:
                return style
        raise LookupError(
            f"No Style was found with name: '{name}' - "
            f"Available names are {[s.name for s in styles]}"
        )

    def get_default_style(self) -> Style:
        default_style_name = "default"
        styles = self.styles_to_qsl
        for style in styles:
            if style.name == default_style_name:
                return style
        logging.debug(
            f"Requested style name for layer '{self.name}'"
            f"was {default_style_name} "
            f"but this is not in the available styles,"
            f"we choose the first available style "
            f"instead which is '{styles[0].name}'"
        )
        return styles[0]

    def __str__(self):
        return f"{self.title} ({self.name})"


class VectorDataSet(DataSet):
    class Meta:
        unique_together = (
            "name",
            "project",
        )
        verbose_name = _("Vector Dataset")
        verbose_name_plural = _("Vector Datasets")

    project = models.ForeignKey(
        Project,
        related_name="vector_datasets",
        related_query_name="vector_dataset",
        on_delete=models.CASCADE,
    )
    geometry_type_simple = models.CharField(max_length=1000, null=False, default="UNSET")
    geometry_type_wkb = models.CharField(max_length=1000, null=False, default="UNSET")

    @property
    def dataset_type(self):
        return "vector"

    @property
    def fields_to_qsl(self) -> list[QslField]:
        fields = []
        for field in self.fields.all():
            fields.append(field.to_qsl)
        return fields

    @property
    def to_qsl(self) -> Vector:
        datasource = self.source_to_qsl
        return Vector(
            name=self.name,
            title=self.title,
            bbox=BBox.from_string(self.bbox),
            bbox_wgs84=BBox.from_string(self.bbox_wgs84),
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
        verbose_name = _("Raster Dataset")
        verbose_name_plural = _("Raster Datasets")

    project = models.ForeignKey(
        Project,
        related_name="raster_datasets",
        related_query_name="raster_dataset",
        on_delete=models.CASCADE,
    )

    @property
    def dataset_type(self):
        return "raster"

    @property
    def to_qsl(self) -> Raster:
        datasource = self.source_to_qsl
        return Raster(
            name=self.name,
            title=self.title,
            bbox=BBox.from_string(self.bbox),
            bbox_wgs84=BBox.from_string(self.bbox_wgs84),
            driver=self.driver,
            source=datasource,
            styles=DictDecoder().decode(self.styles, list[Style]),
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
        verbose_name = _("Custom Dataset")
        verbose_name_plural = _("Custom Datasets")

    project = models.ForeignKey(
        Project,
        related_name="custom_datasets",
        related_query_name="custom_dataset",
        on_delete=models.CASCADE,
    )

    @property
    def dataset_type(self):
        return "custom"

    @property
    def to_qsl(self) -> Custom:
        datasource = self.source_to_qsl
        return Custom(
            name=self.name,
            title=self.title,
            bbox=BBox.from_string(self.bbox),
            bbox_wgs84=BBox.from_string(self.bbox_wgs84),
            driver=self.driver,
            source=datasource,
            styles=DictDecoder().decode(self.styles, list[Style]),
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
        verbose_name = _("Vector Dataset Field")
        verbose_name_plural = _("Vector Dataset Fields")

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
