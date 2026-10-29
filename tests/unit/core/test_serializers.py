import asyncio

import pytest
from adrf import serializers
from adrf.mixins import get_data

from georama.core.common.serializers import ObjectPermissionSerializer


class InheritedPermissionSerializer(serializers.Serializer):
    can_view = serializers.BooleanField()


class ObjectPermissionWithInheritedSerializer(ObjectPermissionSerializer):
    inherited_permissions = InheritedPermissionSerializer()


def permission_row(inherited_permissions):
    return {
        "permission_time_created": None,
        "entity_name": "entity",
        "entity_id": "1",
        "inherited_permissions": inherited_permissions,
    }


def represent_sync(instance):
    return ObjectPermissionWithInheritedSerializer(instance).data


def represent_async(instance):
    return asyncio.run(get_data(ObjectPermissionWithInheritedSerializer(instance)))


@pytest.mark.parametrize("represent", [represent_sync, represent_async])
class TestObjectPermissionSerializer:
    def test_drops_empty_inherited_permissions(self, represent):
        data = represent(permission_row(None))
        assert "inherited_permissions" not in data

    def test_keeps_inherited_permissions(self, represent):
        data = represent(permission_row({"can_view": True}))
        assert data["inherited_permissions"] == {"can_view": True}
