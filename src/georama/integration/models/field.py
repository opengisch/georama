import uuid

from django.db import models
from django.utils.translation import gettext_lazy as _

from georama.integration.models import Vector


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
        related_name="fields",
    )

    def __str__(self):
        return f"{self.alias} ({self.name})"
