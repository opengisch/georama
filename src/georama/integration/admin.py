from django.contrib import admin
from unfold.admin import ModelAdmin

from georama.integration.models import Field
from georama.integration.models.collection import Collection
from georama.integration.models.dataset import Custom, Dataset, Raster, Vector
from georama.integration.models.project import Project


@admin.register(Project)
class ProjectAdmin(ModelAdmin):
    pass


@admin.register(Collection)
class CollectionAdmin(ModelAdmin):
    pass


@admin.register(Dataset)
class DatasetAdmin(ModelAdmin):
    pass


@admin.register(Custom)
class CustomAdmin(ModelAdmin):
    pass


@admin.register(Raster)
class RasterAdmin(ModelAdmin):
    pass


@admin.register(Vector)
class VectorAdmin(ModelAdmin):
    pass


@admin.register(Field)
class FieldAdmin(ModelAdmin):
    pass
