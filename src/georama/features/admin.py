from django.contrib import admin
from django.contrib.auth.models import Permission
from django.forms import BaseInlineFormSet
from django.urls import reverse
from django.utils.safestring import mark_safe

from georama.core.entities.models import save_group_permissions, save_user_permissions
from georama.data_integration.models import VectorDataSet
from georama.features.forms import PublishedAsOgcApiFeaturesForm
from georama.features.models import ColumnOgcApiFeatures, PublishedAsOgcApiFeatures


class ColumnOgcApiFeaturesInlineFormset(BaseInlineFormSet):
    model = ColumnOgcApiFeatures
    fields = ["name", "title"]


class ColumnOgcApiFeaturesInline(admin.TabularInline):
    model = ColumnOgcApiFeatures
    formset = ColumnOgcApiFeaturesInlineFormset
    can_delete = False
    extra = 0

    def has_add_permission(self, request, obj):
        return False


def _get_permissions(obj: PublishedAsOgcApiFeatures, permission_type: str):
    permissions = obj.permissions
    return [p.codename for p in permissions if permission_type in p.codename][0]


@admin.register(PublishedAsOgcApiFeatures)
class PublishedAsOgcApiFeaturesAdmin(admin.ModelAdmin):
    list_display = ["name", "title", "public", "delete_link", "show_published"]
    inlines = [ColumnOgcApiFeaturesInline]
    add_form_template = "admin/features/publishedasvectorfeature/publish.html"
    list_editable = ["public"]
    readonly_fields = ["dataset_detail"]

    form = PublishedAsOgcApiFeaturesForm

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
                    "dataset_detail",
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

    def add_view(self, request, form_url="", extra_context=None):
        extra_context = extra_context or {}
        vector_datasets = VectorDataSet.objects.all()
        extra_context["vector_datasets"] = [
            (vd, reverse("publish_as_oapif", args=[vd.id])) for vd in vector_datasets
        ]
        return super().add_view(
            request,
            form_url,
            extra_context=extra_context,
        )

    def delete_link(self, obj: PublishedAsOgcApiFeatures):
        return mark_safe(
            '<a href="{}" class="btn btn-high btn-success">&#128465;</a>'.format(
                reverse("admin:features_publishedasogcapifeatures_delete", args=(obj.pk,))
            )
        )

    def show_published(self, obj: PublishedAsOgcApiFeatures):
        return mark_safe(
            '<a href="{}" class="btn btn-high btn-success">&#128065;</a>'.format(
                reverse("collection-detail", args=(str(obj.identifier),))
            )
        )

    def dataset_detail(self, obj: PublishedAsOgcApiFeatures):
        return mark_safe(
            f'<a href="{reverse("admin:features_publishedasogcapifeatures_change", args=(obj.dataset.pk,))}">{obj.dataset.title} ({obj.dataset.name})</a>'
        )

    def save_model(self, request, obj, form, change):
        permissions_dct = {"read": "", "create": "", "update": "", "delete": ""}

        # query the correct permission object
        for permission_type in permissions_dct.keys():
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

    dataset_detail.short_description = "Dataset"
