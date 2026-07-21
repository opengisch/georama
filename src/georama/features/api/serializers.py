from adrf import serializers
from django.contrib.auth import get_user_model
from django.utils.formats import date_format
from django.utils.timesince import timesince
from django.utils.translation import gettext_lazy as _

from georama.features.models import FeatureLayer, Field, Metadata

User = get_user_model()


class MetadataSerializer(serializers.ModelSerializer):
    class Meta:
        model = Metadata
        fields = [
            "id",
            "title",
            "description",
            "license",
            "fees",
            "access_constraints",
        ]
        extra_kwargs = {"id": {"read_only": True}}


class FieldSerializer(serializers.ModelSerializer):
    class Meta:
        model = Field
        fields = [
            "name",
            "visible",
        ]


class FeatureLayerSerializer(serializers.ModelSerializer):
    metadata = MetadataSerializer()

    class Meta:
        model = FeatureLayer
        fields = [
            "id",
            "datasource",
            "default_items",
            "max_items",
            "on_exceed",
            "metadata",
        ]
        extra_kwargs = {"id": {"read_only": True}}


class BasePermissionSerializer(serializers.Serializer):
    can_view = serializers.SerializerMethodField()
    can_create = serializers.SerializerMethodField()
    can_delete = serializers.SerializerMethodField()
    can_update = serializers.SerializerMethodField()
    time_created = serializers.DateTimeField(read_only=True, allow_null=True)
    time_created_formatted = serializers.SerializerMethodField()
    time_created_since = serializers.SerializerMethodField()

    async def get_can_view(self, obj):
        return "view_objects_on_published_layer" in obj.permission_codenames

    async def get_can_create(self, obj):
        return "create_objects_on_published_layer" in obj.permission_codenames

    async def get_can_delete(self, obj):
        return "delete_objects_on_published_layer" in obj.permission_codenames

    async def get_can_update(self, obj):
        return "update_objects_on_published_layer" in obj.permission_codenames

    @staticmethod
    async def get_time_created_formatted(obj):
        if t := obj.permission_time_created:
            return date_format(t, format="DATETIME_FORMAT")
        return ""

    @staticmethod
    async def get_time_created_since(obj):
        if t := obj.permission_time_created:
            return _("{} ago").format(timesince(t))
        return ""


class FeatureLayerUserObjectPermissionSerializer(BasePermissionSerializer):
    user_id = serializers.UUIDField(source="id", read_only=True)
    username = serializers.CharField(read_only=True)


class FeatureLayerGroupObjectPermissionSerializer(serializers.Serializer):
    group = serializers.UUIDField(source="group_id")


class PermissionBulkActionSerializer(serializers.Serializer):
    action = serializers.ChoiceField(
        choices=[
            "grant",
            "revoke",
            "allow_create",
            "allow_update",
            "allow_delete",
            "prevent_create",
            "prevent_update",
            "prevent_delete",
        ]
    )


class FeatureLayerUserPermissionBulkActionSerializer(PermissionBulkActionSerializer):
    users = serializers.ListField(
        child=serializers.UUIDField(),
        allow_empty=False,
    )
    # users = serializers.PrimaryKeyRelatedField(
    #     many=True,
    #     queryset=User.objects.all(),
    #     allow_empty=False,
    # )


class FeatureLayerGroupPermissionBulkActionSerializer(PermissionBulkActionSerializer):
    groups = serializers.ListField(
        child=serializers.UUIDField(),
        allow_empty=False,
    )
    # groups = serializers.PrimaryKeyRelatedField(
    #     many=True,
    #     queryset=Group.objects.all(),
    #     allow_empty=False,
    # )
