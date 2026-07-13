from django import forms
from django.forms import modelformset_factory

from georama.features.models import Field


class FieldModelForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={"readonly": "readonly"}))

    class Meta:
        model = Field
        fields = [
            "name",
            "visible",
        ]


FieldFormSet = modelformset_factory(Field, fields=["name", "visible"], extra=0, form=FieldModelForm)
