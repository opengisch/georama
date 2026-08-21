from adrf.routers import DefaultRouter, SimpleRouter
from django.urls import include, path

from georama.webgis.api.viewsets import ManageThemeViewSet, ThemeViewSet
from georama.webgis.views.ogc import OgcServerWebGis
from georama.webgis.views.url_shortener import UrlShortenerCreate, UrlShortenerRetrieve

app_name = "webgis"

management_router = SimpleRouter()
management_router.register(r"themes", ManageThemeViewSet, basename="theme-manager")

router = DefaultRouter()
router.register(r"themes", ThemeViewSet, basename="theme")

urlpatterns = [
    path("", include(router.urls)),
    path("manage/", include(management_router.urls)),
    path("ows/", OgcServerWebGis.as_view(), name="ows_entry"),
    path("/short/get/<str:id>", UrlShortenerRetrieve.as_view(), name="get_short_url"),
    path("/short/create", UrlShortenerCreate.as_view(), name="shorten_url"),
]
