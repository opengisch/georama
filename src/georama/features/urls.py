from django.urls import include, path
from rest_framework.routers import SimpleRouter

from georama.features.api.viewsets import FeatureLayerViewSet
from georama.features.views.pygeoapi import PygeoapiServer

app_name = "features"

management_router = SimpleRouter()
management_router.register(r"feature_layers", FeatureLayerViewSet, basename="featurelayer")

urlpatterns = [
    path("manage/", include(management_router.urls)),
    path("", PygeoapiServer.as_view(action="landing"), name="landing"),
    path(
        "conformance",
        PygeoapiServer.as_view(action="conformance"),
        name="api-conformance",
    ),
    path(
        "openapi",
        PygeoapiServer.as_view(action="openapi"),
        name="api-openapi",
    ),
    path(
        "collections",
        PygeoapiServer.as_view(action="collections"),
        name="api-collections",
    ),
    path(
        "collections/<str:collection_id>",
        PygeoapiServer.as_view(action="collections"),
        name="api-collection-detail",
    ),
    path(
        "collections/<str:collection_id>/schema",
        PygeoapiServer.as_view(action="collection_schema"),
        name="api-collection-schema",
    ),
    path(
        "collections/<str:collection_id>/queryables",
        PygeoapiServer.as_view(action="collection_queryables"),
        name="api-collection-queryables",
    ),
    path(
        "collections/<str:collection_id>/items",
        PygeoapiServer.as_view(action="collection_items"),
        name="api-collection-items",
    ),
    path(
        "collections/<str:collection_id>/items/<str:item_id>",
        PygeoapiServer.as_view(action="collection_item"),
        name="api-collection-item",
    ),
]
