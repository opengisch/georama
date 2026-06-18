from rest_framework import serializers

from georama.integration.models import Collection, Custom, Project, Raster, Vector
from georama.integration.models.dataset import Field


class CollectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Collection
        fields = [
            "id",
            "name",
        ]
        extra_kwargs = {"id": {"read_only": True}}


class ProjectSerializer(serializers.ModelSerializer):
    organisation_id = serializers.SerializerMethodField()

    class Meta:
        model = Project
        fields = [
            "id",
            "name",
            "qgis_version",
            "hash",
            "collection_id",
            "organisation_id",
        ]
        extra_kwargs = {"id": {"read_only": True}}

    def get_organisation_id(self, obj):
        return obj.collection.organisation_id


class VectorDatasetSerializer(serializers.ModelSerializer):
    organisation_id = serializers.SerializerMethodField()
    collection_id = serializers.SerializerMethodField()

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
            "collection_id",
        ]
        extra_kwargs = {"id": {"read_only": True}}

    def get_organisation_id(self, obj):
        return obj.project.collection.organisation_id

    def get_collection_id(self, obj):
        return obj.project.collection_id


class RasterDatasetSerializer(serializers.ModelSerializer):
    organisation_id = serializers.SerializerMethodField()
    collection_id = serializers.SerializerMethodField()

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
            "collection_id",
        ]
        extra_kwargs = {"id": {"read_only": True}}

    def get_organisation_id(self, obj):
        return obj.project.collection.organisation_id

    def get_collection_id(self, obj):
        return obj.project.collection_id


class CustomDatasetSerializer(serializers.ModelSerializer):
    organisation_id = serializers.SerializerMethodField()
    collection_id = serializers.SerializerMethodField()

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
            "collection_id",
        ]
        extra_kwargs = {"id": {"read_only": True}}

    def get_organisation_id(self, obj):
        return obj.project.collection.organisation_id

    def get_collection_id(self, obj):
        return obj.project.collection_id


class FieldSerializer(serializers.ModelSerializer):
    organisation_id = serializers.SerializerMethodField()
    collection_id = serializers.SerializerMethodField()
    project_id = serializers.SerializerMethodField()

    class Meta:
        model = Field
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
            "dataset_id",
            "project_id",
            "organisation_id",
            "collection_id",
        ]
        extra_kwargs = {"id": {"read_only": True}}

    def get_organisation_id(self, obj):
        return obj.dataset.project.collection.organisation_id

    def get_collection_id(self, obj):
        return obj.dataset.project.collection_id

    def get_project_id(self, obj):
        return obj.dataset.project_id
