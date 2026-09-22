from adrf.routers import DefaultRouter, SimpleRouter
from django.urls import include, path

from georama.webgis.api.viewsets import ManageThemeViewSet, ThemeViewSet
from georama.webgis.views.ogc import OgcServerWebGis
from georama.webgis.views.url_shortener import UrlShortenerViewSet

app_name = "webgis"

management_router = SimpleRouter()
management_router.register(r"themes", ManageThemeViewSet, basename="theme-manager")

router = DefaultRouter()
router.register(r"themes", ThemeViewSet, basename="theme")

short_router = SimpleRouter(trailing_slash=False)
short_router.register(r"short", UrlShortenerViewSet, basename="short")

urlpatterns = [
    path("", include(router.urls)),
    path("", include(short_router.urls)),
    path("manage/", include(management_router.urls)),
    path("ows/", OgcServerWebGis.as_view(), name="ows_entry"),
]
