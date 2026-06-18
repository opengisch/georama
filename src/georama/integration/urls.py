from django.urls import include, path

from georama.integration.api.routers import GeoramaIntegrationManageRouter
from georama.integration.api.view_sets import CollectionViewSet
from georama.integration.views.index import Index

app_name = "integration"

management_router = GeoramaIntegrationManageRouter()
management_router.register(r"collections", CollectionViewSet, basename="collection")

urlpatterns = [
    path("", Index.as_view()),
    path("manage/", include(management_router.urls)),
]
