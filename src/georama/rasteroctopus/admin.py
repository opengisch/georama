from django.contrib import admin
from django.urls import reverse
from django.utils.safestring import mark_safe

from georama.qmeleon.models import RasterDataSet, VectorDataSet
from georama.rasteroctopus.models import PublishedAsWms


@admin.register(PublishedAsWms)
class PublishedAsWmsAdmin(admin.ModelAdmin):
    list_display = ["name", "title", "public", "delete_link", "show_published"]
    add_form_template = "admin/rasteroctopus/publishedaswms/publish.html"
    fields = [
        'title',
        'name',
        'public',
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
        extra_context['raster_datasets'] = RasterDataSet.objects.all()
        extra_context['vector_datasets'] = VectorDataSet.objects.all()
        return super().add_view(
            request, form_url, extra_context=extra_context,
        )

    def delete_link(self, obj: PublishedAsWms):
        return mark_safe(
            '<a href="{}" class="btn btn-high btn-success">&#128465;</a>'.format(
                reverse(
                    "admin:rasteroctopus_publishedaswms_delete",
                    args=(obj.pk,)
                )
            )
        )

    def show_published(self, obj: PublishedAsWms):
        return mark_safe(
            '<a href="{}?service=wms&request=getcapabilities" class="btn btn-high btn-success">&#128065;</a>'.format(
                reverse("wms_entry"),
            )
        )

    def dataset_detail(self, obj: PublishedAsWms):
        if isinstance(obj.raster_dataset, RasterDataSet):
            dataset = obj.raster_dataset
            type_name = 'Raster'
        elif isinstance(obj.vector_dataset, VectorDataSet):
            dataset = obj.vector_dataset
            type_name = 'Vector'
        else:
            raise NotImplementedError('linked dataset has to be RasterDataSet|VectorDataSet!')
        return mark_safe(
            f'<a href="{reverse("admin:qmeleon_rasterdataset_change", args=(dataset.pk,))}" class="btn btn-high btn-success">{dataset.title} ({dataset.name})</a><span class="badge badge-secondary">{type_name}</span>'
        )
    dataset_detail.short_description = 'Dataset'
