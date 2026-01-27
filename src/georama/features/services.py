from django.contrib.auth.models import Permission

from georama.core.services import Service
from georama.data_integration.models import VectorDataSet
from georama.features.apps import central_app_label
from georama.features.models import PublishedAsOgcApiFeatures


class PublishedAsOgcApiFeaturesService(Service):
    models = [PublishedAsOgcApiFeatures]
    name = "ogcapi-f"


class VectorDatasetService(Service):
    models = [VectorDataSet]
    name = "vector_dataset"


class PermissionService(Service):
    models = [Permission]
    name = "permission"

    def filter(self, query, **kwargs):
        return query.filter(
            content_type__model=PublishedAsOgcApiFeatures._meta.model_name
        ).filter(codename__startswith=central_app_label)

    def get(self) -> list[Permission]:
        items = []
        for model in self.models:
            items += self.filter(model.objects).all()
        return items
