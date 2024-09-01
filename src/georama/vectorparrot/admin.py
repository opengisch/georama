from django.contrib import admin
from django.forms import BaseInlineFormSet
from django.urls import path, reverse
from django.utils.safestring import mark_safe

from georama.vectorparrot.models import (
    PublishedAsOgcApiFeatures, ColumnOgcApiFeatures
)
from georama.qmeleon.models import VectorDataSet


class ColumnOgcApiFeaturesInlineFormset(BaseInlineFormSet):
    model = ColumnOgcApiFeatures
    fields = ['name', 'title']


class ColumnOgcApiFeaturesInline(admin.TabularInline):
    model = ColumnOgcApiFeatures
    formset = ColumnOgcApiFeaturesInlineFormset
    can_delete = False
    extra = 0

    def has_add_permission(self, request, obj):
        return False


@admin.register(PublishedAsOgcApiFeatures)
class PublishedAsOgcApiFeaturesAdmin(admin.ModelAdmin):
    list_display = ["name", "title", "public", "delete_link", "show_published"]
    inlines = [ColumnOgcApiFeaturesInline]
    add_form_template = "admin/vectorparrot/publishedasvectorfeature/publish.html"
    fields = [
        'title',
        'name',
        'public',
        'column_permission',
        'description',
        'license',
        'fees',
        'access_constraints',
        'dataset_detail'
    ]
    readonly_fields = [
        'dataset_detail'
    ]

    def add_view(self, request, form_url='', extra_context=None):
        extra_context = extra_context or {}
        vector_datasets = VectorDataSet.objects.all()
        extra_context['vector_datasets'] = [
            (vd, reverse('publish_as_oapif', args=[vd.id])) for vd in vector_datasets
        ]
        return super().add_view(
            request, form_url, extra_context=extra_context,
        )

    def delete_link(self, obj: PublishedAsOgcApiFeatures):
        return mark_safe(
            '<a href="{}" class="btn btn-high btn-success">&#128465;</a>'.format(
                reverse(
                    "admin:vectorparrot_publishedasogcapifeatures_delete",
                    args=(obj.pk,)
                )
            )
        )

    def show_published(self, obj: PublishedAsOgcApiFeatures):
        return mark_safe(
            '<a href="{}" class="btn btn-high btn-success">&#128065;</a>'.format(
                reverse(
                    "collection-detail",
                    args=(str(obj.identifier),)
                )
            )
        )

    def dataset_detail(self, obj: PublishedAsOgcApiFeatures):
        return mark_safe(
            f'<a href="{reverse("admin:qmeleon_vectordataset_change", args=(obj.dataset.pk,))}">{obj.dataset.title} ({obj.dataset.name})</a>'
        )
    dataset_detail.short_description = 'Dataset'
