from django.db import models
from django.utils import timezone

from georama.core.common.managers import OrganisationalManager


class JobManager(OrganisationalManager):
    def get_queryset(self) -> models.QuerySet:
        """Always prefetch bound fields to reduce queries.

        Returns:
            the filtered QuerySet
        """
        return super().get_queryset().select_related("process", "created_by")

    def expired(self) -> models.QuerySet:
        """Jobs which outlived their `expires`.

        Returns:
            the filtered QuerySet
        """
        return self.get_queryset().filter(expires__lte=timezone.now())
