from georama.core.services.multi_model.base import Service
from georama.data_integration.models import CustomDataSet, RasterDataSet, VectorDataSet


class ProjectDatasetsService(Service):
    models = [VectorDataSet, RasterDataSet, CustomDataSet]
    name = "project_dataset"

    def filter(self, query, **kwargs):
        return query.filter(project__pk=kwargs["pk"])
