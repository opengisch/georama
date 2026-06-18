import uuid

from django.db import models
from django.utils.translation import gettext_lazy as _

from georama.integration.managers.dataset import DatasetManager, VectorManager
from georama.integration.models.project import Project


class Dataset(models.Model):
    class Meta:
        verbose_name = _("dataset")
        verbose_name_plural = _("datasets")
        unique_together = (
            "qgis_layer_id",
            "project",
        )

    id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, help_text=_("Identifier of the dataset.")
    )
    qgis_layer_id = models.CharField(
        max_length=1000, help_text=_("Layer identifier from the source QGIS project.")
    )
    name = models.CharField(max_length=1000, help_text=_("Name of the dataset."))
    bbox = models.CharField(
        max_length=1000,
        help_text=_("Bounding box of the dataset in the source coordinate reference system."),
    )
    bbox_wgs84 = models.CharField(
        max_length=1000, help_text=_("Bounding box of the dataset transformed to WGS84.")
    )
    source = models.JSONField(
        default=dict, help_text=_("Source configuration and connection metadata of the dataset.")
    )
    styles = models.JSONField(
        default=dict, help_text=_("Rendered style definitions associated with this dataset.")
    )
    driver = models.CharField(
        max_length=50, help_text=_("Provider driver name used to access the dataset.")
    )
    crs = models.JSONField(default=dict, help_text=_("Coordinate reference system of the dataset."))
    minimum_scale = models.FloatField(
        null=True, help_text=_("Minimum scale at which the dataset is visible.")
    )
    maximum_scale = models.FloatField(
        null=True, help_text=_("Maximum scale at which the dataset is visible.")
    )
    project = models.ForeignKey(
        Project,
        on_delete=models.CASCADE,
        related_name="datasets",
        help_text=_("Project the dataset belongs to."),
    )

    objects = DatasetManager()

    def __str__(self):
        return self.name


class Vector(Dataset):
    class Meta:
        verbose_name = _("vector")
        verbose_name_plural = _("vectors")

    objects = VectorManager()

    geometry_type_simple = models.CharField(
        max_length=1000,
        help_text=_("Simplified geometry type of the vector dataset (eg. point, line, polygon)."),
    )
    geometry_type_wkb = models.CharField(
        max_length=1000, help_text=_("Geometry type of the vector dataset.")
    )


class Field(models.Model):
    class Meta:
        unique_together = (
            "name",
            "dataset",
        )
        verbose_name = _("field")
        verbose_name_plural = _("fields")

    id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, help_text=_("Identifier of the field.")
    )
    name = models.CharField(
        max_length=1000, help_text=_("Original field name from the source dataset.")
    )
    type = models.CharField(
        max_length=1000, help_text=_("Original data type from the source dataset.")
    )
    is_primary_key = models.BooleanField(
        default=False, help_text=_("Whether this field is the dataset primary key.")
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
    dataset = models.ForeignKey(
        Vector,
        on_delete=models.CASCADE,
        help_text=_("Vector dataset this field belongs to."),
        related_name="fields",
    )

    def __str__(self):
        return f"{self.alias} ({self.name})"


class Raster(Dataset):
    class Meta:
        verbose_name = _("raster")
        verbose_name_plural = _("rasters")


class Custom(Dataset):
    class Meta:
        verbose_name = _("custom")
        verbose_name_plural = _("custom")
