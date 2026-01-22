from django.forms import ModelForm

from georama.data_integration.models import (
    CustomDataSet,
    Project,
    RasterDataSet,
    VectorDataSet,
)


class ProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = "__all__"


class VectorDataSetForm(ModelForm):
    class Meta:
        model = VectorDataSet
        fields = "__all__"


class RasterDataSetForm(ModelForm):
    class Meta:
        model = RasterDataSet
        fields = "__all__"


class CustomDataSetForm(ModelForm):
    class Meta:
        model = CustomDataSet
        fields = "__all__"
