from django.urls import path

from georama.processes.apps import central_app_label
from georama.processes.views import api, gui

app_name = central_app_label

urlpatterns = [
    path("", gui.Index.as_view(), name="index"),
    path("/execute_process", gui.ExecuteProcess.as_view(), name="process-execute"),
    path("/dataset", gui.PublishedAsDatasetListView.as_view(), name="dataset-list"),
    path(
        "/dataset/add/<str:dataset_type>/<str:dataset_id>",
        gui.PublishDataset.as_view(),
        name="dataset-add",
    ),
    path(
        "/dataset/add/dataset",
        gui.PublishDatasetListView.as_view(),
        name="dataset-add-list",
    ),
    path(
        "/dataset/<str:pk>",
        gui.PublishedAsDatasetDetailView.as_view(),
        name="dataset-detail",
    ),
    path(
        "/dataset/<str:pk>/update",
        gui.PublishedAsDatasetUpdateView.as_view(),
        name="dataset-update",
    ),
    path(
        "/dataset/<str:pk>/delete",
        gui.PublishedAsDatasetDeleteView.as_view(),
        name="dataset-delete",
    ),
    path(
        "/dataset/<str:pk>/permission",
        gui.PublishedAsDatasetPermissionView.as_view(),
        name="dataset-permission-list",
    ),
    path(
        "/dataset/<str:pk>/permission/user",
        gui.PublishedAsDatasetUserListView.as_view(),
        name="dataset-permission-user-list",
    ),
    path(
        "/dataset/<str:pk>/permission/group",
        gui.PublishedAsDatasetGroupListView.as_view(),
        name="dataset-permission-group-list",
    ),
    path("/process", gui.PublishedAsProcessListView.as_view(), name="process-list"),
    path(
        "/process/add/process",
        gui.PublishProcessListView.as_view(),
        name="process-add-list",
    ),
    path(
        "/process/add/<str:process_id>",
        gui.PublishProcess.as_view(),
        name="process-add",
    ),
    path(
        "/process/<str:pk>",
        gui.PublishedAsProcessDetailView.as_view(),
        name="process-detail",
    ),
    path(
        "/process/<str:pk>/update",
        gui.PublishedAsProcessUpdateView.as_view(),
        name="process-update",
    ),
    path(
        "/process/<str:pk>/delete",
        gui.PublishedAsProcessDeleteView.as_view(),
        name="process-delete",
    ),
    path(
        "/process/<str:pk>/permission",
        gui.PublishedAsProcessPermissionView.as_view(),
        name="process-permission-list",
    ),
    path(
        "/process/<str:pk>/permission/user",
        gui.PublishedAsProcessUserListView.as_view(),
        name="process-permission-user-list",
    ),
    path(
        "/process/<str:pk>/permission/group",
        gui.PublishedAsProcessGroupListView.as_view(),
        name="process-permission-group-list",
    ),
    path("/api", api.OgcApiProcesses100.as_view(action="landing"), name="api-landing"),
]
