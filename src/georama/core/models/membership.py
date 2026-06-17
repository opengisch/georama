import uuid

from django.db import models
from django.utils.translation import gettext_lazy as _

from georama.core.managers.membership import MembershipManager
from georama.core.models.organisation import Organisation
from georama.core.models.user import GeoramaUser


class Membership(models.Model):
    class Meta:
        verbose_name = _("membership")
        verbose_name_plural = _("memberships")
        unique_together = (
            "organisation",
            "user",
        )

    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    user = models.ForeignKey(GeoramaUser, on_delete=models.CASCADE, related_name="memberships")
    organisation = models.ForeignKey(
        Organisation, on_delete=models.CASCADE, blank=True, null=True, related_name="memberships"
    )

    objects = MembershipManager()

    def __str__(self):
        return f"{self.organisation.name if self.organisation else 'GLOBAL'} => {self.user}"
