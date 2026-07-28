from adrf import serializers
from django.contrib.auth import get_user_model

User = get_user_model()


class ObjectPermissionSerializer(serializers.Serializer):
    permission_time_created = serializers.DateTimeField(allow_null=True, format=None)
    entity_name = serializers.CharField(read_only=True)
    entity_id = serializers.CharField(read_only=True)

    def to_representation(self, instance):
        data = super().to_representation(instance)
        if data.get("inherited_permissions", None) is None:
            data.pop("inherited_permissions", None)
        return data


class PermissionActionSerializer(serializers.Serializer):
    action = serializers.ChoiceField(choices=[])
    users = serializers.ListField(
        child=serializers.UUIDField(),
        default=list,
    )
    groups = serializers.ListField(
        child=serializers.IntegerField(),
        default=list,
    )
