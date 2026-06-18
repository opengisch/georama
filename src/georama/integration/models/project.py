import uuid

from django.db import models
from django.utils.translation import gettext_lazy as _

from georama.integration.managers.project import ProjectManager
from georama.integration.models.collection import Collection


class Project(models.Model):
    class Meta:
        verbose_name = _("project")
        verbose_name_plural = _("projects")

    id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, help_text=_("Identifier of the project.")
    )
    name = models.CharField(max_length=1000, help_text=_("Name of the project."))
    qgis_version = models.CharField(
        max_length=1000, blank=True, help_text=_("QGIS version the project was created with.")
    )
    hash = models.CharField(
        max_length=20000, blank=True, help_text=_("Hash used to detect changes in project content.")
    )
    collection = models.ForeignKey(
        Collection,
        on_delete=models.CASCADE,
        help_text=_("Collection this project belongs to actually."),
    )

    objects = ProjectManager()

    def __str__(self):
        return f"{self.name} ({_('collection').title()}: {self.collection.name})"
