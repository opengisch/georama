from adminsortable2.admin import SortableAdminMixin
from django.contrib import admin
from django.http import HttpRequest
from django.template.response import TemplateResponse
from django.urls import path
from django.utils.translation import gettext_lazy as _
from treebeard.admin import TreeAdmin
from treebeard.forms import movenodeform_factory

from georama.data_integration.models import Project
from georama.webgis import models


class LayerWmsAdmin(admin.ModelAdmin):
    pass


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
    list_display = ("name", "mandant_name")
    inlines = [
        LayergroupmpInlines,
    ]

    def mandant_name(self, obj: models.PublishedAsTheme) -> str:
        return obj.project.mandant.name

    def get_urls(self):
        urls = super().get_urls()
        my_urls = [
            path("projects/", self.admin_site.admin_view(self.projects), name="projects")
        ]
        return my_urls + urls

    def projects(self, request: HttpRequest, extra_context=None):
        publishable_projects = Project.objects.all()

        context = dict(
            # Include common variables for rendering the admin template.
            self.admin_site.each_context(request),
            # Anything else you want in the context...
            publishable_projects=publishable_projects,
        )
        return TemplateResponse(request, "admin/clogs/publishedastheme/projects.html", context)


class OgcServerAdmin(admin.ModelAdmin):
    list_display = ("name", "url")


admin.site.register(models.LayerGroupMp, LayerGroupMpAdmin)
admin.site.register(models.OgcServer, OgcServerAdmin)
admin.site.register(models.PublishedAsTheme, ThemeAdmin)
admin.site.register(models.PublishedAsLayerWms, LayerWmsAdmin)
admin.site.register(models.PublishedAsLayerWmts, LayerWmtsAdmin)
