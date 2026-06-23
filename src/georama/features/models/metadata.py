import uuid

from django.db import models
from django.utils.translation import gettext_lazy as _

from georama.features.models.feature_layer import FeatureLayer


class Metadata(models.Model):
    ON_EXCEED_CHOICES = (
        ("ERROR", "error"),
        ("THROTTLE", "throttle"),
    )

    class Meta:
        verbose_name = _("metadata")
        verbose_name_plural = _("metadata")

    id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, help_text=_("Identifier of the metadata.")
    )
    default_items = models.IntegerField(default=10, null=True)
    max_items = models.IntegerField(default=500, null=True)
    on_exceed = models.CharField(
        default="ERROR", choices=ON_EXCEED_CHOICES, max_length=10, null=True
    )
    feature_layer = models.OneToOneField(
        FeatureLayer,
        related_name="metadata",
        on_delete=models.CASCADE,
    )
