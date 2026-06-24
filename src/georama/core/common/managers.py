from django.db import models

from georama.core.common.querysets import OrganisationalQuerySet
from georama.core.models.organisation import Organisation


class OrganisationalManager(models.Manager.from_queryset(OrganisationalQuerySet)):
    """
    Manager to be used in context of models bound to organisations to easy handling
    of those.
    """

    def get_queryset(self) -> OrganisationalQuerySet:
        """Always prefetch bound fields to reduce queries.

        Returns:
            the filtered QuerySet
        """
        qs = super().get_queryset()
        return qs.prefetch_related(qs.get_model_organisation_field())

    def organisation_objects(self, organisation: Organisation | None) -> OrganisationalQuerySet:
        """Filters for objects bound to passed organisation. Organisation `None`
        means the _global_ organisation.

        Returns:
            the filtered QuerySet
        """
        return self.get_queryset().organisation_objects(organisation)
