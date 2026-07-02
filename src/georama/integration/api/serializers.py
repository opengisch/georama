from rest_framework import serializers

from georama.integration.models import Custom, Project, Raster, Vector
from georama.integration.models.datasource import VectorField


class ProjectSerializer(serializers.ModelSerializer):
    organisation_id = serializers.SerializerMethodField()

    class Meta:
        model = Project
        fields = [
            "id",
            "name",
            "qgis_version",
            "hash",
            "organisation_id",
        ]
        extra_kwargs = {"id": {"read_only": True}}

    def get_organisation_id(self, obj):
        return obj.organisation_id


class FileSystemProjectSerializer(serializers.Serializer):
    path = serializers.CharField()


class VectorDatasourceSerializer(serializers.ModelSerializer):
    organisation_id = serializers.SerializerMethodField()

    class Meta:
        model = Vector
        fields = [
            "id",
            "qgis_layer_id",
            "name",
            "bbox",
            "bbox_wgs84",
            "source",
            "styles",
            "driver",
            "crs",
            "minimum_scale",
            "maximum_scale",
            "geometry_type_simple",
            "geometry_type_wkb",
            "project_id",
            "organisation_id",
        ]
        extra_kwargs = {"id": {"read_only": True}}

    def get_organisation_id(self, obj):
        return obj.project.organisation_id


class RasterDatasourceSerializer(serializers.ModelSerializer):
    organisation_id = serializers.SerializerMethodField()

    class Meta:
        model = Raster
        fields = [
            "id",
            "qgis_layer_id",
            "name",
            "bbox",
            "bbox_wgs84",
            "source",
            "styles",
            "driver",
            "crs",
            "minimum_scale",
            "maximum_scale",
            "project_id",
            "organisation_id",
        ]
        extra_kwargs = {"id": {"read_only": True}}

    def get_organisation_id(self, obj):
        return obj.project.organisation_id


class CustomDatasourceSerializer(serializers.ModelSerializer):
    organisation_id = serializers.SerializerMethodField()

    class Meta:
        model = Custom
        fields = [
            "id",
            "qgis_layer_id",
            "name",
            "bbox",
            "bbox_wgs84",
            "source",
            "styles",
            "driver",
            "crs",
            "minimum_scale",
            "maximum_scale",
            "project_id",
            "organisation_id",
        ]
        extra_kwargs = {"id": {"read_only": True}}

    def get_organisation_id(self, obj):
        return obj.project.organisation_id


class FieldSerializer(serializers.ModelSerializer):
    organisation_id = serializers.SerializerMethodField()
    project_id = serializers.SerializerMethodField()

    class Meta:
        model = VectorField
        fields = [
            "id",
            "name",
            "type",
            "is_primary_key",
            "type_wfs",
            "type_oapif",
            "type_oapif_format",
            "alias",
            "comment",
            "nullable",
            "length",
            "precision",
            "datasource_id",
            "project_id",
            "organisation_id",
        ]
        extra_kwargs = {"id": {"read_only": True}}

    def get_organisation_id(self, obj):
        return obj.datasource.project.organisation_id

    def get_project_id(self, obj):
        return obj.datasource.project_id
