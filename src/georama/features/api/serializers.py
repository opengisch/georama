from adrf import serializers
from django.contrib.auth import get_user_model

from georama.core.common.serializers import (
    GroupObjectPermissionSerializer,
    GroupPermissionBulkActionSerializer,
    UserObjectPermissionSerializer,
    UserPermissionBulkActionSerializer,
)
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


class FeatureLayerPermissionSerializer(serializers.Serializer):
    can_view = serializers.BooleanField()
    can_create = serializers.BooleanField()
    can_delete = serializers.BooleanField()
    can_update = serializers.BooleanField()


class FeatureLayerUserObjectPermissionSerializer(
    UserObjectPermissionSerializer,
    FeatureLayerPermissionSerializer,
): ...


class FeatureLayerGroupObjectPermissionSerializer(
    GroupObjectPermissionSerializer,
    FeatureLayerPermissionSerializer,
): ...


class FeatureLayerPermissionBulkActionSerializer(serializers.Serializer):
    action = serializers.ChoiceField(choices=list(FeatureLayer.ACTION_MAP.keys()))


class FeatureLayerUserPermissionBulkActionSerializer(
    FeatureLayerPermissionBulkActionSerializer,
    UserPermissionBulkActionSerializer,
): ...


class FeatureLayerGroupPermissionBulkActionSerializer(
    FeatureLayerPermissionBulkActionSerializer, GroupPermissionBulkActionSerializer
): ...
