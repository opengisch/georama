from django.db import models

from georama.core.common.managers import LayerManager
from georama.core.common.querysets import OrganisationalQuerySet
from georama.core.models import Organisation


class WmsLayerManager(LayerManager):
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

    def accessible_layers_queryable(
        self,
        organisation: Organisation,
        user,
        perms: list[str],
        layer_names: list[str] | None = None,
    ) -> OrganisationalQuerySet:
        qs = super().accessible_layers(organisation, user, perms, layer_names)
        return qs.filter(datasource__vector__isnull=False).filter(queryable=True)
