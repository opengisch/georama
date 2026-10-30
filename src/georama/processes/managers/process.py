from django.db import models

from georama.core.common.managers import PublicOrProtectedManager


class ProcessManager(PublicOrProtectedManager):
    def get_queryset(self) -> models.QuerySet:
        """Always prefetch bound fields to reduce queries.

        Returns:
            the filtered QuerySet
        """
        return (
            super()
            .get_queryset()
            .prefetch_related(
                # "jobs",
            )
        )
