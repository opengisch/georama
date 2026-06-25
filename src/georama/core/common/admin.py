from unfold.admin import ModelAdmin

from georama.core.common.querysets import OrganisationalQuerySet
from georama.core.common.request import GeoramaHttpRequest


class OrganisationalModelAdmin(ModelAdmin):
    """
    Model admin which uses organisational bound tables to filter automatically for
    only organisations defined by the request.
    """

    def get_queryset(self, request: GeoramaHttpRequest):
        """
        The queryset is automatically filtered by the organisation.

        Args:
            request: The normal django.http.HttpRequest which is extended by the
                georama.core.middleware.organisation.OrganisationMiddleware with the
                georama_organisation attribute.
        Returns:
            The filtered queryset.
        """
        qs: OrganisationalQuerySet = super().get_queryset(request)
        return qs.organisation_objects(request.georama_organisation)
