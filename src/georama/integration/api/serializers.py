from rest_framework import serializers

from georama.integration.models import Collection


class CollectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Collection
        fields = [
            "id",
            "name",
        ]
        extra_kwargs = {"id": {"read_only": True}}
