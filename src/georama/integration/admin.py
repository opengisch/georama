from django.contrib import admin

from georama.core.common.admin import OrganisationalModelAdmin
from georama.integration.models import Field
from georama.integration.models.collection import Collection
from georama.integration.models.dataset import Custom, Dataset, Raster, Vector
from georama.integration.models.project import Project


@admin.register(Collection)
class CollectionAdmin(OrganisationalModelAdmin):
    list_display = ["name", "organisation__name"]
    prefetch_organisation_related = "organisation"


@admin.register(Project)
class ProjectAdmin(OrganisationalModelAdmin):
    list_display = ["name", "collection__organisation__name"]
    prefetch_organisation_related = "collection__organisation"


@admin.register(Dataset)
class DatasetAdmin(OrganisationalModelAdmin):
    list_display = ["name", "project__collection__organisation__name"]
    prefetch_organisation_related = "project__collection__organisation"


@admin.register(Custom)
class CustomAdmin(OrganisationalModelAdmin):
    list_display = ["name", "project__collection__organisation__name"]
    prefetch_organisation_related = "project__collection__organisation"


@admin.register(Raster)
class RasterAdmin(OrganisationalModelAdmin):
    list_display = ["name", "project__collection__organisation__name"]
    prefetch_organisation_related = "project__collection__organisation"


@admin.register(Vector)
class VectorAdmin(OrganisationalModelAdmin):
    list_display = ["name", "project__collection__organisation__name"]
    prefetch_organisation_related = "project__collection__organisation"


@admin.register(Field)
class FieldAdmin(OrganisationalModelAdmin):
    list_display = ["name", "dataset__project__collection__organisation__name"]
    prefetch_organisation_related = "dataset__project__collection__organisation"
