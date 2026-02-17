from django.urls import path

from georama.maps import views
from georama.maps.apps import central_app_label

app_name = central_app_label

urlpatterns = [
    path("/ows", views.OgcServer.as_view(), name="maps_ogc_entry"),
    path(
        "/",
        views.Index.as_view(),
        name="index",
    ),
    path(
        "/layer/add",
        views.Publish.as_view(),
        name="layer-source-list",
    ),
    path(
        "/layer/add/<str:dataset_type>/<str:dataset_id>",
        views.publish_dataset_as_wms,
        name="layer-source-add",
    ),
    path(
        "/layer/<str:pk>",
        views.MapDetailView.as_view(),
        name="layer-detail",
    ),
    path(
        "/layer/<str:pk>/update",
        views.MapUpdateView.as_view(),
        name="layer-update",
    ),
    path(
        "/layer/<str:pk>/delete",
        views.MapDeleteView.as_view(),
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
