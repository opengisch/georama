from dataclasses import fields

from django.contrib import admin
from django.contrib.auth.models import Permission
from django.urls import reverse
from django.utils.safestring import mark_safe
from qgis_server_light.interface.qgis import BBox

from georama.core.entities.models import save_group_permissions, save_user_permissions
from georama.data_integration.models import CustomDataSet, RasterDataSet, VectorDataSet
from georama.maps.forms import PublishedAsWmsForm
from georama.maps.interfaces.ogc.wms_1_3_0.requests import (
    QslGetMapRequest,
    RequestType,
    ServiceType,
    Version,
)
from georama.maps.models import PublishedAsWms


@admin.register(PublishedAsWms)
class PublishedAsWmsAdmin(admin.ModelAdmin):
    list_display = ["name", "title", "public", "delete_link", "show_published"]
    list_editable = ["public"]
    add_form_template = "admin/maps/publishedaswms/publish.html"
    readonly_fields = ["dataset_detail"]
    list_filter = ["name", "title"]
    form = PublishedAsWmsForm

    fieldsets = (
        (
            None,
            {
                "fields": (
                    "name",
                    "title",
                    "public",
                    "description",
                    "license",
                    "fees",
                    "access_constraints",
                    "extent_buffer",
                )
            },
        ),
        ("Group permissions", {"fields": ("group_read_permission",)}),
        ("User permissions", {"fields": ("user_read_permission",)}),
    )

    def add_view(self, request, form_url="", extra_context=None):
        extra_context = extra_context or {}
        extra_context["raster_datasets"] = RasterDataSet.objects.all()
        extra_context["vector_datasets"] = VectorDataSet.objects.all()
        extra_context["custom_datasets"] = CustomDataSet.objects.all()
        return super().add_view(
            request,
            form_url,
            extra_context=extra_context,
        )

    def delete_link(self, obj: PublishedAsWms):
        return mark_safe(
            '<a href="{}" class="btn btn-high btn-danger"><i class="fas fa-trash text-xs"/></a>'.format(
                reverse("admin:maps_publishedaswms_delete", args=(obj.pk,))
            )
        )

    @staticmethod
    def create_url_params(layer: PublishedAsWms) -> str:
        dataset = layer.bound_dataset
        bbox = BBox.from_string(dataset.bbox)
        params = QslGetMapRequest(
            ServiceType.wms.value,
            RequestType.get_map.value,
            Version.v_1_3_0.value,
            [layer.name],
            [bbox.x_min, bbox.y_min, bbox.x_max, bbox.y_max],
            dataset.crs_to_qsl.auth_id,
            1500,
            1500,
            "image/png",
            True,
            "",
            72,
            72,
            "dpi%3A72",
        )
        parameter_list = []
        for field in fields(QslGetMapRequest):
            field_value = getattr(params, field.name)
            if isinstance(field_value, list):
                field_value = ",".join([str(value) for value in field_value])
            if field_value is not None:
                parameter_list.append(f"{field.name}={field_value}")
        return "&".join(parameter_list)

    def show_published(self, obj: PublishedAsWms):
        # http://localhost:8080/maps?
        # SERVICE=WMS
        # &VERSION=1.3.0
        # &REQUEST=GetMap
        # &BBOX=2686193.854178806767%2C1223001.263198361266%2C2686272.45949376747%2C1226906.964785467368
        # &CRS=EPSG%3A2056
        # &WIDTH=32
        # &HEIGHT=1590
        # &LAYERS=zg_erdverlegter_tank_ausser_betrieb
        # &STYLES=
        # &FORMAT=image%2Fpng
        # &DPI=315
        # &MAP_RESOLUTION=315
        # &FORMAT_OPTIONS=dpi%3A315
        # &TRANSPARENT=TRUE

        return mark_safe(
            '<a href="{}?{}" target="_blank" class="btn btn-high btn-success"><i class="fas fa-eye text-xs"/></a>'.format(
                reverse("ogc_entry"), self.create_url_params(obj)
            )
        )

    def dataset_detail(self, obj: PublishedAsWms):
        if isinstance(obj.raster_dataset, RasterDataSet):
            dataset = obj.raster_dataset
            type_name = "Raster"
        elif isinstance(obj.vector_dataset, VectorDataSet):
            dataset = obj.vector_dataset
            type_name = "Vector"
        elif isinstance(obj.custom_dataset, CustomDataSet):
            dataset = obj.custom_dataset
            type_name = "Custom"
        else:
            raise NotImplementedError(
                "linked dataset has to be RasterDataSet|VectorDataSet|CustomDataSet!"
            )
        return mark_safe(
            f'<a href="{reverse(f"admin:data_integration_{type_name.lower()}dataset_change", args=(dataset.pk,))}" class="btn btn-high btn-success">{dataset.title} ({dataset.name})</a><span class="badge badge-secondary">{type_name}</span>'
        )

    dataset_detail.short_description = "Dataset"

    def get_fields(self, request, obj=None):
        fields = [
            "title",
            "name",
            "public",
            "description",
            "license",
            "fees",
            "access_constraints",
            "dataset_detail",
        ]
        if obj:
            if isinstance(obj.vector_dataset, VectorDataSet):
                fields.append("extent_buffer")
        return fields

    def save_model(self, request, obj, form, change):
        # read permission -> should get only one for PublishedAsWms
        read_permission = Permission.objects.get(codename=obj.permissions[0].codename)

        # save group permissions
        groups_read = form.cleaned_data.get("group_read_permission", [])
        save_group_permissions(groups_read, read_permission)

        # save user permissions
        users_read = form.cleaned_data.get("user_read_permission", [])
        save_user_permissions(users_read, read_permission)

        super().save_model(request, obj, form, change)
