import uuid

from django.db import models
from django.utils.translation import gettext_lazy as _

from georama.integration.models.datasource import Field as DatasourceField


class Field(models.Model):
    class Meta:
        verbose_name = _("field")
        verbose_name_plural = _("fields")
        unique_together = (
            "feature_layer",
            "datasource_field",
        )
        unique_together = (
            "feature_layer",
            "name",
        )

    id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, help_text=_("Identifier of the field.")
    )
    feature_layer = models.ForeignKey(
        "FeatureLayer",
        related_name="fields",
        related_query_name="field",
        on_delete=models.CASCADE,
    )
    datasource_field = models.ForeignKey(
        DatasourceField,
        related_name="feature_layer_fields",
        related_query_name="feature_layer_field",
        on_delete=models.CASCADE,
    )
    name = models.CharField(max_length=None)
    visible = models.BooleanField(default=False)
