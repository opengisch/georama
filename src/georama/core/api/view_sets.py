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
    permission_classes = [permissions.IsAdminUser, permissions.IsAuthenticated]
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
    filter_backends = [
        filters.SearchFilter,
        filters.OrderingFilter,
        DjangoFilterBackend,
    ]
    search_fields = ["username"]
    ordering_fields = ["username"]
    filterset_fields = ["username", "first_name", "last_name"]
