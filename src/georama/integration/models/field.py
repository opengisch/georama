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
