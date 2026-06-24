from django.urls import include, path

from georama.features.api.routers import GeoramaFeaturesManageRouter
from georama.features.api.viewsets import FeatureLayerViewSet
from georama.features.views.index import Index

app_name = "features"

management_router = GeoramaFeaturesManageRouter()
management_router.register(r"feature_layers", FeatureLayerViewSet, basename="featurelayer")


urlpatterns = [
    path("", Index.as_view()),
    path("manage/", include(management_router.urls)),
]
