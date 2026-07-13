from django.db import models

from georama.core.common.managers import OrganisationalManager


class WmsLayerManager(OrganisationalManager):
    def get_queryset(self) -> models.QuerySet:
        """Always prefetch bound fields to reduce queries.

        Returns:
            the filtered QuerySet
        """
        return (
            super()
            .get_queryset()
            .prefetch_related(
                "metadata",
                "datasource",
                "datasource__vector",
                "datasource__raster",
                "datasource__custom",
            )
        )
