import uuid

from django.contrib.gis.db.models import MultiPolygonField
from django.db import models
from django.utils.translation import gettext_lazy as _

from georama.core.common.managers import OrganisationalManager
from georama.core.models.organisation import Organisation


class Fence(models.Model):
    ORGANISATION_FIELD_NAME = "organisation"

    class Meta:
        verbose_name = _("fence")
        verbose_name_plural = _("fences")

    id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, help_text=_("Identifier of the fence.")
    )
    name = models.CharField(help_text=_("Name of the fence."))
    geometry = MultiPolygonField(help_text=_("Geographic boundary of the fence."))
    organisation = models.ForeignKey(
        Organisation,
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        related_name="fences",
        help_text=_("Organisation the fence belongs to."),
    )
    objects = OrganisationalManager()
