import logging
import uuid
from typing import Literal

from django.core.exceptions import ObjectDoesNotExist
from django.db import models
from django.utils.translation import gettext_lazy as _
from qgis_server_light.interface.common import BBox, Crs, Style
from qgis_server_light.interface.exporter.extract import Custom as QslCustom
from qgis_server_light.interface.exporter.extract import DataSource
from qgis_server_light.interface.exporter.extract import Field as QSlField
from qgis_server_light.interface.exporter.extract import Raster as QslRaster
from qgis_server_light.interface.exporter.extract import Vector as QslVector
from xsdata.formats.dataclass.parsers import DictDecoder
from xsdata.formats.dataclass.parsers.config import ParserConfig
from xsdata.formats.dataclass.serializers import DictEncoder

from georama.core.common.managers import OrganisationalManager
from georama.integration.managers.datasource import DatasourceManager, VectorManager
from georama.integration.models.project import Project


class Datasource(models.Model):
    ORGANISATION_FIELD_NAME = "project__organisation"

    class Meta:
        verbose_name = _("datasource")
        verbose_name_plural = _("datasources")
        unique_together = (
            "qgis_layer_id",
            "project",
        )

    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        help_text=_("Identifier of the datasource."),
    )
    qgis_layer_id = models.CharField(
        max_length=1000,
        help_text=_("Layer identifier from the source QGIS project."),
        verbose_name=_("QGIS layer ID"),
    )
    name = models.CharField(
        max_length=1000, help_text=_("Name of the datasource."), verbose_name=_("name")
    )
    bbox = models.CharField(
        max_length=1000,
        help_text=_("Bounding box of the datasource in the source coordinate reference system."),
        verbose_name=_("bounding box"),
    )
    bbox_wgs84 = models.CharField(
        max_length=1000,
        help_text=_("Bounding box of the datasource transformed to WGS84."),
        verbose_name=_("bounding box (WGS 84)"),
    )
    source = models.JSONField(
        default=dict,
        help_text=_("Source configuration and connection metadata of the datasource."),
        verbose_name=_("source"),
    )
    styles = models.JSONField(
        default=list,
        help_text=_("Rendered style definitions associated with this datasource."),
        verbose_name=_("styles"),
    )
    driver = models.CharField(
        max_length=50,
        help_text=_("Provider driver name used to access the datasource."),
        verbose_name=_("driver"),
    )
    crs = models.JSONField(
        default=dict,
        help_text=_("Coordinate reference system of the datasource."),
        verbose_name=_("CRS"),
    )
    minimum_scale = models.FloatField(
        null=True,
        help_text=_("Minimum scale at which the datasource is visible."),
        verbose_name=_("minimum scale"),
    )
    maximum_scale = models.FloatField(
        null=True,
        help_text=_("Maximum scale at which the datasource is visible."),
        verbose_name=_("maximum scale"),
    )
    project = models.ForeignKey(
        Project,
        on_delete=models.CASCADE,
        related_name="datasources",
        help_text=_("Project the datasource belongs to."),
        verbose_name=_("project"),
    )

    objects = DatasourceManager()

    def __str__(self):
        return self.name

    @property
    def get_parser_config(self):
        return ParserConfig(fail_on_unknown_attributes=False, fail_on_unknown_properties=False)

    @property
    def source_to_qsl(self) -> DataSource:
        # TODO: Implement an ENV Django app to manipulate datasources in a hookable way
        datasource = DictDecoder(config=self.get_parser_config).decode(self.source, DataSource)
        return datasource

    @property
    def crs_to_qsl(self) -> Crs:
        return DictDecoder(config=self.get_parser_config).decode(self.crs, Crs)

    @property
    def bbox_to_list(self) -> list:
        return BBox.from_string(self.bbox).to_list()

    @property
    def bbox_2d_string(self) -> str:
        return BBox.from_string(self.bbox).to_2d_string()

    def get_default_style(self) -> Style:
        default_style_name = "default"
        styles = self.styles_to_qsl
        for style in styles:
            if style.name == default_style_name:
                return style
        if len(styles) > 0:
            first_style = styles[0]
            logging.debug(
                f"Requested style name for layer '{self.name}'"
                f"was {default_style_name} "
                f"but this is not in the available styles,"
                f"we choose the first available style "
                f"instead which is '{first_style.name}'"
            )
            return first_style
        else:
            logging.debug(f"No styles found for layer '{self.name}'")

    @property
    def styles_to_qsl(self) -> list[Style]:
        return DictDecoder(config=self.get_parser_config).decode(self.styles, list[Style])

    @property
    def type(self) -> Literal["vector", "raster", "custom"]:
        for name in ["vector", "raster", "custom"]:
            try:
                getattr(self, name)
                return name
            except ObjectDoesNotExist:
                pass
        raise LookupError("Datasource is stale")

    @property
    def icon(self):
        match self.type:
            case "vector":
                return "fa fa-bezier-curve"
            case "raster":
                return "fa fa-th"
            case "custom":
                return "fa fa-asterisk"
            case _:
                return "fa fa-question"

    @staticmethod
    async def set_common_values_from_qsl(
        qsl_object: QslVector | QslRaster | QslCustom,
        db_objct: "Vector|Raster|Custom",
    ):
        db_objct.name = qsl_object.title
        db_objct.bbox = qsl_object.bbox.to_string()
        db_objct.bbox_wgs84 = qsl_object.bbox_wgs84.to_string()
        db_objct.styles = DictEncoder().encode(qsl_object.styles)
        db_objct.driver = qsl_object.driver
        db_objct.source = DictEncoder().encode(qsl_object.source)
        db_objct.qgis_layer_id = qsl_object.id
        db_objct.crs = DictEncoder().encode(qsl_object.crs)
        db_objct.minimum_scale = qsl_object.minimum_scale
        db_objct.maximum_scale = qsl_object.maximum_scale


class Vector(Datasource):
    class Meta:
        verbose_name = _("vector")
        verbose_name_plural = _("vectors")

    objects = VectorManager()

    geometry_type_simple = models.CharField(
        max_length=1000,
        help_text=_(
            "Simplified geometry type of the vector datasource (eg. point, line, polygon)."
        ),
        verbose_name=_("geometry type"),
    )
    geometry_type_wkb = models.CharField(
        max_length=1000,
        help_text=_("Geometry type of the vector datasource."),
        verbose_name=_("geometry type (WKB)"),
    )

    async def set_values_from_qsl(self, qsl_object: QslVector):
        await self.set_common_values_from_qsl(qsl_object, self)
        self.geometry_type_simple = qsl_object.geometry_type_simple
        self.geometry_type_wkb = qsl_object.geometry_type_wkb


class VectorField(models.Model):
    ORGANISATION_FIELD_NAME = "datasource__project__organisation"

    class Meta:
        unique_together = (
            "name",
            "datasource",
        )
        verbose_name = _("field")
        verbose_name_plural = _("fields")

    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        help_text=_("Identifier of the field."),
    )
    name = models.CharField(
        max_length=1000,
        help_text=_("Original field name from the source datasource."),
        verbose_name=_("name"),
    )
    type = models.CharField(
        max_length=1000,
        help_text=_("Original data type from the source datasource."),
        verbose_name=_("type"),
    )
    is_primary_key = models.BooleanField(
        default=False,
        help_text=_("Whether this field is the datasource primary key."),
        verbose_name=_("primary key"),
    )
    type_wfs = models.CharField(
        max_length=1000,
        help_text=_("Field datatype exposed through WFS."),
        verbose_name=_("WFS type"),
    )
    type_oapif = models.CharField(
        max_length=1000,
        help_text=_("Field datatype exposed through OGC API Features."),
        verbose_name=_("OAPIF type"),
    )
    type_oapif_format = models.CharField(
        null=True,
        max_length=1000,
        help_text=_("Output format for the OGC API Features field type."),
        verbose_name=_("OAPIF format"),
    )
    alias = models.CharField(
        max_length=1000, help_text=_("Human-readable field label."), verbose_name=_("alias")
    )
    comment = models.CharField(
        max_length=1000,
        help_text=_("Comment or description of the field."),
        verbose_name=_("comment"),
    )
    nullable = models.BooleanField(
        default=True,
        help_text=_("Whether this field can store null values."),
        verbose_name=_("nullable"),
    )
    length = models.IntegerField(null=True, help_text=_("...."), verbose_name=_("length"))
    precision = models.IntegerField(
        null=True, help_text=_("Numeric precision."), verbose_name=_("precision")
    )
    datasource = models.ForeignKey(
        Vector,
        on_delete=models.CASCADE,
        help_text=_("Vector datasource this field belongs to."),
        related_name="fields",
        verbose_name=_("datasource"),
    )

    objects = OrganisationalManager()

    def __str__(self):
        return f"{self.alias} ({self.name})"

    async def set_values_from_qsl(self, qsl_object: QSlField):
        self.name = qsl_object.name
        self.type = qsl_object.type
        self.is_primary_key = qsl_object.is_primary_key
        self.type_wfs = qsl_object.type_wfs
        self.type_oapif = qsl_object.type_oapif
        self.type_oapif_format = qsl_object.type_oapif_format
        self.alias = qsl_object.alias
        self.comment = qsl_object.comment
        self.nullable = qsl_object.nullable
        self.length = qsl_object.length
        self.precision = qsl_object.precision


class Raster(Datasource):
    class Meta:
        verbose_name = _("raster")
        verbose_name_plural = _("rasters")

    objects = OrganisationalManager()

    async def set_values_from_qsl(self, qsl_object: QslRaster):
        await self.set_common_values_from_qsl(qsl_object, self)


class Custom(Datasource):
    class Meta:
        verbose_name = _("custom")
        verbose_name_plural = _("custom")

    objects = OrganisationalManager()

    async def set_values_from_qsl(self, qsl_object: QslCustom):
        await self.set_common_values_from_qsl(qsl_object, self)
