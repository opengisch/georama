from django.urls import path

from georama.processes import views
from georama.processes.apps import central_app_label

app_name = central_app_label

urlpatterns = [
    path("/", views.Index.as_view(), name="index"),
    path("/execute_process", views.ExecuteProcess.as_view(), name="process-execute"),
    path("/dataset", views.PublishedAsDatasetListView.as_view(), name="dataset-list"),
    path(
        "/dataset/add/<str:dataset_type>/<str:dataset_id>",
        views.PublishDataset.as_view(),
        name="dataset-add",
    ),
    path(
        "/dataset/add/dataset",
        views.PublishDatasetListView.as_view(),
        name="dataset-add-list",
    ),
    path(
        "/dataset/<str:pk>",
        views.PublishedAsDatasetDetailView.as_view(),
        name="dataset-detail",
    ),
    path(
        "/dataset/<str:pk>/update",
        views.PublishedAsDatasetUpdateView.as_view(),
        name="dataset-update",
    ),
    path(
        "/dataset/<str:pk>/delete",
        views.PublishedAsDatasetDeleteView.as_view(),
        name="dataset-delete",
    ),
    path(
        "/dataset/<str:pk>/permission",
        views.PublishedAsDatasetPermissionView.as_view(),
        name="dataset-permission-list",
    ),
    path(
        "/dataset/<str:pk>/permission/user",
        views.PublishedAsDatasetUserListView.as_view(),
        name="dataset-permission-user-list",
    ),
    path(
        "/dataset/<str:pk>/permission/group",
        views.PublishedAsDatasetGroupListView.as_view(),
        name="dataset-permission-group-list",
    ),
    path("/process", views.PublishedAsProcessListView.as_view(), name="process-list"),
    path(
        "/process/add/process",
        views.PublishProcessListView.as_view(),
        name="process-add-list",
    ),
    path(
        "/process/add/<str:process_id>",
        views.PublishProcess.as_view(),
        name="process-add",
    ),
    path(
        "/process/<str:pk>",
        views.PublishedAsProcessDetailView.as_view(),
        name="process-detail",
    ),
    path(
        "/process/<str:pk>/update",
        views.PublishedAsProcessUpdateView.as_view(),
        name="process-update",
    ),
    path(
        "/process/<str:pk>/delete",
        views.PublishedAsProcessDeleteView.as_view(),
        name="process-delete",
    ),
    path(
        "/process/<str:pk>/permission",
        views.PublishedAsProcessPermissionView.as_view(),
        name="process-permission-list",
    ),
    path(
        "/process/<str:pk>/permission/user",
        views.PublishedAsProcessUserListView.as_view(),
        name="process-permission-user-list",
    ),
    path(
        "/process/<str:pk>/permission/group",
        views.PublishedAsProcessGroupListView.as_view(),
        name="process-permission-group-list",
    ),
]
