from rest_framework import serializers

from georama.features.models import FeatureLayer, Field, Metadata


class MetadataSerializer(serializers.ModelSerializer):
    class Meta:
        model = Metadata
        fields = [
            "default_items",
            "max_items",
            "on_exceed",
        ]


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
            "metadata",
        ]
        extra_kwargs = {"id": {"read_only": True}}
