from django import forms
from django.forms import Widget
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

    layer_srid = 4326
    extent = ""

    @property
    def extent_as_numbers(self) -> list[float]:
        if self.extent:
            return [float(e) for e in self.extent.split(",")]
        return []

    @property
    def extent_center(self) -> list[float]:
        e = self.extent_as_numbers
        return (
            [
                e[0] + (e[2] - e[0]) / 2,
                e[1] + (e[3] - e[1]) / 2,
            ]
            if e
            else []
        )

    @property
    def proj4_def(self):
        return CRS.from_epsg(self.layer_srid.replace("EPSG:", "")).to_proj4()

    def format_value(self, value):
        return self.to2dExtent(value)

    def get_context(self, name, value, attrs):
        context = super().get_context(name, value, attrs)

        self.extent = self.to2dExtent(value)
        self.layer_srid = context["widget"]["attrs"]["layer_srid"]

        context["extent"] = self.extent
        context["layer_srid"] = self.layer_srid
        context["proj4_def"] = self.proj4_def
        context["center"] = self.extent_center
        return context

    @staticmethod
    def to2dExtent(value: str) -> str:
        if not value:
            return ""
        extent = value.split(",")
        if len(extent) == 4:
            return value
        elif len(extent) == 6:
            return ",".join([extent[0], extent[1], extent[3], extent[4]])
        else:
            raise ValueError("Extent must be a comma-seperated list of 4 or 6 coordinates")


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

        # Set the layer srid for the custom extent widget
        if self.instance.get_vector_dataset:
            self.fields["extent"].widget.attrs["layer_srid"] = (
                self.instance.get_vector_dataset.crs["AuthId"]
            )

    def clean_extent(self):
        extent = self.cleaned_data["extent"]
        if extent is not None:
            if len(extent.split(",")) != 4:
                raise forms.ValidationError(
                    "Extent must be a comma-seperated list of 4 coordinates"
                )
            for coord in extent.split(","):
                # TODO Do CRS based validation
                pass
        return extent
