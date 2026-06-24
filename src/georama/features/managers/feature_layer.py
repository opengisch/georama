from django.db import models, transaction

from georama.core.common.managers import OrganisationalManager as BaseOrganisationalManager
from georama.core.common.querysets import OrganisationalQuerySet
from georama.core.models.organisation import Organisation


class OrganisationalManager(BaseOrganisationalManager):
    def organisation_objects(self, organisation: Organisation | None) -> OrganisationalQuerySet:
        if organisation is None:
            return self.get_queryset().filter(
                datasource__project__collection__organisation__domain__isnull=True
            )
        return self.get_queryset().filter(
            datasource__project__collection__organisation__domain=organisation.domain
        )


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
                "datasource__project",
                "datasource__project__collection",
                "datasource__project__collection__organisation",
            )
        )

    def bulk_create(self, objects, *args, **kwargs):

        with transaction.atomic():
            feature_layers = super().bulk_create(*args, **kwargs)
            for feature_layer in feature_layers:
                feature_layer.fields.bulk_create(self.datasource_related_fields())
