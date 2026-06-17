import uuid

from django.db import models
from django.utils.translation import gettext_lazy as _

from georama.core.models.organisation import Organisation
from georama.integration.managers.collection import CollectionManager


class Collection(models.Model):
    class Meta:
        verbose_name = _("collection")
        verbose_name_plural = _("collections")

    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    name = models.CharField(max_length=1000, unique=True)
    organisation = models.ForeignKey(Organisation, null=True, blank=True, on_delete=models.CASCADE)

    objects = CollectionManager()

    def __str__(self):
        return self.name
