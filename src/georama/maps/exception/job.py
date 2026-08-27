from georama.core.exceptions.base import GeoramaBaseError


class JobHandlingBaseError(GeoramaBaseError):
    def __init__(self, message="Job execution failed", job_id=None):
        self.job_id = job_id
        super().__init__(message)

    def __str__(self):
        base = super().__str__()
        if self.job_id:
            return f"[Job {self.job_id}] {base}"
        return base


class UnexpectedBehaviourError(JobHandlingBaseError):
    def __init__(
        self, message="Something unexpected happened while job execution", job_id=None
    ):
        super().__init__(message=message, job_id=job_id)


class JobExecutionError(JobHandlingBaseError):
    pass
