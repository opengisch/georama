from django.urls import include, path, re_path

from georama.core.common.routers import DefaultRouter, SimpleRouter
from georama.webgis.api.viewsets import ManageThemeViewSet, ThemeViewSet, UrlShortenerViewSet
from georama.webgis.views.ogc import OgcServerWebGis

app_name = "webgis"

management_router = SimpleRouter()
management_router.register(r"themes", ManageThemeViewSet, basename="theme-manager")

router = DefaultRouter()
router.register(r"themes", ThemeViewSet, basename="theme")

short_router = SimpleRouter()
short_router.register(r"short", UrlShortenerViewSet, basename="short")

urlpatterns = [
    path("", include(router.urls)),
    path("", include(short_router.urls)),
    path("manage/", include(management_router.urls)),
    re_path(r"ows/?$", OgcServerWebGis.as_view(), name="ows_entry"),
]
