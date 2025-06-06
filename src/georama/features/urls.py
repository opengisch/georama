from django.urls import path

from georama.features import views

urlpatterns = [
    path("/", views.landing_page, name="landing"),
    path("/conformance", views.conformance, name="conformance"),
    path("/openapi", views.openapi, name="openapi"),
    path("/collections", views.collections, name="collections"),
    path(
        "/collections/<str:collection_id>",
        views.collections,
        name="collection-detail",
    ),
    path(
        "/collections/<str:collection_id>/schema",
        views.collection_schema,
        name="collection-schema",
    ),
    path(
        "/collections/<str:collection_id>/queryables",
        views.collection_queryables,
        name="collection-queryables",
    ),
    path(
        "/collections/<str:collection_id>/items",
        views.collection_items,
        name="collection-items",
    ),
    path(
        "/collections/<str:collection_id>/items/<str:item_id>",
        views.collection_item,
        name="collection-item",
    ),
    path(
        "/publish_as/oapif/<str:vector_dataset_id>",
        views.admin_publish_as_oapif,
        name="publish_as_oapif",
    ),
]
