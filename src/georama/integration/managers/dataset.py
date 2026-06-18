from django.db import models

from georama.core.common.managers import OrganisationalManager


class DatasetManager(OrganisationalManager):
    def get_queryset(self) -> models.QuerySet:
        """Always prefetch bound fields to reduce queries.

        Returns:
            the filtered QuerySet
        """
        return (
            super()
            .get_queryset()
            .prefetch_related(
                "vector",
                "raster",
                "custom",
                "project",
                "project__collection",
                "project__collection__organisation",
            )
        )


class VectorManager(OrganisationalManager):
    def get_queryset(self) -> models.QuerySet:
        """Always prefetch bound fields to reduce queries.

        Returns:
            the filtered QuerySet
        """
        return (
            super()
            .get_queryset()
            .prefetch_related(
                "fields", "project", "project__collection", "project__collection__organisation"
            )
        )
