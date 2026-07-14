from django.utils.translation import gettext as _
from rest_framework import serializers

from georama.maps.models import Metadata, WmsLayer


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


class WmsLayerSerializer(serializers.ModelSerializer):
    metadata = MetadataSerializer()

    class Meta:
        model = WmsLayer
        fields = [
            "id",
            "datasource",
            "extent",
            "is_queryable",
            "metadata",
        ]
        extra_kwargs = {"id": {"read_only": True}}


class PreviewGeneratorResult(serializers.Serializer):
    layer_id = serializers.UUIDField(
        read_only=True, help_text=_("UUID (primary key) of layer entity")
    )


class PreviewGeneratorBulkResult(serializers.Serializer):
    results = PreviewGeneratorResult(
        many=True,
        read_only=True,
        help_text=_("Collection of the layers previews were generated for."),
    )


class PreviewGeneratorInput(serializers.Serializer):
    layer_ids = serializers.ListField(
        child=serializers.UUIDField(),
        required=True,
        help_text=_("UUIDs (primary keys) of layer entities"),
    )


class PublishFromDatasourceInput(serializers.Serializer):
    pk = serializers.UUIDField(
        required=True,
        help_text=_("UUIDs (primary key) of the datasource the layer should be published from."),
    )
