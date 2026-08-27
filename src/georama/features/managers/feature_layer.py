from django.db import models, transaction

from georama.core.common.managers import OrganisationalManager
from georama.features.models.field import Field


class FeatureLayerManager(OrganisationalManager):
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
            )
        )

    def bulk_create(self, *args, **kwargs):
        with transaction.atomic():
            feature_layers = super().bulk_create(*args, **kwargs)
            Field.objects.bulk_create(
                field
                for layer in feature_layers
                for field in layer.datasource_related_fields()
            )
            return feature_layers
