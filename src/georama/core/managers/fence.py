from georama.core.common.managers import OrganisationalManager
from georama.core.common.querysets import OrganisationalQuerySet


class FenceManager(OrganisationalManager):
    def get_queryset(self) -> OrganisationalQuerySet:
        """Always prefetch bound fields to reduce queries.

        Returns:
            the filtered QuerySet
        """
        return super().get_queryset().prefetch_related("organisation")
