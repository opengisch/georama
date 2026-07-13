from django import forms

from georama.features.models import FeatureLayer, Metadata


class MetadataForm(forms.ModelForm):
    class Meta:
        model = Metadata
        fields = [
            "title",
            "description",
            "license",
            "fees",
            "access_constraints",
        ]


class FeatureLayerModelForm(forms.ModelForm):
    class Meta:
        model = FeatureLayer
        fields = [
            "default_items",
            "max_items",
            "on_exceed",
            "metadata",
        ]
