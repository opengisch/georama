import shutil
import uuid
from collections.abc import Callable
from pathlib import Path

from django.contrib.auth import get_user_model
from django.db import models, transaction
from django.urls import reverse
from django.utils import timezone
from django.utils.translation import gettext
from django.utils.translation import gettext_lazy as _
from qgis_server_light.interface.dispatcher.common import JobState, Status
from qgis_server_light.interface.job.process.output import (
    ProcessResult,
    Reference,
    ResultOutput,
)
from xsdata.formats.dataclass.parsers import DictDecoder, JsonParser
from xsdata.formats.dataclass.serializers import DictEncoder

from georama.processes.interface.ogc_api.processes.part1.v_100.main import (
    Job as OgcJob,
)
from georama.processes.interface.ogc_api.processes.part1.v_100.main import (
    Link,
    StatusCode,
)
from georama.processes.interface.ogc_api.processes.part1.v_100.serializers import (
    OgcApiDictEncoder,
)
from georama.processes.managers.job import JobManager
from georama.processes.processes_config import Config

User = get_user_model()


class Job(models.Model):
    ORGANISATION_FIELD_NAME = "process__organisation"

    STATUS_CODE_BY_QSL_STATUS = {
        Status.QUEUED: StatusCode.ACCEPTED,
        Status.RUNNING: StatusCode.RUNNING,
        Status.SUCCESS: StatusCode.SUCCESSFUL,
        Status.FAILURE: StatusCode.FAILED,
    }

    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        help_text=_("Identifier of the job, also used as job id in QGIS-Server-Light."),
    )
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_created=True)
    process = models.ForeignKey("Process", on_delete=models.CASCADE)
    job_parameters = models.JSONField()
    job_result = models.JSONField(null=True)
    status = models.CharField(
        max_length=16,
        choices=[(status_code.value, status_code.value) for status_code in StatusCode],
        default=StatusCode.ACCEPTED.value,
    )
    message = models.TextField(null=True, blank=True)
    progress = models.PositiveSmallIntegerField(null=True, blank=True)
    finished = models.DateTimeField(null=True, blank=True)
    updated = models.DateTimeField(null=True, blank=True)
    expires = models.DateTimeField()

    objects = JobManager()

    class Meta:
        verbose_name = f"{_('Job')}"
        verbose_name_plural = f"{_('Jobs')}"

    def __str__(self):
        return str(self.id)

    @property
    def title(self):
        return self.process.title

    @property
    def is_finished(self) -> bool:
        return self.status in (StatusCode.SUCCESSFUL, StatusCode.FAILED, StatusCode.DISMISSED)

    def apply_state(self, job_state: JobState | None):
        self.updated = timezone.now()
        if job_state is None:
            self.status = StatusCode.FAILED.value
            self.message = gettext("The job is not known to the process-workers anymore.")
        else:
            self.status = self.STATUS_CODE_BY_QSL_STATUS[job_state.status].value
            self.message = job_state.message
            if job_state.result is not None:
                process_result = JsonParser().from_bytes(job_state.result.data, ProcessResult)
                self.job_result = DictEncoder().encode(process_result)
        if self.is_finished and self.finished is None:
            self.finished = self.updated

    @property
    def process_result(self) -> ProcessResult | None:
        if self.job_result is None:
            return None
        return DictDecoder().decode(self.job_result, ProcessResult)

    @property
    def results_url(self) -> str:
        return reverse("processes:job-results", kwargs={"pk": self.pk})

    def output_url(self, output_id: str) -> str:
        return reverse("processes:job-output", kwargs={"pk": self.pk, "output_id": output_id})

    def results(self, absolute_uri: Callable[[str], str]) -> dict:
        # the results of OGC API - Processes are a map by output id, QSL ships a list
        return {
            output.id: self.output_value(output, absolute_uri)
            for output in self.process_result.outputs
        }

    def output_value(self, output: ResultOutput, absolute_uri: Callable[[str], str]):
        if isinstance(output.value, Reference):
            # the reference is relative to the output dir, the client gets the download url
            return OgcApiDictEncoder().encode(
                Link(href=absolute_uri(self.output_url(output.id)), type=output.value.type)
            )
        return output.value

    def reference(self, output_id: str) -> Reference | None:
        if self.status != StatusCode.SUCCESSFUL:
            return None
        for output in self.process_result.outputs:
            if output.id == output_id and isinstance(output.value, Reference):
                return output.value
        return None

    @property
    def output_dir(self) -> Path:
        # the process-workers write every job into its own dir named by the job id
        return Config().output_dir / str(self.id)

    @staticmethod
    def remove_output_dir(sender, instance: "Job", **kwargs):
        # connected to post_delete, so cascades and queryset deletes take the dir along too
        output_dir = instance.output_dir
        # a rolled back delete keeps its files
        transaction.on_commit(lambda: shutil.rmtree(output_dir, ignore_errors=True))

    @staticmethod
    def reference_path(reference: Reference) -> Path | None:
        output_dir = Config().output_dir.resolve()
        path = (output_dir / reference.href).resolve()
        # the path comes from the worker, still a file outside the output dir is never served
        if not path.is_relative_to(output_dir):
            return None
        return path

    def status_info(self, absolute_uri: Callable[[str], str]) -> OgcJob:
        links = [
            Link(
                rel="self",
                href=absolute_uri(reverse("processes:job-detail", kwargs={"pk": self.pk})),
                type="application/json",
                title="Job status",
            )
        ]
        if self.status == StatusCode.SUCCESSFUL:
            links.append(
                Link(
                    rel="http://www.opengis.net/def/rel/ogc/1.0/results",
                    href=absolute_uri(self.results_url),
                    type="application/json",
                    title="Job results",
                )
            )
            # the files can be downloaded right from the status, without the results first
            links.extend(
                Link(
                    rel="enclosure",
                    href=absolute_uri(self.output_url(output.id)),
                    type=output.value.type,
                    title=output.id,
                )
                for output in self.process_result.outputs
                if isinstance(output.value, Reference)
            )
        return OgcJob(
            type="process",
            job_id=str(self.pk),
            process_id=self.process.algorithm_id,
            status=StatusCode(self.status),
            message=self.message,
            progress=self.progress,
            created=self.created_at,
            finished=self.finished,
            updated=self.updated,
            links=links,
        )
