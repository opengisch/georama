import base64
import logging
import math
import uuid
from datetime import datetime
from pathlib import Path

from django.conf import settings
from django.db import models
from django.db.models import QuerySet
from django.templatetags.static import static
from django.utils.translation import gettext_lazy as _
from qgis_server_light.interface.common import BBox
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
        primary_key=True,
        default=uuid.uuid4,
        help_text=_("Identifier of the project."),
    )
    name = models.CharField(
        max_length=1000, help_text=_("Name of the project."), verbose_name=_("name")
    )
    path = models.CharField(
        max_length=None, help_text=_("Path to the qgis project."), verbose_name=_("path")
    )
    qgis_version = models.CharField(
        max_length=1000,
        blank=True,
        help_text=_("QGIS version the project was created with."),
        verbose_name=_("QGIS version"),
    )
    config = models.JSONField(
        blank=True,
        help_text=_(
            "The JSON config representation of the QGIS Project which was created by "
            "the QGIS-Server-Light exporter"
        ),
        verbose_name=_("configuration"),
    )
    organisation = models.ForeignKey(
        Organisation,
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        related_name="projects",
        help_text=_("Organisation this project belongs to."),
        verbose_name=_("organisation"),
    )
    integrated_at = models.DateTimeField(
        auto_now_add=True,
        help_text=_("The point in time when the project was created last time."),
        verbose_name=_("integrated at"),
    )
    preview = models.BinaryField(
        null=True,
        blank=True,
        help_text=_("Preview image of the project."),
        verbose_name=_("preview"),
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
        """Checks if the corresponding QGIS project file was not modified since integration."""
        qp_fmd = self.qgis_project_file_modification_date
        if qp_fmd is None:
            return False
        return self.integrated_at.timestamp() > qp_fmd.timestamp()

    @property
    def project_file(self) -> QgisProject:
        return QgisProject(path=Path(self.path), organisation=self.organisation_folder)

    @property
    def qsl_job_layers_and_extent(self) -> tuple[list, BBox]:
        """Convert datasources to QSL job layers in render order and collect their WGS84 extent.

        This uses the project's tree structure to determine the correct render order,
        same as themes do. Returns layers and their combined WGS84 extent
        (excluding background layers).

        Returns:
            Tuple of (layers list, combined WGS84 extent as BBox)
        """
        layers = []
        bbox = BBox(x_min=math.inf, y_min=math.inf, x_max=-math.inf, y_max=-math.inf)
        config = self.config_as_dataclass

        def collect(group):
            for child in group.children:
                subgroup = config.tree.find_by_name(child)
                if subgroup:
                    if subgroup.is_checked:
                        collect(subgroup)
                else:
                    dataset = config.datasets.find_dataset_by_id(child)
                    if dataset is None:
                        continue
                    if dataset.is_spatial and dataset.is_checked:
                        # Find the datasource for this dataset
                        ds_qs = self.datasources.filter(qgis_layer_id=dataset.id)
                        try:
                            datasource = ds_qs.get()
                            layers.append(datasource.to_qsl_job_layer())
                            # Collect extent from non-background layers
                            if not dataset.is_background:
                                extent_wgs84 = datasource.bbox_wgs84
                                if extent_wgs84:
                                    ds_bbox = BBox.from_string(extent_wgs84)
                                    bbox.x_min = min(ds_bbox.x_min, bbox.x_min)
                                    bbox.y_min = min(ds_bbox.y_min, bbox.y_min)
                                    bbox.x_max = max(ds_bbox.x_max, bbox.x_max)
                                    bbox.y_max = max(ds_bbox.y_max, bbox.y_max)
                        except self.datasources.model.DoesNotExist:
                            continue

        collect(config.tree.root)
        return layers, bbox

    async def generate_preview_image(self) -> bytes | None:
        """Generate preview image for this project (renders all datasources in render order).

        Uses WGS84 extent collected from all visible layers, rendering in EPSG:4326.

        Returns:
            The png or `None` if the job could not be created.
        """
        from asgiref.sync import sync_to_async

        from georama.core.qsl_utils import render_image

        # Get layers and their combined WGS84 extent
        layers, bbox = await sync_to_async(lambda: self.qsl_job_layers_and_extent)()

        if not layers:
            logging.warning(f"No datasources found for project {self.name}")
            return None

        if any(math.isinf(n) for n in bbox.to_2d_list()):
            logging.warning(f"Could not determine valid extent for project {self.name}")
            return None

        # WGS84 coordinates are swapped
        bbox = BBox(x_min=bbox.y_min, y_min=bbox.x_min, x_max=bbox.y_max, y_max=bbox.x_max)

        return await render_image(
            layers,
            bbox,
            "EPSG:4326",
            250,
            250,
        )

    @property
    def preview_image(self) -> str:
        """Return the preview image as a base64-encoded data URL or a fallback static image.

        Returns:
            The data encoded preview image or the absolute path to the static fallback image.
        """
        if self.preview is not None:
            return f"data:image/png;base64,{base64.b64encode(self.preview).decode()}"
        return static("integration/images/qgis.png")
