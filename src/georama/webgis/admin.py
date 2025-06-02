from adminsortable2.admin import SortableAdminMixin
from django.contrib import admin
from django.http import HttpRequest
from django.template.response import TemplateResponse
from django.urls import path
from django.utils.translation import gettext_lazy as _
from treebeard.admin import TreeAdmin
from treebeard.forms import movenodeform_factory

from georama.data_integration.models import (
    CustomDataSet,
    Project,
    RasterDataSet,
    VectorDataSet,
)
from georama.webgis import models


class LayerWmsAdmin(admin.ModelAdmin):
    list_display = ["name", "title", "public"]
    list_editable = ["public"]

    def get_urls(self):
        urls = super().get_urls()
        my_urls = [
            path(
                "datasets/",
                self.admin_site.admin_view(self.datasets),
                name="datasets",
            )
        ]
        return my_urls + urls

    def datasets(self, request: HttpRequest, extra_context=None):
        extra_context = extra_context or {}
        extra_context.update(
            dict(
                # Include common variables for rendering the admin template.
                self.admin_site.each_context(request),
                # Anything else you want in the context...
                raster_datasets=RasterDataSet.objects.all(),
                vector_datasets=VectorDataSet.objects.all(),
                custom_datasets=CustomDataSet.objects.all(),
                publish_dataset_as_wms_view_name="webgis_publish_dataset_as_wms",
            )
        )
        return TemplateResponse(
            request, "admin/maps/publishedaswms/publish.html", extra_context
        )


class LayerWmtsAdmin(admin.ModelAdmin):
    pass


class LayerGroupMpAdmin(TreeAdmin):
    form = movenodeform_factory(models.LayerGroupMp)
    list_display = ("name",)


class LayergroupmpInlines(admin.TabularInline):
    model = models.LayerGroupMp
    extra = 2
    verbose_name = _("Groupe de couche")
    verbose_name_plural = _("Groupes de couches")


class ThemeAdmin(SortableAdminMixin, admin.ModelAdmin):
    # overwrite this directly to circumnavigate problem of template which otherwise is located in different
    # path
    change_list_template = "admin/webgis/publishedastheme/change_list.html"
    list_display = ("name",)
    # inlines = [
    #     LayergroupmpInlines,
    # ]

    def get_urls(self):
        urls = super().get_urls()
        my_urls = [
            path("projects", self.admin_site.admin_view(self.projects), name="projects")
        ]
        return my_urls + urls

    def projects(self, request: HttpRequest, extra_context=None):
        publishable_projects = Project.objects.all()
        extra_context = extra_context or {}
        extra_context.update(
            dict(
                # Include common variables for rendering the admin template.
                self.admin_site.each_context(request),
                # Anything else you want in the context...
                publishable_projects=publishable_projects,
            )
        )
        return TemplateResponse(
            request, "admin/webgis/publishedastheme/projects.html", extra_context
        )


class OgcServerAdmin(admin.ModelAdmin):
    list_display = ("name", "url")


admin.site.register(models.LayerGroupMp, LayerGroupMpAdmin)
admin.site.register(models.OgcServer, OgcServerAdmin)
admin.site.register(models.PublishedAsTheme, ThemeAdmin)
admin.site.register(models.PublishedAsLayerWms, LayerWmsAdmin)
admin.site.register(models.PublishedAsLayerWmts, LayerWmtsAdmin)
