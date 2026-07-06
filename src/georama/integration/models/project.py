import uuid

from django.db import models
from django.utils.translation import gettext_lazy as _

from django.conf import settings
from georama.core.models.organisation import Organisation
from georama.integration.managers.project import ProjectManager
from georama.integration.lib.qgis_project_file_structure import QgisProject


class Project(models.Model):
    ORGANISATION_FIELD_NAME = "organisation"

    class Meta:
        verbose_name = _("project")
        verbose_name_plural = _("projects")
        unique_together = (
            "organisation",
            "path",
        )

    id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, help_text=_("Identifier of the project.")
    )
    name = models.CharField(max_length=1000, help_text=_("Name of the project."))
    path = models.CharField(max_length=None, help_text=_("Path to the qgis project."))
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

    @property
    def datasources_sorted_by_name(self):
        return self.datasources.order_by('name').all()

    @property
    def organisation_folder(self):
        if self.organisation:
            return self.organisation.domain
        return settings.DATA_INTEGRATION_GLOBAL_ORGANISATION_FOLDER

    @property
    def modification_date(self):
        return QgisProject(path=self.path, organisation=self.organisation_folder).modification_date
