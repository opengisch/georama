from django import forms

from georama.maps.models import WmsLayer


class WmsLayerModelForm(forms.ModelForm):
    class Meta:
        model = WmsLayer
        fields = [
            "metadata",
        ]
