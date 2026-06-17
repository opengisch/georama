import uuid

from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _
from guardian.mixins import GuardianUserMixin


class GeoramaUser(AbstractUser, GuardianUserMixin):
    class Meta:
        verbose_name = _("user")
        verbose_name_plural = _("users")

    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
