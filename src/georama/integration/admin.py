from django.contrib import admin
from unfold.admin import TabularInline

from georama.core.common.admin import OrganisationalModelAdmin
from georama.integration.models import VectorField
from georama.integration.models.datasource import Custom, Datasource, Raster, Vector
from georama.integration.models.project import Project


@admin.register(Project)
class ProjectAdmin(OrganisationalModelAdmin):
    list_display = ["name", "organisation__name"]
    prefetch_organisation_related = "organisation"


@admin.register(Datasource)
class DatasourceAdmin(OrganisationalModelAdmin):
    list_display = ["name", "project__organisation__name"]
    prefetch_organisation_related = "project__organisation"


@admin.register(Custom)
class CustomAdmin(OrganisationalModelAdmin):
    list_display = ["name", "project__organisation__name"]
    prefetch_organisation_related = "project__organisation"


@admin.register(Raster)
class RasterAdmin(OrganisationalModelAdmin):
    list_display = ["name", "project__organisation__name"]
    prefetch_organisation_related = "project__organisation"


class FieldInlineAdmin(TabularInline):
    model = VectorField
    extra = 0
    exclude = ["id"]
    hide_title = True


@admin.register(Vector)
class VectorAdmin(OrganisationalModelAdmin):
    list_display = ["name", "project__organisation__name"]
    prefetch_organisation_related = "project__organisation"
    inlines = [FieldInlineAdmin]


@admin.register(VectorField)
class FieldAdmin(OrganisationalModelAdmin):
    list_display = ["name", "datasource__project__organisation__name"]
    prefetch_organisation_related = "datasource__project__organisation"
