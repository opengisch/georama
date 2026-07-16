from adrf import serializers
from django.contrib.auth import get_user_model

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

    async def get_can_view(self, obj):
        return "view_objects_on_published_layer" in obj["permission_codenames"]

    async def get_can_create(self, obj):
        return "create_objects_on_published_layer" in obj["permission_codenames"]

    async def get_can_delete(self, obj):
        return "delete_objects_on_published_layer" in obj["permission_codenames"]

    async def get_can_update(self, obj):
        return "update_objects_on_published_layer" in obj["permission_codenames"]


class FeatureLayerUserObjectPermissionSerializer(BasePermissionSerializer):
    user = serializers.UUIDField(source="user_id")


class FeatureLayerGroupObjectPermissionSerializer(serializers.Serializer):
    group = serializers.UUIDField(source="group_id")


class PermissionBulkActionSerializer(serializers.Serializer):
    action = serializers.ChoiceField(
        choices=[
            "allow_view",
            "allow_create",
            "allow_delete",
            "allow_update",
            "prevent_view",
            "prevent_create",
            "prevent_delete",
            "prevent_update",
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
