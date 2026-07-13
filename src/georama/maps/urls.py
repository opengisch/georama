from adrf import routers
from django.urls import include, path

from georama.maps.api.viewsets import ManageWmsLayerViewSet, WmsLayerViewSet
from georama.maps.views.ogc import OgcServer

app_name = "maps"

management_router = routers.SimpleRouter()
management_router.register(r"map_layers", ManageWmsLayerViewSet, basename="maplayer-manager")

router = routers.SimpleRouter()
router.register(r"map_layers", WmsLayerViewSet, basename="maplayer")

urlpatterns = [
    path("", include(router.urls)),
    path("manage/", include(management_router.urls)),
    path("ows", OgcServer.as_view(), name="maps_ogc_entry"),
]
