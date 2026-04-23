from django.urls import path

from georama.process import views
from georama.process.apps import central_app_label

app_name = central_app_label

urlpatterns = [
    path("/", views.Index.as_view(), name="index"),
    path("/execute_process", views.Process.as_view(), name="process-execute"),
    path("/dataset", views.PublishedAsDatasetListView.as_view(), name="dataset-list"),
    path(
        "/dataset/add/dataset/<str:pk>",
        views.PublishDatasetListView.as_view(),
        name="dataset-add",
    ),
    path(
        "/dataset/add/dataset",
        views.PublishedAsDatasetListView.as_view(),
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
]
