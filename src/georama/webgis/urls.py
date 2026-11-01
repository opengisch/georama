from adrf.routers import DefaultRouter, SimpleRouter
from django.urls import include, path, re_path
from django.utils.translation import gettext as _
from drf_spectacular import views


from georama.webgis.api.viewsets import ManageThemeViewSet, ThemeViewSet, UrlShortenerViewSet
from georama.webgis.views.ogc import OgcServerWebGis

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
    path(
        "manage/schema/",
        views.SpectacularAPIView.as_view(
            urlconf=management_router.urls,
            custom_settings={
                "TITLE": _("Management API of the WebGIS app."),
                "SCHEMA_PATH_PREFIX": "",
                "SCHEMA_PATH_PREFIX_INSERT": "webgis/manage",
            },
        ),
        name="schema",
    ),
    path(
        "manage/schema/swagger/",
        views.SpectacularSwaggerView.as_view(url_name="webgis:schema"),
        name="swagger",
    ),
    path(
        "manage/schema/redoc/",
        views.SpectacularRedocView.as_view(url_name="webgis:schema"),
        name="redoc",
    ),
    re_path(r"ows/?$", OgcServerWebGis.as_view(), name="ows_entry"),
]
