from datetime import timedelta
from pathlib import Path

from django.conf import settings


class Config:
    @property
    def sync_execute_timeout(self) -> float:
        """Timeout in seconds."""
        return settings.PROCESSES_SYNC_EXECUTE_TIMEOUT

    @property
    def job_expire(self) -> timedelta:
        return timedelta(seconds=settings.PROCESSES_JOB_EXPIRE)

    @property
    def output_dir(self) -> Path:
        return Path(settings.PROCESSES_OUTPUT_DIR)
