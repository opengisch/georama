from adrf import serializers
from asgiref.sync import sync_to_async
from django.contrib.auth import get_user_model
from django.db import transaction
from django.utils.translation import gettext_lazy as _
from rest_framework.exceptions import ValidationError
from rest_framework.utils import html

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


class FieldListSerializer(serializers.ListSerializer):
    def validate(self, data):
        layer = self.parent.instance
        field_names = {field.name for field in layer.fields.all()} if layer is not None else set()
        submitted_name = [item.get("name") for item in data]
        if any(name not in field_names for name in submitted_name):
            raise ValidationError("Unknown field name.")
        if len(submitted_name) != len(set(submitted_name)):
            raise ValidationError("Duplicate field name.")
        return data

    def update(self, instance, validated_data):
        fields = {field.name: field for field in instance.all()}
        for data in validated_data:
            self.child.update(fields[data["name"]], data)
        return instance


class FieldSerializer(serializers.ModelSerializer):
    class Meta:
        list_serializer_class = FieldListSerializer
        model = Field
        fields = [
            "name",
            "visible",
        ]

    def to_internal_value(self, data):
        if html.is_html_input(data):
            data = data.copy()
            data.setdefault("visible", "false")
        return super().to_internal_value(data)


class FeatureLayerSerializer(serializers.ModelSerializer):
    metadata = MetadataSerializer()
    fields = FieldSerializer(
        many=True,
        required=False,
        label=_("Fields visibility"),
        style={"template": "features/fields.html"},
    )  # pyright: ignore[reportAssignmentType]

    class Meta:
        model = FeatureLayer
        fields = [
            "id",
            "datasource",
            "default_items",
            "max_items",
            "on_exceed",
            "metadata",
            "fields",
        ]
        extra_kwargs = {"id": {"read_only": True}}

    @transaction.atomic
    def update(self, instance, validated_data):
        metadata_data = validated_data.pop("metadata", None)
        fields_data = validated_data.pop("fields", None)
        instance = super().update(instance, validated_data)
        if metadata_data is not None:
            MetadataSerializer().update(instance.metadata, metadata_data)
        if fields_data is not None:
            self.fields["fields"].update(instance.fields, fields_data)
        return instance

    async def aupdate(self, instance, validated_data):
        return await sync_to_async(self.update)(instance, validated_data)


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
