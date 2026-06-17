from django.db import models

from georama.core.common.querysets import OrganisationalQuerySet
from georama.core.models.organisation import Organisation


class OrganisationalManager(models.Manager.from_queryset(OrganisationalQuerySet)):
    """
    Manager to be used in context of models bound to organisations to easy handling
    of those.
    """

    def organisation_objects(self, organisation: Organisation | None) -> OrganisationalQuerySet:
        """Filters for objects bound to passed organisation. Organisation `None`
        means the _global_ organisation.

        Returns:
            the filtered QuerySet
        """
        return self.get_queryset().organisation_objects(organisation)
