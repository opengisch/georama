from django.db import models
from django.utils.translation import gettext_lazy as _

from georama.core.models.fence import Fence


class GeoramaObjectPermissionAuditAbstract(models.Model):
    assigned_at = models.DateTimeField(
        auto_now=True,
        help_text=_("Date and time when the object permission was assigned at."),
    )

    class Meta:
        abstract = True


class GeoramaObjectPermissionFenceAbstract(models.Model):
    fences = models.ManyToManyField(
        Fence,
        blank=True,
        help_text=_("Fences limiting where this object permission is effective."),
    )

    class Meta:
        abstract = True
