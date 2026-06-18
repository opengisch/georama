from django.urls import include, path

from georama.integration.api.routers import GeoramaIntegrationManageRouter
from georama.integration.api.view_sets import (
    CollectionViewSet,
    CustomDatasetViewSet,
    FieldViewSet,
    ProjectViewSet,
    RasterDatasetViewSet,
    VectorDatasetViewSet,
)
from georama.integration.views.index import Index

app_name = "integration"

management_router = GeoramaIntegrationManageRouter()
management_router.register(r"collections", CollectionViewSet, basename="collection")
management_router.register(r"projects", ProjectViewSet, basename="project")
management_router.register(r"vector_datasets", VectorDatasetViewSet, basename="vector")
management_router.register(r"vector_dataset_fields", FieldViewSet, basename="field")
management_router.register(r"raster_datasets", RasterDatasetViewSet, basename="raster")
management_router.register(r"custom_datasets", CustomDatasetViewSet, basename="custom")

urlpatterns = [
    path("", Index.as_view()),
    path("manage/", include(management_router.urls)),
]
