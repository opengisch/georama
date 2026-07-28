from adrf import serializers

from georama.core.common.serializers import (
    ObjectPermissionSerializer,
    PermissionActionSerializer,
)
from georama.webgis.models import Theme
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
