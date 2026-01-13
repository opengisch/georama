from dataclasses import fields
from urllib.parse import quote

from django.contrib import admin
from django.contrib.auth.models import Permission
from django.urls import reverse
from django.utils.http import urlencode
from django.utils.safestring import mark_safe
from django.utils.translation import gettext_lazy as _
from qgis_server_light.interface.qgis import BBox

from georama.core.entities.models import save_group_permissions, save_user_permissions
from georama.data_integration.models import (
    Project,
    DataSet,
    CustomDataSet,
    RasterDataSet,
    VectorDataSet,
)
from georama.maps.forms import PublishedAsWmsForm
from georama.maps.interfaces.georama.requests import (
    QslGetMapRequest,
    RequestType,
    ServiceType,
    Version,
)
from georama.maps.models import PublishedAsWms
from georama.maps.services.wfs_2_0_0 import WfsOperation
from maps.apps import MapsConfig


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
    add_form_template = "admin/maps/publishedaswms/publish.html"
    readonly_fields = ["dataset_detail", "extent_wgs84"]
    form = PublishedAsWmsForm

    def add_view(self, request, form_url="", extra_context=None):
        field_labels = {
            "name": DataSet._meta.get_field("name").verbose_name,
            "title": DataSet._meta.get_field("title").verbose_name,
            "project": Project._meta.verbose_name,
            "mandant": Project._meta.get_field("mandant").verbose_name,
        }
        nav_labels = {
            "vector": VectorDataSet._meta.verbose_name_plural,
            "raster": RasterDataSet._meta.verbose_name_plural,
            "custom": CustomDataSet._meta.verbose_name_plural,
        }

        extra_context = extra_context or {}
        extra_context.update(
            dict(
                # Include common variables for rendering the admin template.
                self.admin_site.each_context(request),
                vector_datasets=VectorDataSet.objects.all(),
                raster_datasets=RasterDataSet.objects.all(),
                custom_datasets=CustomDataSet.objects.all(),
                publish_dataset_as_wms_view_name="maps_publish_dataset_as_wms",
                field_labels=field_labels,
                nav_labels=nav_labels,
                model_name=PublishedAsWms._meta.verbose_name_plural,
                app_label=MapsConfig.get_simple_appname(),
                app_verbose_name=MapsConfig.verbose_name,
            )
        )

        return super().add_view(
            request,
            form_url,
            extra_context=extra_context,
        )

    def change_view(self, request, object_id=None, form_url="", extra_context=None):
        extra_context = extra_context or {}
        extra_context["show_save_and_add_another"] = False
        return super().change_view(
            request,
            object_id,
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

    dataset_detail.short_description = _("Dataset")

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
