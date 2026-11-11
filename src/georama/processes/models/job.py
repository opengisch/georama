from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.utils.translation import gettext
from django.utils.translation import gettext_lazy as _
from qgis_server_light.interface.dispatcher.common import JobState, Status
from qgis_server_light.interface.job.process.output import FileOutput, ProcessResult
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

User = get_user_model()


class Job(models.Model):
    ORGANISATION_FIELD_NAME = "process__organisation"

    STATUS_CODE_BY_QSL_STATUS = {
        Status.QUEUED: StatusCode.ACCEPTED,
        Status.RUNNING: StatusCode.RUNNING,
        Status.SUCCESS: StatusCode.SUCCESSFUL,
        Status.FAILURE: StatusCode.FAILED,
    }

    redis_job_id = models.UUIDField(db_index=True)
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

    @property
    def results(self) -> dict:
        return {
            output.name: self.output_value(output.value) for output in self.process_result.outputs
        }

    def output_value(self, value: FileOutput | str | int | float | bool):
        if isinstance(value, FileOutput):
            return OgcApiDictEncoder().encode(Link(href=self.results_url, type=value.media_type))
        return value

    @property
    def dataclass(self):
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
            links=[
                Link(
                    rel="self",
                    href=reverse("processes:job-detail", kwargs={"pk": self.pk}),
                    type="application/json",
                    title="Job status",
                )
            ],
        )
