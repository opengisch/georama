from georama.core.services import Service
from georama.data_integration.models import CustomDataSet, RasterDataSet, VectorDataSet
from georama.maps.models import PublishedAsWms


class PublishedAsWmsService(Service):
    models = [PublishedAsWms]
    name = "maps"


class ProjectDatasetsService(Service):
    models = [VectorDataSet, RasterDataSet, CustomDataSet]
    name = "dataset"
