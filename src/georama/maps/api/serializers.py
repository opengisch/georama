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
