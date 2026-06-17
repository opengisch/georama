import uuid

from django.contrib.gis.db.models import MultiPolygonField
from django.db import models
from django.utils.translation import gettext_lazy as _

from georama.core.managers.fence import FenceManager
from georama.core.models.organisation import Organisation


class Fence(models.Model):
    class Meta:
        verbose_name = _("fence")
        verbose_name_plural = _("fences")

    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    name = models.CharField()
    geometry = MultiPolygonField()
    organisation = models.ForeignKey(
        Organisation, null=True, blank=True, on_delete=models.CASCADE, related_name="fences"
    )
    objects = FenceManager()
