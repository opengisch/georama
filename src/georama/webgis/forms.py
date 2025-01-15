from django import forms
from django.contrib.gis.forms import OpenLayersWidget

GEOPORTAL_URLS = {
    "mapnv": "https://mapnv.ch/themes",
    "cartoriviera": "https://map.cartoriviera.ch/themes",
    "sitn": "https://sitn.ne.ch/themes",
    "mapbs": "https://map.geo.bs.ch/themes",
}


class MapWidgetFor3Dgeom(OpenLayersWidget):
    supports_3d = True
    template_name = "gis/openlayers.html"


class HomeForm(forms.Form):

    geoportal_url = forms.ChoiceField(
        label="Geoportal", required=True, choices=GEOPORTAL_URLS, widget=forms.Select
    )
