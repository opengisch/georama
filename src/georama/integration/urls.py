from adrf import routers
from django.urls import include, path

from georama.integration.api.view_sets import (
    ManageCustomDatasourceViewSet,
    ManageDatasourceViewSet,
    ManageFieldViewSet,
    ManageProjectViewSet,
    ManageRasterDatasourceViewSet,
    ManageVectorDatasourceViewSet,
)

app_name = "integration"

management_router = routers.SimpleRouter()
management_router.register(r"projects", ManageProjectViewSet, basename="manager-project")
management_router.register(r"datasources", ManageDatasourceViewSet, basename="manager-datasource")
management_router.register(
    r"vector_datasources", ManageVectorDatasourceViewSet, basename="manager-vector"
)
management_router.register(
    r"vector_datasource_fields", ManageFieldViewSet, basename="manager-field"
)
management_router.register(
    r"raster_datasources", ManageRasterDatasourceViewSet, basename="manager-raster"
)
management_router.register(
    r"custom_datasources", ManageCustomDatasourceViewSet, basename="manager-custom"
)

urlpatterns = [
    path("manage/", include(management_router.urls)),
]
