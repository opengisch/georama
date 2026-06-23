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
            "id",
            "datasource_field",
        ]
        extra_kwargs = {"id": {"read_only": True}}


class FeatureLayerSerializer(serializers.ModelSerializer):
    metadata = MetadataSerializer()

    class Meta:
        model = FeatureLayer
        fields = [
            "id",
            "datasource",
            "metadata",
            # "fields",
        ]
        extra_kwargs = {"id": {"read_only": True}}
