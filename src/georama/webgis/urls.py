from adrf.routers import DefaultRouter, SimpleRouter
from django.urls import include, path

from georama.webgis.api.viewsets import ManageThemeViewSet, ThemeViewSet, UrlShortenerViewSet
from georama.webgis.views.ogc import OgcServerWebGis
from georama.webgis.views.pygeoapi import PygeoapiServerWebGIS

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
    path("api", PygeoapiServerWebGIS.as_view(action="landing"), name="landing"),
    path(
        "api/conformance",
        PygeoapiServerWebGIS.as_view(action="conformance"),
        name="api-conformance",
    ),
    path(
        "api/openapi",
        PygeoapiServerWebGIS.as_view(action="openapi"),
        name="api-openapi",
    ),
    path(
        "api/collections",
        PygeoapiServerWebGIS.as_view(action="collections"),
        name="api-collections",
    ),
    path(
        "api/collections/<str:collection_id>",
        PygeoapiServerWebGIS.as_view(action="collections"),
        name="api-collection-detail",
    ),
    path(
        "api/collections/<str:collection_id>/schema",
        PygeoapiServerWebGIS.as_view(action="collection_schema"),
        name="api-collection-schema",
    ),
    path(
        "api/collections/<str:collection_id>/queryables",
        PygeoapiServerWebGIS.as_view(action="collection_queryables"),
        name="api-collection-queryables",
    ),
    path(
        "api/collections/<str:collection_id>/items",
        PygeoapiServerWebGIS.as_view(action="collection_items"),
        name="api-collection-items",
    ),
    path(
        "api/collections/<str:collection_id>/items/<str:item_id>",
        PygeoapiServerWebGIS.as_view(action="collection_item"),
        name="api-collection-item",
    ),
]
