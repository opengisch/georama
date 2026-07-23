from adrf import serializers
from django.contrib.auth import get_user_model

User = get_user_model()


class BasePermissionSerializer(serializers.Serializer):
    permission_time_created = serializers.DateTimeField(allow_null=True, format=None)


class UserObjectPermissionSerializer(BasePermissionSerializer):
    entity_id = serializers.UUIDField(source="id", read_only=True)
    entity_name = serializers.CharField(source="username", read_only=True)


class GroupObjectPermissionSerializer(BasePermissionSerializer):
    entity_id = serializers.IntegerField(source="id", read_only=True)
    entity_name = serializers.CharField(source="name", read_only=True)


class BasePermissionBulkActionSerializer(serializers.Serializer):
    action = serializers.ChoiceField(choices=[])


class UserPermissionBulkActionSerializer(BasePermissionBulkActionSerializer):
    users = serializers.ListField(
        child=serializers.UUIDField(),
        allow_empty=False,
    )


class GroupPermissionBulkActionSerializer(BasePermissionBulkActionSerializer):
    groups = serializers.ListField(
        child=serializers.IntegerField(),
        allow_empty=False,
    )
