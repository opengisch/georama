from drf_spectacular.plumbing import build_mock_request as original_build_mock_request
from rest_framework import viewsets
from rest_framework.permissions import DjangoModelPermissions

from georama.core.common.request import GeoramaDrfRequest


class GeoramaModelPermissions(DjangoModelPermissions):
    """A permission which also checks view permission on read endpoints."""

    perms_map = {
        "GET": ["%(app_label)s.view_%(model_name)s"],
        "OPTIONS": ["%(app_label)s.view_%(model_name)s"],
        "HEAD": ["%(app_label)s.view_%(model_name)s"],
        "POST": ["%(app_label)s.add_%(model_name)s"],
        "PUT": ["%(app_label)s.change_%(model_name)s"],
        "PATCH": ["%(app_label)s.change_%(model_name)s"],
        "DELETE": ["%(app_label)s.delete_%(model_name)s"],
    }


def build_mock_request(method, path, view, original_request, **kwargs):
    """we need to hook in here since the generator for schemas seem to not
    transport all attributes"""
    request = original_build_mock_request(method, path, view, original_request, **kwargs)
    if original_request:
        request.georama_organisation = original_request.georama_organisation
    return request


class OrganisationalModelViewSet(viewsets.ModelViewSet):
    """
    A DRF ViewSet which uses organisational bound tables to filter automatically for
    only organisations defined by the request.

    Attributes:
        request: The normal rest_framework.request.Request which is extended by the
            georama.core.middleware.organisation.OrganisationMiddleware with the
            georama_organisation attribute.
    """

    request: GeoramaDrfRequest

    def get_queryset(self):
        """
        The queryset is automatically filtered by the organisation.

        Returns:
            The filtered queryset.
        """
        qs = super().get_queryset()
        return qs.organisation_objects(self.request.georama_organisation)
