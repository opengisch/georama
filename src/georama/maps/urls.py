from django.urls import include, path
from rest_framework.routers import SimpleRouter

from georama.maps.api.viewsets import WmsLayerViewSet
from georama.maps.views.ogc import OgcServer

app_name = "maps"

management_router = SimpleRouter()
management_router.register(r"feature_layers", WmsLayerViewSet, basename="wmslayer")

urlpatterns = [
    path("manage/", include(management_router.urls)),
    path("ows", OgcServer.as_view(), name="maps_ogc_entry"),
]
