import uuid

from django.db import models
from django.utils.translation import gettext_lazy as _

from georama.core.models.organisation import Organisation
from georama.integration.managers.project import ProjectManager


class Project(models.Model):
    ORGANISATION_FIELD_NAME = "organisation"

    class Meta:
        verbose_name = _("project")
        verbose_name_plural = _("projects")
        unique_together = (
            "name",
            "organisation",
        )

    id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, help_text=_("Identifier of the project.")
    )
    name = models.CharField(max_length=1000, help_text=_("Name of the project."))
    path = models.CharField(max_length=None, help_text=_("Path to the qgis project."), unique=True)
    qgis_version = models.CharField(
        max_length=1000, blank=True, help_text=_("QGIS version the project was created with.")
    )
    hash = models.CharField(
        max_length=20000, blank=True, help_text=_("Hash used to detect changes in project content.")
    )
    organisation = models.ForeignKey(
        Organisation,
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        related_name="projects",
        help_text=_("Organisation this project belongs to."),
    )

    objects = ProjectManager()

    def __str__(self):
        return f"{self.name}"
