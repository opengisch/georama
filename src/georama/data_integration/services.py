from georama.core.services import Service
from georama.data_integration.models import (
    CustomDataSet,
    Project,
    RasterDataSet,
    VectorDataSet,
)


class ProjectService(Service):
    models = [Project]


class ProjectDatasetsService(Service):
    models = [VectorDataSet, RasterDataSet, CustomDataSet]

    def count(self):
        count = 0
        for model in self.models:
            count += model.objects.filter(project__isnull=False).count()
        return count


class ManualDatasetService(Service):
    models = [VectorDataSet, RasterDataSet, CustomDataSet]

    def count(self):
        count = 0
        for model in self.models:
            count += model.objects.filter(project__isnull=True).count()
        return count
