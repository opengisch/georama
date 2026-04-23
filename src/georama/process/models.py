from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse

from georama.core.entities.models import PublishedAs
from georama.core.models.mixins import GeoramaPermissionMixin
from georama.core.services.permission import PermissionInterface
from georama.process.apps import central_app_label

User = get_user_model()


class Job(models.Model):
    redis_job_id = models.UUIDField(db_index=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_created=True)
    process = models.ForeignKey("Process", on_delete=models.CASCADE)
    job_parameters = models.JSONField()
    job_result = models.JSONField()

    # @property
    # def job_result(self):
    #     redis_job = qsl_redis_queue.client.get(f"job:{self.redis_job_id}")


class Process(GeoramaPermissionMixin, PublishedAs):
    published_as_type = f"{central_app_label}process"

    process_id = models.CharField(max_length=None, db_index=True)

    def get_absolute_url(self):
        return reverse(f"{central_app_label}:process-detail", kwargs={"pk": self.pk})


class PublishedAsDataset(GeoramaPermissionMixin, PublishedAs):
    published_as_type = f"{central_app_label}dataset"

    @property
    def permissions(self) -> list[PermissionInterface]:
        # No need for Update or delete with WMS...
        return self.read_permissions

    def get_absolute_url(self):
        return reverse(f"{central_app_label}:dataset-detail", kwargs={"pk": self.pk})
