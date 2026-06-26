from django.urls import include, path
from rest_framework.routers import SimpleRouter

from georama.features.api.viewsets import FeatureLayerViewSet
from georama.features.views.index import Index

app_name = "features"

management_router = SimpleRouter()
management_router.register(r"feature_layers", FeatureLayerViewSet, basename="featurelayer")

urlpatterns = [
    path("", Index.as_view()),
    path("manage/", include(management_router.urls)),
]
