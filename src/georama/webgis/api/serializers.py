from adrf import serializers
from django.conf import settings
from django.db import IntegrityError
from django.urls import reverse
from django.utils.crypto import get_random_string
from rest_framework.exceptions import ValidationError

from georama.core.common.serializers import (
    ObjectPermissionSerializer,
    PermissionActionSerializer,
)
from georama.webgis.models import Theme, UrlShortener
from georama.webgis.models.metadata import Metadata
from georama.webgis.models.wms_layer import WmsLayer


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


class ThemeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Theme
        fields = [
            "id",
            "project_id",
            "metadata_id",
            "public",
            "ordering",
            "zoom",
            "theme_json",
        ]
        extra_kwargs = {"id": {"read_only": True}}


class WmsLayerSerializer(serializers.ModelSerializer):
    metadata = MetadataSerializer()

    class Meta:
        model = WmsLayer
        fields = [
            "id",
            "datasource_id",
            "extent",
            "is_queryable",
            "metadata",
        ]
        extra_kwargs = {"id": {"read_only": True}}


class ThemePermissionSerializer(serializers.Serializer):
    can_view = serializers.BooleanField()


class ThemeObjectPermissionSerializer(ObjectPermissionSerializer):
    entity_permissions = ThemePermissionSerializer()
    inherited_permissions = ThemePermissionSerializer()


class ThemePermissionActionSerializer(PermissionActionSerializer):
    action = serializers.ChoiceField(
        choices=[(key, value[2]) for key, value in Theme.ACTION_MAP.items()]
    )


class UrlShortenerCreateSerializer(serializers.ModelSerializer):
    short_url = serializers.SerializerMethodField()

    class Meta:
        model = UrlShortener
        fields = ["url", "short_url"]
        extra_kwargs = {"url": {"write_only": True}}

    def get_short_url(self, obj):
        return reverse("webgis:short-detail", kwargs={"pk": obj.pk})

    def validate_url(self, value):
        if not value.startswith(settings.WEBGISURL):
            raise ValidationError("Invalid URL.")
        return value

    def create(self, validated_data):
        while True:
            try:
                return UrlShortener.objects.create(id=get_random_string(length=6), **validated_data)
            except IntegrityError:
                continue


class UrlShortenerRetrieveSerializer(serializers.ModelSerializer):
    long_url = serializers.CharField(source="url")

    class Meta:
        model = UrlShortener
        fields = ["long_url"]
