import uuid
from datetime import datetime
from pathlib import Path

from django.conf import settings
from django.db import models
from django.db.models import QuerySet
from django.utils.translation import gettext_lazy as _
from qgis_server_light.interface.exporter.extract import Config
from xsdata.formats.dataclass.parsers import DictDecoder
from xsdata.formats.dataclass.parsers.config import ParserConfig

from georama.core.models.organisation import Organisation
from georama.integration.lib.qgis_project_file_structure import QgisProject
from georama.integration.managers.project import ProjectManager


class Project(models.Model):
    ORGANISATION_FIELD_NAME = "organisation"

    class Meta:
        verbose_name = _("Project")
        verbose_name_plural = _("Projects")
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
        max_length=1000,
        blank=True,
        help_text=_("QGIS version the project was created with."),
    )
    config = models.JSONField(
        blank=True,
        help_text=_(
            "The JSON config representation of the QGIS Project which was created by "
            "the QGIS-Server-Light exporter"
        ),
    )
    organisation = models.ForeignKey(
        Organisation,
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        related_name="projects",
        help_text=_("Organisation this project belongs to."),
    )
    integrated_at = models.DateTimeField(
        auto_now_add=True,
        help_text=_("The point in time when the project was created last time."),
    )

    objects = ProjectManager()

    def __str__(self):
        return f"{self.name}"

    @property
    def config_as_dataclass(self):
        decoder_config = ParserConfig(fail_on_unknown_properties=False)
        return DictDecoder(decoder_config).decode(self.config, Config)

    @property
    def datasources_sorted_by_name(self) -> QuerySet:
        return self.datasources.order_by("name").all()

    @property
    def organisation_folder(self) -> str:
        if self.organisation:
            return self.organisation.domain
        return settings.DATA_INTEGRATION_GLOBAL_ORGANISATION_FOLDER

    @property
    def qgis_project_file_modification_date(self) -> datetime | None:
        return self.project_file.modification_date

    @property
    def qgis_project_file_exists(self) -> bool:
        return self.project_file.exists

    @property
    def up_to_date(self) -> bool:
        """Checks if the corresponding"""
        qp_fmd = self.qgis_project_file_modification_date
        if qp_fmd is None:
            return False
        return self.integrated_at.timestamp() > qp_fmd.timestamp()

    @property
    def project_file(self) -> QgisProject:
        return QgisProject(path=Path(self.path), organisation=self.organisation_folder)
