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


class FieldInlineAdmin(TabularInline):
    model = Field
    extra = 0
    exclude = ["id"]

    def get_formset(self, request, obj=None, **kwargs):
        formset = super().get_formset(request, obj, **kwargs)
        datasource_field = formset.form.base_fields.get("datasource_field")

        if obj is None:
            datasource_field.queryset = datasource_field.queryset.none()
        else:
            datasource_field.queryset = datasource_field.queryset.filter(datasource=obj.datasource)
        return formset


@admin.register(FeatureLayer)
class FeatureLayerAdmin(OrganisationalModelAdmin):
    prefetch_organisation_related = "datasource__project__collection__organisation"
    inlines = [MetadataInlineAdmin, FieldInlineAdmin]
