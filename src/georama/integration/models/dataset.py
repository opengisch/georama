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

    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    qgis_layer_id = models.CharField(max_length=1000)
    name = models.CharField(max_length=1000)
    bbox = models.CharField(max_length=1000)
    bbox_wgs84 = models.CharField(max_length=1000)
    source = models.JSONField(default=dict)
    styles = models.JSONField(default=dict)
    driver = models.CharField(max_length=50)
    crs = models.JSONField(default=dict)
    minimum_scale = models.FloatField(null=True)
    maximum_scale = models.FloatField(null=True)
    project = models.ForeignKey(
        Project,
        on_delete=models.CASCADE,
    )

    objects = DatasetManager()

    def __str__(self):
        return self.name


class Vector(Dataset):
    class Meta:
        verbose_name = _("vector")
        verbose_name_plural = _("vectors")

    objects = VectorManager()

    geometry_type_simple = models.CharField(max_length=1000)
    geometry_type_wkb = models.CharField(max_length=1000)


class Field(models.Model):
    class Meta:
        unique_together = (
            "name",
            "dataset",
        )
        verbose_name = _("field")
        verbose_name_plural = _("fields")

    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    name = models.CharField(max_length=1000)
    type = models.CharField(max_length=1000)
    is_primary_key = models.BooleanField(default=False)
    type_wfs = models.CharField(max_length=1000)
    type_oapif = models.CharField(max_length=1000)
    type_oapif_format = models.CharField(max_length=1000)
    alias = models.CharField(max_length=1000)
    comment = models.CharField(max_length=1000)
    nullable = models.BooleanField(default=True)
    length = models.IntegerField(null=True)
    precision = models.IntegerField(null=True)
    dataset = models.ForeignKey(
        Vector,
        on_delete=models.CASCADE,
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
