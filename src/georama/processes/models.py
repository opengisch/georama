from functools import cached_property
from typing import Self

from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse
from django.utils.translation import gettext
from django.utils.translation import gettext_lazy as _
from qgis_server_light.interface.exporter.extract import Algorithm

from georama.core.entities.models import PublishedAs
from georama.core.models.mixins import GeoramaPermissionMixin
from georama.core.services.permission import PermissionInterface
from georama.data_integration.models import CustomDataSet, RasterDataSet, VectorDataSet
from georama.processes.apps import central_app_label, qsl_available_processes
from georama.processes.interface.ogc_api.v_100.processes import (
    JobControlOptions,
    Link,
    ProcessBase,
    TransmissionMode,
)

User = get_user_model()


class Job(GeoramaPermissionMixin):
    redis_job_id = models.UUIDField(db_index=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_created=True)
    process = models.ForeignKey("PublishedAsProcess", on_delete=models.CASCADE)
    job_parameters = models.JSONField()
    job_result = models.JSONField()

    # @property
    # def job_result(self):
    #     redis_job = qsl_redis_queue.client.get(f"job:{self.redis_job_id}")


class PublishedAsProcess(GeoramaPermissionMixin, PublishedAs):
    class Meta:
        verbose_name = f"{_('Process')}"
        verbose_name_plural = f"{_('Processes')}"
        permissions = [("can_manage_object_permissions", "Can manage object permissions")]

    published_as_type = f"{central_app_label}process"

    process_id = models.CharField(max_length=None, db_index=True, unique=True)

    def get_absolute_url(self):
        return reverse(f"{central_app_label}:process-detail", kwargs={"pk": self.pk})

    @cached_property
    def qsl_algorithm(self) -> Algorithm:
        return qsl_available_processes.algorithm_by_id(self.process_id)

    @property
    def permissions(self) -> list[PermissionInterface]:
        return self.read_permissions

    @property
    def title(self):
        return self.qsl_algorithm.display_name

    @property
    def description(self) -> str:
        return self.qsl_algorithm.short_description

    @property
    def help(self) -> str:
        return self.qsl_algorithm.short_help_string

    @property
    def dataclass(self: Self):
        return ProcessBase(
            id=self.process_id,
            description=self.qsl_algorithm.short_help_string,
            job_control_options=[JobControlOptions.SYNC],
            output_transmission=[TransmissionMode.VALUE],
            title=self.qsl_algorithm.display_name,
            version="1.0.0",
            links=[
                Link(
                    type="application/json",
                    rel="self",
                    href=reverse(
                        f"{central_app_label}:api-process-detail",
                        kwargs={"process_id": self.process_id},
                    ),
                    href_lang="en",
                    title=gettext("Process execution"),
                ),
                Link(
                    type="application/json",
                    rel="execution",
                    href=reverse(
                        f"{central_app_label}:api-process-execution",
                        kwargs={"process_id": self.process_id},
                    ),
                    href_lang="en",
                    title=gettext("Process execution"),
                ),
            ],
        )


class PublishedAsDataset(GeoramaPermissionMixin, PublishedAs):
    class Meta:
        verbose_name = f"{_('Dataset')}"
        verbose_name_plural = f"{_('Datasets')}"
        permissions = [("can_manage_object_permissions", "Can manage object permissions")]

    published_as_type = f"{central_app_label}dataset"

    raster_dataset = models.ForeignKey(
        RasterDataSet,
        # TODO: this seems wrong => only because error:
        #  It is impossible to add a non-nullable field 'dataset' to ... without
        #  specifying a default. This is because the database needs something
        #  to populate existing rows.
        null=True,
        related_name="published_oapip_dataset",
        related_query_name="published_oapip_dataset",
        on_delete=models.CASCADE,
    )
    vector_dataset = models.ForeignKey(
        VectorDataSet,
        # TODO: this seems wrong => only because error:
        #  It is impossible to add a non-nullable field 'dataset' to ... without
        #  specifying a default. This is because the database needs something
        #  to populate existing rows.
        null=True,
        related_name="published_oapip_dataset",
        related_query_name="published_oapip_dataset",
        on_delete=models.CASCADE,
    )
    custom_dataset = models.ForeignKey(
        CustomDataSet,
        # TODO: this seems wrong => only because error:
        #  It is impossible to add a non-nullable field 'dataset' to ... without
        #  specifying a default. This is because the database needs something
        #  to populate existing rows.
        null=True,
        related_name="published_oapip_dataset",
        related_query_name="published_oapip_dataset",
        on_delete=models.CASCADE,
    )

    @property
    def bound_dataset(self) -> VectorDataSet | RasterDataSet | CustomDataSet:
        if isinstance(self.raster_dataset, RasterDataSet):
            return self.raster_dataset
        elif isinstance(self.vector_dataset, VectorDataSet):
            return self.vector_dataset
        elif isinstance(self.custom_dataset, CustomDataSet):
            return self.custom_dataset
        else:
            raise NotImplementedError(
                "linked dataset has to be RasterDataSet|VectorDataSet|CustomDataSet!"
            )

    @property
    def permissions(self) -> list[PermissionInterface]:
        return self.read_permissions

    def get_absolute_url(self):
        return reverse(f"{central_app_label}:dataset-detail", kwargs={"pk": self.pk})
