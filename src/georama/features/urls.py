from adrf import routers
from adrf.routers import DefaultRouter
from django.urls import include, path
from django.utils.translation import gettext as _
from drf_spectacular import views

from georama.features.api.viewsets import FeatureLayerViewSet, ManageFeatureLayerViewSet
from georama.features.views.pygeoapi import PygeoapiServer

app_name = "features"

management_router = routers.SimpleRouter()
management_router.register(r"feature_layers", ManageFeatureLayerViewSet, basename="feature-manager")

router = DefaultRouter()
router.register(r"feature_layers", FeatureLayerViewSet, basename="feature")

urlpatterns = [
    path("", include(router.urls)),
    path("manage/", include(management_router.urls)),
    path(
        "manage/schema/",
        views.SpectacularAPIView.as_view(
            urlconf=management_router.urls,
            custom_settings={
                "TITLE": _("Management API of the Features app."),
                "SCHEMA_PATH_PREFIX": "",
                "SCHEMA_PATH_PREFIX_INSERT": "features/manage",
            },
        ),
        name="schema",
    ),
    path(
        "manage/schema/swagger/",
        views.SpectacularSwaggerView.as_view(url_name="features:schema"),
        name="swagger",
    ),
    path(
        "manage/schema/redoc/",
        views.SpectacularRedocView.as_view(url_name="features:schema"),
        name="redoc",
    ),
    path("api", PygeoapiServer.as_view(action="landing"), name="landing"),
    path(
        "api/conformance",
        PygeoapiServer.as_view(action="conformance"),
        name="api-conformance",
    ),
    path(
        "api/openapi",
        PygeoapiServer.as_view(action="openapi"),
        name="api-openapi",
    ),
    path(
        "api/collections",
        PygeoapiServer.as_view(action="collections"),
        name="api-collections",
    ),
    path(
        "api/collections/<str:collection_id>",
        PygeoapiServer.as_view(action="collections"),
        name="api-collection-detail",
    ),
    path(
        "api/collections/<str:collection_id>/schema",
        PygeoapiServer.as_view(action="collection_schema"),
        name="api-collection-schema",
    ),
    path(
        "api/collections/<str:collection_id>/queryables",
        PygeoapiServer.as_view(action="collection_queryables"),
        name="api-collection-queryables",
    ),
    path(
        "api/collections/<str:collection_id>/items",
        PygeoapiServer.as_view(action="collection_items"),
        name="api-collection-items",
    ),
    path(
        "api/collections/<str:collection_id>/items/<str:item_id>",
        PygeoapiServer.as_view(action="collection_item"),
        name="api-collection-item",
    ),
]
