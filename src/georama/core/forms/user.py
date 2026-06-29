from django import forms

from georama.core.models import GeoramaUser


class GeoramaUserForm(forms.ModelForm):
    class Meta:
        model = GeoramaUser
        fields = [
            "username",
            "first_name",
            "last_name",
            "email",
        ]
