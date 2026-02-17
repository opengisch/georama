from georama.core.services.multi_model.base import Service
from georama.data_integration.models import CustomDataSet, RasterDataSet, VectorDataSet


class DatasetService(Service):
    models = [VectorDataSet, RasterDataSet, CustomDataSet]
    name = "dataset"
