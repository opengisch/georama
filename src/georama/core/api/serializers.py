from adrf import serializers
from django.contrib.auth.models import Group, Permission
from rest_framework.serializers import PrimaryKeyRelatedField
from rest_framework_gis.serializers import GeoFeatureModelSerializer

from georama.core.models import Fence, GeoramaUser, Membership, Organisation


class PermissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Permission
        fields = [
            "id",
            "name",
            "codename",
            "content_type",
        ]
        extra_kwargs = {"id": {"read_only": True}}


class GroupSerializer(serializers.ModelSerializer):
    permissions = PrimaryKeyRelatedField(
        many=True,
        queryset=Permission.objects.all(),
    )

    class Meta:
        model = Group
        fields = [
            "id",
            "name",
            "permissions",
        ]
        extra_kwargs = {"id": {"read_only": True}}


class UserSerializer(serializers.ModelSerializer):
    groups = PrimaryKeyRelatedField(
        many=True,
        queryset=Group.objects.all(),
    )
    user_permissions = PrimaryKeyRelatedField(
        many=True,
        queryset=Permission.objects.all(),
    )
    memberships = PrimaryKeyRelatedField(
        many=True,
        queryset=Membership.objects.all(),
    )

    class Meta:
        model = GeoramaUser
        fields = [
            "id",
            "username",
            "first_name",
            "last_name",
            "email",
            "is_superuser",
            "is_staff",
            "is_active",
            "is_anonymous",
            "date_joined",
            "last_login",
            "groups",
            "user_permissions",
            "memberships",
        ]
        extra_kwargs = {"id": {"read_only": True}}


class OrganisationSerializer(serializers.ModelSerializer):
    fences = PrimaryKeyRelatedField(
        many=True,
        queryset=Fence.objects.all(),
    )
    memberships = PrimaryKeyRelatedField(
        many=True,
        queryset=Membership.objects.all(),
    )

    class Meta:
        model = Organisation
        fields = [
            "id",
            "name",
            "domain",
            "fences",
            "memberships",
        ]
        extra_kwargs = {"id": {"read_only": True}}


class FenceSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = Fence
        geo_field = "geometry"
        fields = [
            "id",
            "name",
            "organisation_id",
        ]
        extra_kwargs = {"id": {"read_only": True}}


class MembershipSerializer(serializers.ModelSerializer):
    class Meta:
        model = Membership
        fields = [
            "id",
            "user_id",
            "organisation_id",
        ]
        extra_kwargs = {"id": {"read_only": True}}
