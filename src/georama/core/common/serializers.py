from adrf import serializers
from django.contrib.auth import get_user_model
from django.utils.formats import date_format
from django.utils.timesince import timesince
from django.utils.translation import gettext_lazy as _

User = get_user_model()


class BasePermissionSerializer(serializers.Serializer):
    time_created = serializers.DateTimeField(read_only=True, allow_null=True)
    time_created_formatted = serializers.SerializerMethodField()
    time_created_since = serializers.SerializerMethodField()

    @staticmethod
    async def get_time_created_formatted(obj):
        if t := obj.permission_time_created:
            return date_format(t, format="DATETIME_FORMAT")
        return ""

    @staticmethod
    async def get_time_created_since(obj):
        if t := obj.permission_time_created:
            return _("{} ago").format(timesince(t))
        return ""


class UserObjectPermissionSerializer(BasePermissionSerializer):
    entity_id = serializers.UUIDField(source="id", read_only=True)
    entity_name = serializers.CharField(source="username", read_only=True)


class GroupObjectPermissionSerializer(BasePermissionSerializer):
    entity_id = serializers.UUIDField(source="id", read_only=True)
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
