from adrf import routers
from django.urls import include, path
from django.utils.translation import gettext as _
from drf_spectacular import views

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
    path(
        "manage/schema/",
        views.SpectacularAPIView.as_view(
            urlconf=management_router.urls,
            custom_settings={
                "TITLE": _("Management API of the Maps app."),
                "SCHEMA_PATH_PREFIX": "",
                "SCHEMA_PATH_PREFIX_INSERT": "maps/manage",
            },
        ),
        name="schema",
    ),
    path(
        "manage/schema/swagger/",
        views.SpectacularSwaggerView.as_view(url_name="maps:schema"),
        name="swagger",
    ),
    path(
        "manage/schema/redoc/",
        views.SpectacularRedocView.as_view(url_name="maps:schema"),
        name="redoc",
    ),
    path("ows", OgcServer.as_view(), name="maps_ogc_entry"),
]
