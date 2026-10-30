import logging

from django.contrib import admin
from unfold.admin import ModelAdmin

from georama.core.common.admin import OrganisationalModelAdmin
from georama.webgis.models import Metadata, Theme, WmsLayer
from georama.webgis.models.theme import ThemeGroupObjectPermission, ThemeUserObjectPermission

logger = logging.getLogger(__name__)


@admin.register(WmsLayer)
class WmsLayerAdmin(OrganisationalModelAdmin):
    prefetch_organisation_related = "datasource__project__organisation"

    def get_readonly_fields(self, request, obj=None):
        if obj is not None and obj.pk:
            return (*super().get_readonly_fields(request, obj), "datasource")
        return super().get_readonly_fields(request, obj)


@admin.register(ThemeUserObjectPermission)
class WmsLayerUserObjectPermissionAdmin(OrganisationalModelAdmin):
    readonly_fields = ["time_created"]

    def get_list_display(self, request):
        return (*super().get_list_display(request), "time_created")


@admin.register(ThemeGroupObjectPermission)
class WmsLayerGroupObjectPermissionAdmin(OrganisationalModelAdmin):
    readonly_fields = ["time_created"]

    def get_list_display(self, request):
        return (*super().get_list_display(request), "time_created")


@admin.register(Metadata)
class MetadataAdmin(ModelAdmin):
    prefetch_organisation_related = "wms_layer__datasource__project__organisation"


@admin.register(Theme)
class ThemeAdmin(OrganisationalModelAdmin):
    prefetch_organisation_related = "project__organisation"
