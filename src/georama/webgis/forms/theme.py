from django import forms

from georama.webgis.models import Theme


class ThemeModelForm(forms.ModelForm):
    class Meta:
        model = Theme
        fields = [
            "project",
            "public",
            "ordering",
        ]
