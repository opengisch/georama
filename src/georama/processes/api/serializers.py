from adrf import serializers
from django.contrib.auth import get_user_model
from django.utils.translation import gettext as _
from rest_framework.exceptions import ValidationError
from rest_framework.serializers import PrimaryKeyRelatedField

from georama.core.common.serializers import (
    ObjectPermissionSerializer,
    PermissionActionSerializer,
)
from georama.processes.models.job import Job
from georama.processes.models.process import Process
from georama.processes.models.process_input import ProcessInput

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
            "status",
            "message",
            "progress",
            "finished",
            "updated",
            "expires",
        ]
        extra_kwargs = {
            "id": {"read_only": True},
            "created_by": {"read_only": True},
            "created_at": {"read_only": True},
            "process": {"read_only": True},
            "job_parameters": {"read_only": True},
            "job_result": {"read_only": True},
            "status": {"read_only": True},
            "message": {"read_only": True},
            "progress": {"read_only": True},
            "finished": {"read_only": True},
            "updated": {"read_only": True},
            "expires": {"read_only": True},
        }


class ProcessSerializer(serializers.ModelSerializer):
    title = serializers.CharField(read_only=True)
    description = serializers.CharField(read_only=True)

    class Meta:
        model = Process
        fields = [
            "id",
            "algorithm_id",
            "public",
            "title",
            "description",
        ]
        extra_kwargs = {
            "id": {"read_only": True},
        }

    def get_extra_kwargs(self):
        extra_kwargs = super().get_extra_kwargs()
        if self.instance is not None:
            extra_kwargs["algorithm_id"] = {"read_only": True}
        return extra_kwargs

    def validate_algorithm_id(self, value):
        try:
            self.context["process_descriptions"].process_by_id(value)
        except LookupError as e:
            raise ValidationError("Algorithm is not served by any process-worker.") from e
        organisation = self.context["request"].georama_organisation
        published = Process.objects.organisation_objects(organisation).filter(algorithm_id=value)
        if published.exists():
            raise ValidationError("Algorithm is already published in this organisation.")
        return value


class ProcessPermissionSerializer(serializers.Serializer):
    can_view = serializers.BooleanField()


class ProcessObjectPermissionSerializer(ObjectPermissionSerializer):
    entity_permissions = ProcessPermissionSerializer()
    inherited_permissions = ProcessPermissionSerializer()


class ProcessPermissionActionSerializer(PermissionActionSerializer):
    action = serializers.ChoiceField(
        choices=[(key, value[2]) for key, value in Process.ACTION_MAP.items()]
    )


class ProcessInputSerializer(serializers.ModelSerializer):
    title = serializers.CharField(read_only=True)
    datasource = PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = ProcessInput
        fields = [
            "id",
            "public",
            "title",
            "datasource",
        ]
        extra_kwargs = {"id": {"read_only": True}}


class PublishFromDatasourceInput(serializers.Serializer):
    pk = serializers.UUIDField(
        required=True,
        help_text=_(
            "UUIDs (primary key) of the datasource the process input should be published from."
        ),
    )


class ProcessInputPermissionSerializer(serializers.Serializer):
    can_view = serializers.BooleanField()


class ProcessInputObjectPermissionSerializer(ObjectPermissionSerializer):
    entity_permissions = ProcessInputPermissionSerializer()
    inherited_permissions = ProcessInputPermissionSerializer()


class ProcessInputPermissionActionSerializer(PermissionActionSerializer):
    action = serializers.ChoiceField(
        choices=[(key, value[2]) for key, value in ProcessInput.ACTION_MAP.items()]
    )
