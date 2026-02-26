from django.urls import path

from georama.features import views
from georama.features.apps import central_app_label

app_name = central_app_label

urlpatterns = [
    # path("/pygeoapi", include(views.PygeoapiServer.urls(), namespace=app_name)),
    path("/api", views.PygeoapiServer.as_view(action="landing"), name="api-landing"),
    path(
        "/api/conformance",
        views.PygeoapiServer.as_view(action="conformance"),
        name="api-conformance",
    ),
    path(
        "/api/openapi",
        views.PygeoapiServer.as_view(action="openapi"),
        name="api-openapi",
    ),
    path(
        "/api/collections",
        views.PygeoapiServer.as_view(action="collections"),
        name="api-collections",
    ),
    path(
        "/api/collections/<str:collection_id>",
        views.PygeoapiServer.as_view(action="collections"),
        name="api-collection-detail",
    ),
    path(
        "/api/collections/<str:collection_id>/schema",
        views.PygeoapiServer.as_view(action="collection_schema"),
        name="api-collection-schema",
    ),
    path(
        "/api/collections/<str:collection_id>/queryables",
        views.PygeoapiServer.as_view(action="collection_queryables"),
        name="api-collection-queryables",
    ),
    path(
        "/api/collections/<str:collection_id>/items",
        views.PygeoapiServer.as_view(action="collection_items"),
        name="api-collection-items",
    ),
    path(
        "/api/collections/<str:collection_id>/items/<str:item_id>",
        views.PygeoapiServer.as_view(action="collection_item"),
        name="api-collection-item",
    ),
    path(
        "",
        views.Index.as_view(),
        name="index",
    ),
    path(
        "/layer",
        views.LayerListView.as_view(),
        name="layer-list",
    ),
    path(
        "/layer/add",
        views.PublishListView.as_view(),
        name="layer-add-list",
    ),
    path(
        "/layer/add/<str:vector_dataset_id>",
        views.PublishLayer.as_view(),
        name="layer-add",
    ),
    path(
        "/layer/<str:pk>",
        views.FeatureDetailView.as_view(),
        name="layer-detail",
    ),
    path(
        "/layer/<str:pk>/update",
        views.FeatureUpdateView.as_view(),
        name="layer-update",
    ),
    path(
        "/layer/<str:pk>/delete",
        views.FeatureDeleteView.as_view(),
        name="layer-delete",
    ),
    path(
        "/layer/<str:pk>/permission",
        views.PermissionView.as_view(),
        name="layer-permission-list",
    ),
    path(
        "/layer/<str:pk>/permission/user",
        views.UserListView.as_view(),
        name="layer-permission-user-list",
    ),
    path(
        "/layer/<str:pk>/permission/group",
        views.GroupListView.as_view(),
        name="layer-permission-group-list",
    ),
]
