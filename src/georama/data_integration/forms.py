from django.forms import ModelForm

from georama.data_integration.models import Project


class ProjectForm(ModelForm):
    class Meta:
        model = Project
        exclude = []
