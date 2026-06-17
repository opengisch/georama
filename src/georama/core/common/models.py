from django.db import models

from georama.core.models.fence import Fence


class GeoramaObjectPermissionAuditAbstract(models.Model):
    assigned_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class GeoramaObjectPermissionFenceAbstract(models.Model):
    fences = models.ManyToManyField(Fence, blank=True)

    class Meta:
        abstract = True
