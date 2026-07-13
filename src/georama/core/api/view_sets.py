from django.contrib.auth.models import Group, Permission
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters, permissions, viewsets

from georama.core.api.serializers import (
    FenceSerializer,
    GroupSerializer,
    MembershipSerializer,
    OrganisationSerializer,
    PermissionSerializer,
    UserSerializer,
)
from georama.core.common.api import OrganisationalModelViewSet
from georama.core.forms.user import GeoramaUserForm
from georama.core.models import Fence, GeoramaUser, Membership, Organisation


class MembershipViewSet(OrganisationalModelViewSet):
    queryset = Membership.objects.all()
    permission_classes = [permissions.IsAdminUser]
    serializer_class = MembershipSerializer
    filter_backends = [
        filters.SearchFilter,
        filters.OrderingFilter,
        DjangoFilterBackend,
    ]
    search_fields = []
    ordering_fields = []
    filterset_fields = []


class FenceViewSet(OrganisationalModelViewSet):
    queryset = Fence.objects.all()
    permission_classes = [permissions.IsAdminUser]
    serializer_class = FenceSerializer
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


class OrganisationViewSet(viewsets.ModelViewSet):
    queryset = Organisation.objects.all()
    permission_classes = [permissions.IsAdminUser]
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
    permission_classes = [permissions.IsAdminUser]
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
    permission_classes = [permissions.IsAdminUser]
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
    permission_classes = [permissions.IsAdminUser]
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
