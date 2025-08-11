from dataclasses import fields
from urllib.parse import quote

from django.contrib import admin
from django.contrib.auth.models import Permission
from django.urls import reverse
from django.utils.html import format_html
from django.utils.http import urlencode
from django.utils.safestring import mark_safe
from django.utils.translation import gettext_lazy as _
from qgis_server_light.interface.qgis import BBox

from georama.core.entities.models import save_group_permissions, save_user_permissions
from georama.data_integration.models import CustomDataSet, RasterDataSet, VectorDataSet
from georama.maps.forms import PublishedAsWmsForm
from georama.maps.interfaces.georama.requests import (
    QslGetMapRequest,
    RequestType,
    ServiceType,
    Version,
)
from georama.maps.models import PublishedAsWms
from georama.maps.services.wfs_2_0_0 import WfsOperation


def wms_get_capabilities_url() -> str:
    return "{}?SERVICE=WMS&REQUEST=GETCAPABILITIES&VERSION=1.3.0".format(
        reverse("maps_ogc_entry")
    )


def wfs_get_capabilities_url() -> str:
    return "{}?SERVICE=WFS&REQUEST=GETCAPABILITIES&VERSION=2.0.0".format(
        reverse("maps_ogc_entry")
    )


@admin.register(PublishedAsWms)
class PublishedAsWmsAdmin(admin.ModelAdmin):
    list_display = [
        "icon_column",
        "name",
        "title",
        "public",
        "queryable",
        "delete_link",
        "show_published",
        "preview_image",
    ]
    list_editable = ["public", "queryable"]
    add_form_template = "admin/maps/publishedaswms/publish.html"
    readonly_fields = ["dataset_detail"]
    list_filter = ["name", "title"]
    form = PublishedAsWmsForm

    def icon_column(self, obj):
        icon = "fg-poi"
        if isinstance(obj.raster_dataset, RasterDataSet):
            icon = "fg-landcover-map"
        elif isinstance(obj.vector_dataset, VectorDataSet):
            icon = "fg-contour-map"
        elif isinstance(obj.custom_dataset, CustomDataSet):
            icon = "fg-flow-map"
        return format_html(
            f"<i class='{icon} fg-2x' style='color: black; margin: 0; padding: 0;'></i>"
        )

    icon_column.short_description = "src"
    icon_column.allow_tags = True

    def add_view(self, request, form_url="", extra_context=None):
        extra_context = extra_context or {}
        extra_context["raster_datasets"] = RasterDataSet.objects.all()
        extra_context["vector_datasets"] = VectorDataSet.objects.all()
        extra_context["custom_datasets"] = CustomDataSet.objects.all()
        extra_context["publish_dataset_as_wms_view_name"] = "maps_publish_dataset_as_wms"
        return super().add_view(
            request,
            form_url,
            extra_context=extra_context,
        )

    def changelist_view(self, request, extra_context=None):
        extra_context = extra_context or {}
        extra_context["wms_get_capabilities_url"] = wms_get_capabilities_url()
        extra_context["wfs_get_capabilities_url"] = wfs_get_capabilities_url()
        return super().changelist_view(
            request,
            extra_context=extra_context,
        )

    def delete_link(self, obj: PublishedAsWms):
        return mark_safe(
            '<a href="{}" class="btn btn-high btn-danger"><i class="fas fa-trash text-xs"/></a>'.format(
                reverse("admin:maps_publishedaswms_delete", args=(obj.pk,))
            )
        )

    @staticmethod
    def create_wms_url_params(
        layer: PublishedAsWms, img_width: int = 1500, img_height: int = 1500
    ) -> str:
        dataset = layer.bound_dataset
        if layer.extent:
            bbox = layer.extent.split(",")
        else:
            bbox_obj = BBox.from_string(dataset.bbox)
            bbox = [bbox_obj.x_min, bbox_obj.y_min, bbox_obj.x_max, bbox_obj.y_max]
        params = QslGetMapRequest(
            SERVICE=ServiceType.wms.value,
            REQUEST=RequestType.get_map.value,
            VERSION=Version.v_1_3_0.value,
            LAYERS=[layer.name],
            BBOX=bbox,
            CRS=dataset.crs_to_qsl.auth_id,
            WIDTH=img_width,
            HEIGHT=img_height,
            FORMAT="image/png",
            TRANSPARENT=True,
            STYLES="",
            DPI=72,
            FILTER=None,
            MAP_RESOLUTION=72,
            FORMAT_OPTIONS="dpi%3A72",
        )
        url_params = {}
        for field in fields(QslGetMapRequest):
            field_value = getattr(params, field.name)
            if isinstance(field_value, list):
                field_value = ",".join([str(value) for value in field_value])
            if field_value is not None:
                url_params[field.name] = field_value
        return urlencode(url_params)

    @staticmethod
    def create_wfs_url_params(layer: PublishedAsWms, output_format: str = "text/xml") -> str:
        return "&".join(
            [
                "SERVICE=WFS",
                "REQUEST=GetFeature",
                "VERSION=2.0.0",
                f'TYPENAMES={quote(f"{WfsOperation.own_namespace}:{layer.name}")}',
                f"SRSNAME={quote(layer.bound_dataset.crs_to_qsl.ogc_urn)}",
                f"outputformat={quote(output_format)}",
            ]
        )

    def show_published(self, obj: PublishedAsWms):
        return mark_safe(
            "".join(
                [
                    '<a href="{}?{}" target="_blank" class="btn btn-high btn-success" title="WMS GetMap"><i class="fas fa-eye text-xs"/></a>'.format(
                        reverse("maps_ogc_entry"), self.create_wms_url_params(obj)
                    ),
                    '<a href="{}?{}" target="_blank" class="btn btn-high btn-success" title="WFS GetFeature"><i class="fas fa-eye text-xs"/></a>'.format(
                        reverse("maps_ogc_entry"), self.create_wfs_url_params(obj)
                    ),
                ]
            )
        )

    show_published.short_description = "Operations"

    def preview_image(self, obj: PublishedAsWms):
        base64Img = "data:image/png;base64,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"
        return mark_safe(
            "".join(
                [
                    '<img src="{}" style="width: 200px; height: 200px"/>'.format(base64Img),
                ]
            )
        )

    preview_image.short_description = "Layer preview"

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

    def get_fieldsets(self, request, obj=None):
        fields = [
            "title",
            "name",
            "public",
            "description",
            "license",
            "fees",
            "access_constraints",
            "dataset_detail",
            "queryable",
        ]
        if obj:
            if isinstance(obj.vector_dataset, VectorDataSet):
                fields.append("extent_buffer")
                fields.append("extent")
        return (
            (
                None,
                {"fields": fields},
            ),
            ("Group permissions", {"fields": ("group_read_permission",)}),
            ("User permissions", {"fields": ("user_read_permission",)}),
        )

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


def custom_links():
    return {
        "maps": [
            {
                "name": _("WMS Capabilities"),
                "url": wms_get_capabilities_url(),
                "icon": "fa fa-eye",
            }
        ]
    }
