import logging

from django.contrib import admin
from unfold.admin import TabularInline

from georama.core.common.admin import OrganisationalModelAdmin
from georama.features.models.feature_layer import FeatureLayer
from georama.features.models.field import Field
from georama.features.models.metadata import Metadata

logger = logging.getLogger(__name__)


class MetadataInlineAdmin(TabularInline):
    model = Metadata
    max_num = 1
    min_num = 1
    exclude = ["id"]
    hide_title = True


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
class FeatureLayerAdmin(OrganisationalModelAdmin):
    prefetch_organisation_related = "datasource__project__collection__organisation"

    def get_readonly_fields(self, request, obj=None):
        if obj is not None and obj.pk:
            return (*super().get_readonly_fields(request, obj), "datasource")
        return super().get_readonly_fields(request, obj)

    def get_inlines(self, request, obj):
        """Hook for specifying custom inlines."""
        if obj and obj.pk:
            return [MetadataInlineAdmin, FieldInlineAdmin]
        return [MetadataInlineAdmin]
