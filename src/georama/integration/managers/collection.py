from django.db import models

from georama.core.common.managers import OrganisationalManager


class CollectionManager(OrganisationalManager):
    def get_queryset(self) -> models.QuerySet:
        """Always prefetch bound fields to reduce queries.

        Returns:
            the filtered QuerySet
        """
        return super().get_queryset()
