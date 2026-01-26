from django.urls import path

from georama.features import views
from georama.features.apps import central_app_label

app_name = central_app_label

urlpatterns = [
    # path("/pygeoapi", include(views.PygeoapiServer.urls(), namespace=app_name)),
    path("/pygeoapi", views.PygeoapiServer.as_view(action="landing"), name="landing"),
    path(
        "/pygeoapi/conformance",
        views.PygeoapiServer.as_view(action="conformance"),
        name="conformance",
    ),
    path(
        "/pygeoapi/openapi",
        views.PygeoapiServer.as_view(action="openapi"),
        name="openapi",
    ),
    path(
        "/pygeoapi/collections",
        views.PygeoapiServer.as_view(action="collections"),
        name="collections",
    ),
    path(
        "/pygeoapi/collections/<str:collection_id>",
        views.PygeoapiServer.as_view(action="collections"),
        name="collection-detail",
    ),
    path(
        "/pygeoapi/collections/<str:collection_id>/schema",
        views.PygeoapiServer.as_view(action="collection_schema"),
        name="collection-schema",
    ),
    path(
        "/pygeoapi/collections/<str:collection_id>/queryables",
        views.PygeoapiServer.as_view(action="collection_queryables"),
        name="collection-queryables",
    ),
    path(
        "/pygeoapi/collections/<str:collection_id>/items",
        views.PygeoapiServer.as_view(action="collection_items"),
        name="collection-items",
    ),
    path(
        "/pygeoapi/collections/<str:collection_id>/items/<str:item_id>",
        views.PygeoapiServer.as_view(action="collection_item"),
        name="collection-item",
    ),
    path(
        "/publish_as/oapif/<str:vector_dataset_id>",
        views.admin_publish_as_oapif,
        name="publish_as_oapif",
    ),
    path(
        "/",
        views.Index.as_view(),
        name="index",
    ),
    path(
        "/publish",
        views.Publish.as_view(),
        name=views.Publish.name,
    ),
    path(
        "/ogcapi-f/form/<str:pk>",
        views.PublishedAsOgcApiFeaturesServiceFormView.as_view(),
        name=views.PublishedAsOgcApiFeaturesServiceFormView.name,
    ),
    path(
        "/ogcapi-f/form",
        views.PublishedAsOgcApiFeaturesServiceFormView.as_view(),
        name=views.PublishedAsOgcApiFeaturesServiceFormView.name,
    ),
]
