from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _

from georama.processes.interface.ogc_api.processes.part1.v_100.main import (
    Job as OgcJob,
)
from georama.processes.interface.ogc_api.processes.part1.v_100.main import (
    Link,
)
from georama.processes.managers.job import JobManager

User = get_user_model()


class Job(models.Model):
    ORGANISATION_FIELD_NAME = "process__organisation"

    redis_job_id = models.UUIDField(db_index=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_created=True)
    process = models.ForeignKey("Process", on_delete=models.CASCADE)
    job_parameters = models.JSONField()
    job_result = models.JSONField(null=True)

    objects = JobManager()

    class Meta:
        verbose_name = f"{_('Job')}"
        verbose_name_plural = f"{_('Jobs')}"

    # @property
    # def job_result(self):
    #     redis_job = qsl_redis_queue.client.get(f"job:{self.redis_job_id}")

    @property
    def title(self):
        return self.process.title

    @property
    def dataclass(self):
        return OgcJob(
            type="process",
            job_id=str(self.pk),
            process_id=str(self.process_id),
            status="accepted",
            message="Placeholder job status",
            progress=0,
            created=self.created_at,
            started=self.created_at,
            finished=self.created_at,
            updated=self.created_at,
            links=[
                Link(
                    rel="self",
                    href=reverse("processes:job-detail", kwargs={"pk": self.pk}),
                    type="application/json",
                    title="Job status",
                )
            ],
        )
