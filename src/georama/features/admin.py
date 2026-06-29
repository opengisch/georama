import logging

from django.contrib import admin
from guardian.admin import GuardedModelAdminMixin
from unfold.admin import ModelAdmin, TabularInline

from georama.core.common.admin import OrganisationalModelAdmin
from georama.features.models.feature_layer import (
    FeatureLayer,
    FeatureLayerGroupObjectPermission,
    FeatureLayerUserObjectPermission,
)
from georama.features.models.field import Field
from georama.features.models.metadata import Metadata

logger = logging.getLogger(__name__)


class FieldInlineAdmin(TabularInline):
    model = Field
    extra = 0
    exclude = ["id"]
    fields = ("datasource_field", "name", "visible")
    readonly_fields = ("datasource_field",)
    hide_title = True

    def has_delete_permission(self, request, obj=None):
        return False

    def has_add_permission(self, request, obj=None):
        return False


@admin.register(FeatureLayer)
class FeatureLayerAdmin(GuardedModelAdminMixin, OrganisationalModelAdmin):
    prefetch_organisation_related = "datasource__project__collection__organisation"

    def get_readonly_fields(self, request, obj=None):
        if obj is not None and obj.pk:
            return (*super().get_readonly_fields(request, obj), "datasource")
        return super().get_readonly_fields(request, obj)

    def get_inlines(self, request, obj):
        """Hook for specifying custom inlines."""
        if obj and obj.pk:
            return [FieldInlineAdmin]
        return []


@admin.register(FeatureLayerUserObjectPermission)
class FeatureLayerUserObjectPermissionAdmin(OrganisationalModelAdmin):
    readonly_fields = ["time_created"]

    def get_list_display(self, request):
        return (*super().get_list_display(request), "time_created")


@admin.register(FeatureLayerGroupObjectPermission)
class FeatureLayerGroupObjectPermissionAdmin(OrganisationalModelAdmin):
    readonly_fields = ["time_created"]

    def get_list_display(self, request):
        return (*super().get_list_display(request), "time_created")


@admin.register(Metadata)
class MetadataAdmin(ModelAdmin):
    prefetch_organisation_related = "feature_layer__datasource__project__collection__organisation"
