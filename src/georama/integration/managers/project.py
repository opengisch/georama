from django.db import models


class ProjectManager(models.Manager):
    def get_queryset(self) -> models.QuerySet:
        """Always prefetch bound fields to reduce queries.

        Returns:
            the filtered QuerySet
        """
        return super().get_queryset().prefetch_related("datasets", "collection")
