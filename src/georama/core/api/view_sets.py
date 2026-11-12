import asyncio

from adrf.viewsets import ViewSet
from django.conf import settings
from django.contrib.auth.models import Group, Permission
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters, renderers, status, viewsets
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from georama.core.api.serializers import (
    GroupSerializer,
    MembershipSerializer,
    OrganisationSerializer,
    PermissionSerializer,
    UserSerializer,
)
from georama.core.common.api import IsSuperuser, OrganisationalModelViewSet
from georama.core.common.health import HealthCheckResult, get_health_checks
from georama.core.common.renderers import StandaloneTemplateHTMLRenderer
from georama.core.forms.user import GeoramaUserForm
from georama.core.models import GeoramaUser, Membership, Organisation


class MembershipViewSet(OrganisationalModelViewSet):
    queryset = Membership.objects.all()
    permission_classes = [IsSuperuser]
    serializer_class = MembershipSerializer
    filter_backends = [
        filters.SearchFilter,
        filters.OrderingFilter,
        DjangoFilterBackend,
    ]
    search_fields = []
    ordering_fields = []
    filterset_fields = []


class OrganisationViewSet(viewsets.ModelViewSet):
    queryset = Organisation.objects.all()
    permission_classes = [IsSuperuser]
    serializer_class = OrganisationSerializer
    filter_backends = [
        filters.SearchFilter,
        filters.OrderingFilter,
        DjangoFilterBackend,
    ]
    search_fields = ["name"]
    ordering_fields = ["name"]
    filterset_fields = ["name", "domain"]


class PermissionViewSet(viewsets.ModelViewSet):
    queryset = Permission.objects.all()
    permission_classes = [IsSuperuser]
    serializer_class = PermissionSerializer
    filter_backends = [
        filters.SearchFilter,
        filters.OrderingFilter,
        DjangoFilterBackend,
    ]
    search_fields = ["name"]
    ordering_fields = ["name"]
    filterset_fields = ["name", "codename"]


class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    permission_classes = [IsSuperuser]
    serializer_class = GroupSerializer
    filter_backends = [
        filters.SearchFilter,
        filters.OrderingFilter,
        DjangoFilterBackend,
    ]
    search_fields = ["name"]
    ordering_fields = ["name"]
    filterset_fields = [
        "name",
    ]


class UserViewSet(viewsets.ModelViewSet):
    queryset = GeoramaUser.objects.all()
    permission_classes = [IsSuperuser]
    serializer_class = UserSerializer
    list_template_name = "core/drf/user/list.html"
    partial_list_template_name = "core/drf/user/partials/list.html"
    form = GeoramaUserForm

    filter_backends = [
        filters.SearchFilter,
        filters.OrderingFilter,
        DjangoFilterBackend,
    ]
    search_fields = ["username", "first_name", "last_name"]
    ordering_fields = ["username", "first_name", "last_name"]
    filterset_fields = ["username", "first_name", "last_name"]


class HealthViewSet(ViewSet):
    """Public status of Georama and the resources it depends on, for probes and humans.
    No authentication, so neither the session nor the user is loaded from the database.
    """

    permission_classes = [AllowAny]
    authentication_classes = []
    renderer_classes = [renderers.JSONRenderer, StandaloneTemplateHTMLRenderer]
    template_name = "core/health.html"
    check_timeout = 2

    async def list(self, request):
        results = await asyncio.gather(
            *(check.run(self.check_timeout) for check in get_health_checks())
        )
        healthy = all(result.healthy for result in results)
        data = {
            "status": self.status_name(healthy),
            "checks": {result.name: self.check_data(result) for result in results},
        }
        if request.accepted_renderer.format == "html":
            # no context processor runs for this page, see StandaloneTemplateHTMLRenderer
            data["site_title"] = settings.SITE_TITLE
        return Response(
            data,
            status=status.HTTP_200_OK if healthy else status.HTTP_503_SERVICE_UNAVAILABLE,
            headers={"Cache-Control": "no-store"},
        )

    @staticmethod
    def status_name(healthy: bool) -> str:
        return "ok" if healthy else "down"

    @classmethod
    def check_data(cls, result: HealthCheckResult) -> dict:
        return {"status": cls.status_name(result.healthy), **result.details}
