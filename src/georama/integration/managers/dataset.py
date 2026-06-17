from django.db import models


class DatasetManager(models.Manager):
    def get_queryset(self) -> models.QuerySet:
        """Always prefetch bound fields to reduce queries.

        Returns:
            the filtered QuerySet
        """
        return super().get_queryset().prefetch_related("vector", "raster", "custom", "project")


class VectorManager(models.Manager):
    def get_queryset(self) -> models.QuerySet:
        """Always prefetch bound fields to reduce queries.

        Returns:
            the filtered QuerySet
        """
        return super().get_queryset().prefetch_related("fields")
