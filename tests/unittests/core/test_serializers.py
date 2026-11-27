import asyncio

import pytest
from adrf import serializers
from adrf.mixins import get_data
from django.http import QueryDict

from georama.core.common.bulk_actions import DeleteBulkAction
from georama.core.common.serializers import BulkActionSerializer, ObjectPermissionSerializer


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


class TestBulkActionSerializer:
    @pytest.fixture
    def delete_bulk_action(self):
        return DeleteBulkAction()

    @pytest.mark.parametrize(
        "data",
        [
            {"action": "delete", "ids": ["1", "abc"]},
            QueryDict("action=delete&ids=1&ids=abc"),
        ],
    )
    def test_accepts_multiple_ids(self, data, delete_bulk_action):
        serializer = BulkActionSerializer(data=data, context={"bulk_actions": [delete_bulk_action]})

        assert serializer.is_valid(), serializer.errors
        # the action name is resolved to the action the viewset offers
        assert serializer.validated_data == {"action": delete_bulk_action, "ids": ["1", "abc"]}

    @pytest.mark.parametrize(
        "data",
        [
            {},
            {"action": "delete", "ids": []},
            {"action": "delete", "ids": [""]},
            {"action": "unknown", "ids": ["1"]},
            # a known action which the viewset does not offer
            {"action": "make-public", "ids": ["1"]},
        ],
    )
    def test_rejects_invalid_actions(self, data, delete_bulk_action):
        serializer = BulkActionSerializer(data=data, context={"bulk_actions": [delete_bulk_action]})

        assert not serializer.is_valid()
