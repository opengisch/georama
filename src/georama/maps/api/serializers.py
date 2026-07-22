from adrf import serializers
from django.utils.translation import gettext as _

from georama.core.common.serializers import (
    GroupObjectPermissionSerializer,
    GroupPermissionBulkActionSerializer,
    UserObjectPermissionSerializer,
    UserPermissionBulkActionSerializer,
)
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
    create_preview = serializers.BooleanField(
        default=True,
        required=False,
        help_text=_(
            "Switch to enable/disable the automatic generation "
            "of the preview image in the moment of publishing."
        ),
    )


class WmsLayerPermissionSerializer(serializers.Serializer):
    can_view = serializers.SerializerMethodField()

    async def get_can_view(self, obj):
        return WmsLayer.VIEW_PERMISSION in obj.permission_codenames


class WmsLayerUserObjectPermissionSerializer(
    UserObjectPermissionSerializer,
    WmsLayerPermissionSerializer,
): ...


class WmsLayerGroupObjectPermissionSerializer(
    GroupObjectPermissionSerializer,
    WmsLayerPermissionSerializer,
): ...


class WmsLayerPermissionBulkActionSerializer(serializers.Serializer):
    action = serializers.ChoiceField(choices=list(WmsLayer.ACTION_MAP.keys()))


class WmsLayerUserPermissionBulkActionSerializer(
    WmsLayerPermissionBulkActionSerializer,
    UserPermissionBulkActionSerializer,
): ...


class WmsLayerGroupPermissionBulkActionSerializer(
    WmsLayerPermissionBulkActionSerializer, GroupPermissionBulkActionSerializer
): ...
