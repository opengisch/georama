import base64
from dataclasses import fields
from urllib.parse import quote

from django.contrib import admin
from django.contrib.auth.models import Permission
from django.templatetags.static import static
from django.urls import reverse
from django.utils.html import format_html
from django.utils.http import urlencode
from django.utils.safestring import mark_safe
from django.utils.translation import gettext_lazy as _
from qgis_server_light.interface.common import BBox

from georama.core.entities.models import save_group_permissions, save_user_permissions
from georama.data_integration.models import CustomDataSet, RasterDataSet, VectorDataSet
from georama.maps.forms import PublishedAsWmsAdminForm
from georama.maps.interfaces.georama.requests import (
    GetMapRequestParams,
    RequestType,
    ServiceType,
    Version,
)
from georama.maps.models import PublishedAsWms
from georama.maps.services.wfs_2_0_0 import WfsOperation


def wms_get_capabilities_url() -> str:
    return "{}?SERVICE=WMS&REQUEST=GETCAPABILITIES&VERSION=1.3.0".format(
        reverse("maps:maps_ogc_entry")
    )


def wfs_get_capabilities_url() -> str:
    return "{}?SERVICE=WFS&REQUEST=GETCAPABILITIES&VERSION=2.0.0".format(
        reverse("maps:maps_ogc_entry")
    )


@admin.register(PublishedAsWms)
class PublishedAsWmsAdmin(admin.ModelAdmin):
    list_display = [
        "icon_column",
        "name",
        "title",
        "public",
        "queryable",
        "operations",
        "preview_image",
    ]
    list_editable = ["public", "queryable"]
    list_display_links = ["icon_column", "name", "title"]
    add_form_template = "admin/maps/publishedaswms/publish.html"
    readonly_fields = ["dataset_detail", "extent_wgs84"]
    list_filter = ["name", "title"]
    form = PublishedAsWmsAdminForm

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
        extra_context["publish_dataset_as_wms_view_name"] = "maps:layer-add"
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

    @staticmethod
    def create_wms_url_params(
        layer: PublishedAsWms, img_width: int = 1500, img_height: int = 1500
    ) -> str:
        dataset = layer.bound_dataset
        bbox = BBox.from_string(layer.extent).to_2d_list()
        params = GetMapRequestParams(
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
        for field in fields(GetMapRequestParams):
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
                f"TYPENAMES={quote(f'{WfsOperation.own_namespace}:{layer.name}')}",
                f"SRSNAME={quote(layer.bound_dataset.crs_to_qsl.ogc_urn)}",
                f"outputformat={quote(output_format)}",
            ]
        )

    def operations(self, obj: PublishedAsWms):
        links = []
        links += f'<a href="{reverse("maps:maps_ogc_entry")}?{self.create_wms_url_params(obj)}" target="_blank" class="btn btn-high btn-success x-1" title="WMS GetMap"><i class="fas fa-map text-xs"></i></a>'  # noqa: E501
        if obj.is_queryable:
            links += f'<a href="{reverse("maps:maps_ogc_entry")}?{self.create_wfs_url_params(obj)}" target="_blank" class="btn btn-high btn-success x-1" title="WFS GetFeature"><i class="fas fa-code text-xs"></i></a>'  # noqa: E501
        links += f'<a href="{reverse("admin:maps_publishedaswms_delete", args=(obj.pk,))}" class="btn btn-high btn-danger"><i class="fas fa-trash-alt text-xs"/></a>'  # noqa: E501
        return mark_safe(f'<div class="btn-group" role="group">{"".join(links)}</div>')

    operations.short_description = "Operations"

    def preview_image(self, obj: PublishedAsWms):
        if obj.preview:
            img_src = f"data:image/png;base64,{base64.b64encode(obj.preview).decode()}"
            dimensions = obj.preview_dimensions
        else:
            img_src = static("wms-placeholder.svg")
            dimensions = (250, 195)
        return mark_safe(
            "".join(
                [
                    '<img src="{}" class="border shadow-sm" style="width: {}px; height: {}px"/>'.format(  # noqa: E501
                        img_src, *dimensions
                    ),
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
            f'<a href="{reverse(f"admin:data_integration_{type_name.lower()}dataset_change", args=(dataset.pk,))}" class="btn btn-high btn-success">{dataset.title} ({dataset.name})</a><span class="badge badge-secondary">{type_name}</span>'  # noqa: E501
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
        if obj and isinstance(obj.vector_dataset, VectorDataSet):
            fields.append("extent_buffer")
            fields.append("extent")
            fields.append("extent_wgs84")
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
