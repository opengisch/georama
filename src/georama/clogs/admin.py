from adminsortable2.admin import SortableAdminMixin
from django.contrib import admin
from treebeard.admin import TreeAdmin
from treebeard.forms import movenodeform_factory
from georama.clogs import models
from django.utils.translation import gettext_lazy as _


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

class OgcServerAdmin(admin.ModelAdmin):
    list_display = ("name", "url")


admin.site.register(models.LayerGroupMp, LayerGroupMpAdmin)
admin.site.register(models.OgcServer, OgcServerAdmin)
admin.site.register(models.PublishedAsTheme, ThemeAdmin)
admin.site.register(models.PublishedAsLayerWms, LayerWmsAdmin)
admin.site.register(models.PublishedAsLayerWmts, LayerWmtsAdmin)
