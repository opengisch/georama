import uuid

from django.db import models
from django.utils.translation import gettext_lazy as _


class Organisation(models.Model):
    class Meta:
        verbose_name = _("organisation")
        verbose_name_plural = _("organisations")

    id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, help_text=_("Identifier of the organisation.")
    )
    name = models.CharField(help_text=_("Name of the organisation."))
    domain = models.CharField(unique=True, help_text=_("Domain used to identify the organisation."))
    public_access = models.BooleanField(
        default=False, help_text=_("Whether anonymous users can access this organisation.")
    )

    def __str__(self):
        return f"{self.name} (domain: {self.domain})"
