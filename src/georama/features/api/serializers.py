from adrf import serializers
from django.contrib.auth import get_user_model

from georama.core.common.serializers import (
    ObjectPermissionSerializer,
    PermissionActionSerializer,
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


class FeatureLayerObjectPermissionSerializer(ObjectPermissionSerializer):
    entity_permissions = FeatureLayerPermissionSerializer()
    inherited_permissions = FeatureLayerPermissionSerializer()


class FeatureLayerPermissionActionSerializer(PermissionActionSerializer):
    action = serializers.ChoiceField(
        choices=[(key, value[2]) for key, value in FeatureLayer.ACTION_MAP.items()]
    )
