from django import forms
from django.forms import Widget
from django.urls import reverse
from pyproj import CRS

from django.contrib.admin import widgets
from django.contrib.auth.models import Group, User
from qgis_server_light.interface.qgis import BBox

from georama.maps.models import PublishedAsWms


class LayerExtentWidget(Widget):
    class Media:
        css = {
            "all": ["https://cdn.jsdelivr.net/npm/ol@v10.6.1/ol.css"],
        }
        js = (
            "https://cdn.jsdelivr.net/npm/ol@v10.6.1/dist/ol.js",
            "https://cdn.jsdelivr.net/npm/proj4@2.19.10/dist/proj4.min.js",
        )

    template_name = "admin/maps/preview_map/preview_map.html"

    @staticmethod
    def extent_center(extent: BBox) -> list[float]:
        return (
            [
                extent.x_min + (extent.x_max - extent.x_min) / 2,
                extent.y_min + (extent.y_max - extent.y_min) / 2,
            ]
            if extent
            else []
        )

    @staticmethod
    def proj4_def(layer_srid):
        return CRS.from_epsg(layer_srid.replace("EPSG:", "")).to_proj4()

    def get_context(self, name, value, attrs):
        context = super().get_context(name, value, attrs)
        widget_attrs = context["widget"]["attrs"]
        extent: BBox = BBox.from_string(value)

        context["extent"] = extent.to_2d_string()
        context["layer_srid"] = widget_attrs["layer_srid"]
        context["original_extent"] = BBox.from_string(
            widget_attrs["original_extent"]
        ).to_2d_string()
        context["layer_url"] = widget_attrs["layer_url"]
        context["layer_name"] = widget_attrs["layer_name"]
        context["proj4_def"] = self.proj4_def(widget_attrs["layer_srid"])
        context["center"] = self.extent_center(extent)
        context["map_width"] = widget_attrs["map_width"]
        context["map_height"] = widget_attrs["map_height"]
        return context


class PublishedAsWmsForm(forms.ModelForm):
    class Meta:
        model = PublishedAsWms
        fields = "__all__"
        widgets = {
            "extent": LayerExtentWidget(),
        }

    group_read_permission = forms.ModelMultipleChoiceField(
        required=False,
        queryset=None,
        widget=widgets.FilteredSelectMultiple(
            verbose_name="Group read permission", is_stacked=False
        ),
    )

    user_read_permission = forms.ModelMultipleChoiceField(
        required=False,
        queryset=None,
        widget=widgets.FilteredSelectMultiple(
            verbose_name="User read permission", is_stacked=False
        ),
    )

    @staticmethod
    def get_first_match_partial_key(dictionary, partial_key):
        matches = [k for k, v in dictionary.items() if partial_key in k]
        return matches[0] if matches else None

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # get the read permission, should get only one permission for PublishedAsWms
        permissions = self.instance.permissions
        permission_read = [p.codename for p in permissions][0]

        # filling the field with the correct queryset and initialize it with the data from the db

        self.fields["group_read_permission"].queryset = Group.objects.all()
        self.fields["group_read_permission"].initial = Group.objects.filter(
            permissions__codename=permission_read
        )

        self.fields["user_read_permission"].queryset = User.objects.all().exclude(
            is_superuser=True
        )
        self.fields["user_read_permission"].initial = User.objects.filter(
            user_permissions__codename=permission_read
        ).exclude(is_superuser=True)

        if self.instance.name:
            # Provide additional context for the map widget for defining the layer extent
            widget_attrs = {
                "layer_srid": self.instance.bound_dataset.crs["AuthId"],
                "original_extent": self.instance.bound_dataset.bbox,
                "layer_url": reverse("maps_ogc_entry"),
                "layer_name": self.instance.name,
                "map_width": self.instance.preview_dimensions[0],
                "map_height": self.instance.preview_dimensions[1],
            }
            self.fields["extent"].widget.attrs.update(widget_attrs)

    def clean_extent(self):
        extent = self.cleaned_data["extent"]
        if extent:
            try:
                bbox = BBox.from_string(extent)
            except ValueError:
                raise forms.ValidationError(
                    "Invalid extent: Extent must be a comma-seperated list of 4 coordinates"
                )
            if bbox.x_min > bbox.x_max or bbox.y_min > bbox.y_max:
                raise forms.ValidationError(
                    "Invalid extent: Extent coordinates must be ordered: x_min,y_min,x_max,y_max"
                )
        return extent
