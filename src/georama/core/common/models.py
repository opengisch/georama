import uuid

from django.db import models
from django.utils.translation import gettext_lazy as _


class BaseMetadata(models.Model):
    class Meta:
        abstract = True

    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        help_text=_("Identifier of the metadata."),
    )
    title = models.CharField(
        max_length=1000,
        default="",
        blank=True,
        help_text=_("The verbose title of the connected item."),
        verbose_name=_("title"),
    )
    description = models.TextField(default="", blank=True, verbose_name=_("description"))
    license = models.TextField(
        default="""
    This dataset is made available under the Open Database
    License: http://opendatacommons.org/licenses/odbl/1.0/.
    Any rights in individual contents of the database are licensed
    under the Database Contents
    License: http://opendatacommons.org/licenses/dbcl/1.0/
    """,
        verbose_name=_("license"),
    )
    fees = models.TextField(default="No fees apply.", verbose_name=_("fees"))
    access_constraints = models.TextField(
        default="No access constraints apply.", verbose_name=_("access constraints")
    )
