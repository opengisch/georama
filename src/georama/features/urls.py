from django.urls import include, path

from georama.features.api.routers import GeoramaFeaturesManageRouter
from georama.features.api.viewsets import FeatureLayerViewSet, FieldViewSet
from georama.features.views.index import Index

app_name = "features"

management_router = GeoramaFeaturesManageRouter()
management_router.register(r"feature_layer", FeatureLayerViewSet, basename="feature_layer")
management_router.register(
    r"feature_layer/(?P<feature_layer_id>[^/.]+)/fields",
    FieldViewSet,
    basename="feature_layer_fields",
)

urlpatterns = [
    path("", Index.as_view()),
    path("manage/", include(management_router.urls)),
]
