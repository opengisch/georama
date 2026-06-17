from django.contrib.auth.models import Group, Permission
from rest_framework import serializers
from rest_framework_gis.serializers import GeoFeatureModelSerializer

from georama.core.models import Fence, GeoramaUser, Membership, Organisation


class PermissionSchema(serializers.ModelSerializer):
    class Meta:
        model = Permission
        fields = [
            "id",
            "name",
            "codename",
            "content_type",
        ]


class GroupSchema(serializers.ModelSerializer):
    permissions = serializers.PrimaryKeyRelatedField(
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


class UserSchema(serializers.ModelSerializer):
    groups = serializers.PrimaryKeyRelatedField(
        many=True,
        queryset=Group.objects.all(),
    )
    user_permissions = serializers.PrimaryKeyRelatedField(
        many=True,
        queryset=Permission.objects.all(),
    )
    memberships = serializers.PrimaryKeyRelatedField(
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


class OrganisationSchema(serializers.ModelSerializer):
    fences = serializers.PrimaryKeyRelatedField(
        many=True,
        queryset=Fence.objects.all(),
    )
    memberships = serializers.PrimaryKeyRelatedField(
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


class FenceSchema(GeoFeatureModelSerializer):
    class Meta:
        model = Fence
        geo_field = "geometry"
        fields = [
            "id",
            "name",
            "organisation_id",
        ]


class MembershipSchema(serializers.ModelSerializer):
    class Meta:
        model = Membership
        fields = [
            "id",
            "user_id",
            "organisation_id",
        ]
