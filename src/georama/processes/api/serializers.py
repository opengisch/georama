from adrf import serializers
from django.contrib.auth import get_user_model

from georama.core.common.serializers import (
    ObjectPermissionSerializer,
    PermissionActionSerializer,
)
from georama.processes.models.job import Job
from georama.processes.models.process import Process

User = get_user_model()


class JobSerializer(serializers.ModelSerializer):
    class Meta:
        model = Job
        fields = [
            "id",
            "redis_job_id",
            "created_by",
            "created_at",
            "process",
            "job_parameters",
            "job_result",
        ]
        extra_kwargs = {
            "id": {"read_only": True},
            "created_by": {"read_only": True},
            "created_at": {"read_only": True},
            "process": {"read_only": True},
            "job_parameters": {"read_only": True},
            "job_result": {"read_only": True},
        }


class ProcessSerializer(serializers.ModelSerializer):
    title = serializers.CharField(read_only=True)
    help = serializers.CharField(read_only=True)
    description = serializers.CharField(read_only=True)

    class Meta:
        model = Process
        fields = [
            "id",
            "public",
            "title",
            "description",
            "help",
        ]


class ProcessPermissionSerializer(serializers.Serializer):
    can_view = serializers.BooleanField()


class ProcessObjectPermissionSerializer(ObjectPermissionSerializer):
    entity_permissions = ProcessPermissionSerializer()
    inherited_permissions = ProcessPermissionSerializer()


class ProcessPermissionActionSerializer(PermissionActionSerializer):
    action = serializers.ChoiceField(
        choices=[(key, value[2]) for key, value in Process.ACTION_MAP.items()]
    )
