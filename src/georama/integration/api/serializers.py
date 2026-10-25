from adrf import serializers

from georama.integration.models import Custom, Datasource, Project, Raster, Vector
from georama.integration.models.datasource import VectorField


class ProjectSerializer(serializers.ModelSerializer):
    organisation_id = serializers.ReadOnlyField()

    class Meta:
        model = Project
        fields = [
            "id",
            "name",
            "qgis_version",
            "path",
            "organisation_id",
        ]
        extra_kwargs = {"id": {"read_only": True}}


class FileSystemProjectSerializer(serializers.Serializer):
    project_path = serializers.CharField()
    config_path = serializers.CharField()


class DatasourceSerializer(serializers.ModelSerializer):
    organisation_id = serializers.ReadOnlyField(source="project.organisation_id")

    class Meta:
        model = Datasource
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


class VectorDatasourceSerializer(serializers.ModelSerializer):
    organisation_id = serializers.ReadOnlyField(source="project.organisation_id")

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


class RasterDatasourceSerializer(serializers.ModelSerializer):
    organisation_id = serializers.ReadOnlyField(source="project.organisation_id")

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


class CustomDatasourceSerializer(serializers.ModelSerializer):
    organisation_id = serializers.ReadOnlyField(source="project.organisation_id")

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


class FieldSerializer(serializers.ModelSerializer):
    organisation_id = serializers.ReadOnlyField(source="datasource.project.organisation_id")
    project_id = serializers.ReadOnlyField(source="datasource.project_id")

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
