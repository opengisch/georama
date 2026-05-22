from django.shortcuts import redirect
from django.urls import path

from georama.processes.apps import central_app_label
from georama.processes.views import api, management

app_name = central_app_label

urlpatterns = [
    # TODO: remove this
    path("/execute_process", management.ExecuteProcess.as_view(), name="process-execute"),
    path("/dataset", management.PublishedAsDatasetListView.as_view(), name="dataset-list"),
    path(
        "/dataset/add/<str:dataset_type>/<str:dataset_id>",
        management.PublishDataset.as_view(),
        name="dataset-add",
    ),
    path(
        "/dataset/add/dataset",
        management.PublishDatasetListView.as_view(),
        name="dataset-add-list",
    ),
    path(
        "/dataset/<str:pk>",
        management.PublishedAsDatasetDetailView.as_view(),
        name="dataset-detail",
    ),
    path(
        "/dataset/<str:pk>/update",
        management.PublishedAsDatasetUpdateView.as_view(),
        name="dataset-update",
    ),
    path(
        "/dataset/<str:pk>/delete",
        management.PublishedAsDatasetDeleteView.as_view(),
        name="dataset-delete",
    ),
    path(
        "/dataset/<str:pk>/permission",
        management.PublishedAsDatasetPermissionView.as_view(),
        name="dataset-permission-list",
    ),
    path(
        "/dataset/<str:pk>/permission/user",
        management.PublishedAsDatasetUserListView.as_view(),
        name="dataset-permission-user-list",
    ),
    path(
        "/dataset/<str:pk>/permission/group",
        management.PublishedAsDatasetGroupListView.as_view(),
        name="dataset-permission-group-list",
    ),
    path("/process", management.PublishedAsProcessListView.as_view(), name="process-list"),
    path(
        "/process/add/process",
        management.PublishProcessListView.as_view(),
        name="process-add-list",
    ),
    path(
        "/process/add/<str:process_id>",
        management.PublishProcess.as_view(),
        name="process-add",
    ),
    path(
        "/process/<str:pk>",
        management.PublishedAsProcessDetailView.as_view(),
        name="process-detail",
    ),
    path(
        "/process/<str:pk>/update",
        management.PublishedAsProcessUpdateView.as_view(),
        name="process-update",
    ),
    path(
        "/process/<str:pk>/delete",
        management.PublishedAsProcessDeleteView.as_view(),
        name="process-delete",
    ),
    path(
        "/process/<str:pk>/permission",
        management.PublishedAsProcessPermissionView.as_view(),
        name="process-permission-list",
    ),
    path(
        "/process/<str:pk>/permission/user",
        management.PublishedAsProcessUserListView.as_view(),
        name="process-permission-user-list",
    ),
    path(
        "/process/<str:pk>/permission/group",
        management.PublishedAsProcessGroupListView.as_view(),
        name="process-permission-group-list",
    ),
    path("/", lambda _: redirect("processes:api-landing"), name="index"),
    path("/api", api.LandingView.as_view(), name="api-landing"),
    path("/api/conformance", api.ConformanceView.as_view(), name="api-conformance"),
    path("/api/processes", api.ProcessListView.as_view(), name="api-process-list"),
    path(
        "/api/processes/<process_id>",
        api.ProcessDetailView.as_view(),
        name="api-process-detail",
    ),
    path(
        "/api/processes/<process_id>/execution",
        api.ProcessExectionView.as_view(),
        name="api-process-execution",
    ),
    path("/api/jobs", api.JobListView.as_view(), name="api-job-list"),
    path("/api/jobs/<job_id>", api.JobDetailView.as_view(), name="api-job-detail"),
    path("/api/jobs/<job_id>/results", api.JobResultView.as_view(), name="api-job-results"),
]
