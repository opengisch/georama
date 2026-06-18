import uuid

from django.db import models
from django.utils.translation import gettext_lazy as _

from georama.core.models.organisation import Organisation
from georama.integration.managers.collection import CollectionManager


class Collection(models.Model):
    class Meta:
        verbose_name = _("collection")
        verbose_name_plural = _("collections")
        unique_together = (
            "name",
            "organisation",
        )

    id = models.UUIDField(
        primary_key=True, default=uuid.uuid4,
        help_text=_("Identifier of the collection.")
    )
    name = models.CharField(
        max_length=1000, help_text=_("Unique name of the collection.")
    )
    organisation = models.ForeignKey(
        Organisation,
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        help_text=_("Organisation that owns this collection."),
    )

    objects = CollectionManager()

    def __str__(self):
        return self.name
