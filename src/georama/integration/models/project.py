import uuid

from django.conf import settings
from django.db import models
from django.utils.translation import gettext_lazy as _

from georama.integration.managers.project import ProjectManager
from georama.integration.models.collection import Collection


class Project(models.Model):
    class Meta:
        verbose_name = _("project")
        verbose_name_plural = _("projects")

    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    name = models.CharField(max_length=1000)
    version = models.CharField(max_length=1000, blank=True)
    hash = models.CharField(max_length=20000, blank=True)
    collection = models.ForeignKey(
        Collection,
        on_delete=models.CASCADE,
    )
    integrated_at = models.DateTimeField(auto_now=True)
    integrated_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        editable=False,
        null=True,
        on_delete=models.SET_NULL,
    )
    integrated_by_name = models.CharField(max_length=150, null=False, editable=False)

    objects = ProjectManager()

    def __str__(self):
        return f"{self.name} ({_('collection').title()}: {self.collection.name})"
