import uuid

from django.db import models
from django.utils.translation import gettext_lazy as _


class Organisation(models.Model):
    class Meta:
        verbose_name = _("organisation")
        verbose_name_plural = _("organisations")

    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    name = models.CharField()
    domain = models.CharField(unique=True)
    public_access = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.name} (domain: {self.domain})"
