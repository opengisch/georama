from django.contrib import admin
from django.contrib.auth.models import Permission
from django.forms import BaseInlineFormSet
from django.urls import reverse
from django.utils.html import format_html
from django.utils.safestring import mark_safe
from django.utils.translation import gettext as _

from georama.core.entities.models import save_group_permissions, save_user_permissions
from georama.data_integration.models import VectorDataSet
from georama.features.apps import FeaturesConfig
from georama.features.forms import PublishedAsOgcApiFeaturesAdminForm
from georama.features.models import ColumnOgcApiFeatures, PublishedAsOgcApiFeatures

appname = FeaturesConfig.get_simple_appname()


class ColumnOgcApiFeaturesInlineFormset(BaseInlineFormSet):
    model = ColumnOgcApiFeatures
    fields = ["name", "title"]


class ColumnOgcApiFeaturesInline(admin.TabularInline):
    model = ColumnOgcApiFeatures
    formset = ColumnOgcApiFeaturesInlineFormset
    readonly_fields = ["dataset_column"]
    can_delete = False
    extra = 0

    def has_add_permission(self, request, obj):
        return False


def _get_permissions(obj: PublishedAsOgcApiFeatures, permission_type: str):
    permissions = obj.permissions
    return [p.codename for p in permissions if permission_type in p.codename][0]


@admin.register(PublishedAsOgcApiFeatures)
class PublishedAsOgcApiFeaturesAdmin(admin.ModelAdmin):
    list_display = ["icon_column", "name", "title", "public", "operations"]
    list_display_links = ["icon_column", "name", "title"]
    inlines = [ColumnOgcApiFeaturesInline]
    add_form_template = "admin/features/publishedasvectorfeature/publish.html"
    list_editable = ["public"]
    readonly_fields = ["dataset"]

    form = PublishedAsOgcApiFeaturesAdminForm

    fieldsets = (
        (
            None,
            {
                "fields": (
                    "title",
                    "name",
                    "public",
                    "column_permission",
                    "description",
                    "license",
                    "fees",
                    "access_constraints",
                    "dataset",
                    "max_items",
                    "default_items",
                    "on_exceed",
                )
            },
        ),
        (
            "Group permissions",
            {
                "fields": (
                    "group_read_permission",
                    "group_create_permission",
                    "group_update_permission",
                    "group_delete_permission",
                )
            },
        ),
        (
            "User permissions",
            {
                "fields": (
                    "user_read_permission",
                    "user_create_permission",
                    "user_update_permission",
                    "user_delete_permission",
                )
            },
        ),
    )

    def icon_column(self, obj):
        icon = "fg-contour-map"
        return format_html(
            f"<i class='{icon} fg-2x' style='color: black; margin: 0; padding: 0;'></i>"
        )

    icon_column.short_description = "src"
    icon_column.allow_tags = True

    def add_view(self, request, form_url="", extra_context=None):
        extra_context = extra_context or {}
        vector_datasets = VectorDataSet.objects.all()
        extra_context["vector_datasets"] = [
            (
                vd,
                f'{reverse("features:layer-add", kwargs={"vector_dataset_id": vd.id})}?next={reverse("admin:features_publishedasogcapifeatures_changelist")}',  # noqa 501
            )
            for vd in vector_datasets
        ]
        return super().add_view(
            request,
            form_url,
            extra_context=extra_context,
        )

    def obj_perms_manage_view(self, request, object_pk, extra_context=None):
        # Call the original but ignore extra_context if needed
        return super().obj_perms_manage_view(request, object_pk)

    def operations(self, obj: PublishedAsOgcApiFeatures):
        operations = [
            '<div class="btn-group" role="group">',
            '<a href="{}" target="_blank" class="btn btn-high btn-success x-1" '
            'title="{}"><i class="fas fa-map text-xs"></i></a>'.format(
                reverse(f"{appname}:api-collection-detail", args=(str(obj.identifier),)),
                _("Open OAPIF Collection GUI in new Tab"),
            ),
            '<a href="{}" target="_blank" class="btn btn-high btn-danger x-1" '
            'title="{}"><i class="fas fa-trash-alt text-xs"></i></a>'.format(
                reverse("admin:features_publishedasogcapifeatures_delete", args=(obj.pk,)),
                _("Delete item"),
            ),
            "</div>",
        ]
        return mark_safe("".join(operations))

    operations.short_description = "Operations"

    def save_model(self, request, obj, form, change):
        permissions_dct = {"read": "", "create": "", "update": "", "delete": ""}

        # query the correct permission object
        for permission_type in permissions_dct:
            permissions_dct[permission_type] = Permission.objects.get(
                codename=_get_permissions(obj, permission_type)
            )

        # save the permissions
        for permission_type, permission in permissions_dct.items():
            # save group permissions
            groups = form.cleaned_data.get(f"group_{permission_type}_permission", [])
            save_group_permissions(groups, permission)
            # save user permissions
            users = form.cleaned_data.get(f"user_{permission_type}_permission", [])
            save_user_permissions(users, permission)

        super().save_model(request, obj, form, change)
