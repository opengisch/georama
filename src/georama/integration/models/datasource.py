import uuid

from django.db import models
from django.utils.translation import gettext_lazy as _
from qgis_server_light.interface.common import BBox
from qgis_server_light.interface.exporter.extract import (
    Crs,
    DataSource,
)
from xsdata.formats.dataclass.parsers import DictDecoder
from xsdata.formats.dataclass.parsers.config import ParserConfig

from georama.core.common.managers import OrganisationalManager
from georama.integration.managers.datasource import DatasourceManager, VectorManager
from georama.integration.models.project import Project


class Datasource(models.Model):
    ORGANISATION_FIELD_NAME = "project__collection__organisation"

    class Meta:
        verbose_name = _("datasource")
        verbose_name_plural = _("datasources")
        unique_together = (
            "qgis_layer_id",
            "project",
        )

    id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, help_text=_("Identifier of the datasource.")
    )
    qgis_layer_id = models.CharField(
        max_length=1000, help_text=_("Layer identifier from the source QGIS project.")
    )
    name = models.CharField(max_length=1000, help_text=_("Name of the datasource."))
    bbox = models.CharField(
        max_length=1000,
        help_text=_("Bounding box of the datasource in the source coordinate reference system."),
    )
    bbox_wgs84 = models.CharField(
        max_length=1000, help_text=_("Bounding box of the datasource transformed to WGS84.")
    )
    source = models.JSONField(
        default=dict, help_text=_("Source configuration and connection metadata of the datasource.")
    )
    styles = models.JSONField(
        default=dict, help_text=_("Rendered style definitions associated with this datasource.")
    )
    driver = models.CharField(
        max_length=50, help_text=_("Provider driver name used to access the datasource.")
    )
    crs = models.JSONField(
        default=dict, help_text=_("Coordinate reference system of the datasource.")
    )
    minimum_scale = models.FloatField(
        null=True, help_text=_("Minimum scale at which the datasource is visible.")
    )
    maximum_scale = models.FloatField(
        null=True, help_text=_("Maximum scale at which the datasource is visible.")
    )
    project = models.ForeignKey(
        Project,
        on_delete=models.CASCADE,
        related_name="datasources",
        help_text=_("Project the datasource belongs to."),
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
    )
    geometry_type_wkb = models.CharField(
        max_length=1000, help_text=_("Geometry type of the vector datasource.")
    )


class Field(models.Model):
    ORGANISATION_FIELD_NAME = "datasource__project__collection__organisation"

    class Meta:
        unique_together = (
            "name",
            "datasource",
        )
        verbose_name = _("field")
        verbose_name_plural = _("fields")

    id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, help_text=_("Identifier of the field.")
    )
    name = models.CharField(
        max_length=1000, help_text=_("Original field name from the source datasource.")
    )
    type = models.CharField(
        max_length=1000, help_text=_("Original data type from the source datasource.")
    )
    is_primary_key = models.BooleanField(
        default=False, help_text=_("Whether this field is the datasource primary key.")
    )
    type_wfs = models.CharField(max_length=1000, help_text=_("Field datatype exposed through WFS."))
    type_oapif = models.CharField(
        max_length=1000, help_text=_("Field datatype exposed through OGC API Features.")
    )
    type_oapif_format = models.CharField(
        max_length=1000, help_text=_("Output format for the OGC API Features field type.")
    )
    alias = models.CharField(max_length=1000, help_text=_("Human-readable field label."))
    comment = models.CharField(max_length=1000, help_text=_("Comment or description of the field."))
    nullable = models.BooleanField(
        default=True, help_text=_("Whether this field can store null values.")
    )
    length = models.IntegerField(null=True, help_text=_("...."))
    precision = models.IntegerField(null=True, help_text=_("Numeric precision."))
    datasource = models.ForeignKey(
        Vector,
        on_delete=models.CASCADE,
        help_text=_("Vector datasource this field belongs to."),
        related_name="fields",
    )

    objects = OrganisationalManager()

    def __str__(self):
        return f"{self.alias} ({self.name})"


class Raster(Datasource):
    class Meta:
        verbose_name = _("raster")
        verbose_name_plural = _("rasters")

    objects = OrganisationalManager()


class Custom(Datasource):
    class Meta:
        verbose_name = _("custom")
        verbose_name_plural = _("custom")

    objects = OrganisationalManager()
