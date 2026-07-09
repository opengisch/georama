from django import forms

from georama.features.models import FeatureLayer


class FeatureLayerModelForm(forms.ModelForm):
    class Meta:
        model = FeatureLayer
        fields = [
            "default_items",
            "max_items",
            "on_exceed",
            "metadata",
        ]
