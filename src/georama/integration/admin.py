from django.contrib import admin
from unfold.admin import ModelAdmin

from georama.integration.models import Field
from georama.integration.models.collection import Collection
from georama.integration.models.dataset import Custom, Dataset, Raster, Vector
from georama.integration.models.project import Project


@admin.register(Project)
class ProjectAdmin(ModelAdmin):
    list_display = ["name", "collection__organisation__name"]

    def get_queryset(self, request):
        return super().get_queryset(request).prefetch_related("collection__organisation")


@admin.register(Collection)
class CollectionAdmin(ModelAdmin):
    list_display = ["name", "organisation__name"]

    def get_queryset(self, request):
        return super().get_queryset(request).prefetch_related("organisation")


@admin.register(Dataset)
class DatasetAdmin(ModelAdmin):
    list_display = ["name", "project__collection__organisation__name"]

    def get_queryset(self, request):
        return super().get_queryset(request).prefetch_related("project__collection__organisation")


@admin.register(Custom)
class CustomAdmin(ModelAdmin):
    list_display = ["name", "project__collection__organisation__name"]

    def get_queryset(self, request):
        return super().get_queryset(request).prefetch_related("project__collection__organisation")


@admin.register(Raster)
class RasterAdmin(ModelAdmin):
    list_display = ["name", "project__collection__organisation__name"]

    def get_queryset(self, request):
        return super().get_queryset(request).prefetch_related("project__collection__organisation")


@admin.register(Vector)
class VectorAdmin(ModelAdmin):
    list_display = ["name", "project__collection__organisation__name"]

    def get_queryset(self, request):
        return super().get_queryset(request).prefetch_related("project__collection__organisation")


@admin.register(Field)
class FieldAdmin(ModelAdmin):
    list_display = ["name", "dataset__project__collection__organisation__name"]

    def get_queryset(self, request):
        return (
            super()
            .get_queryset(request)
            .prefetch_related("dataset__project__collection__organisation")
        )
