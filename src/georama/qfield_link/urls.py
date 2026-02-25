from django.urls import path

from georama.qfield_link import views
from georama.qfield_link.apps import central_app_label

app_name = central_app_label

urlpatterns = [
    path(
        "/project/<str:qfield_cloud_project_id>/download",
        views.ProjectDownloader.as_view(),
        name="project-download",
    ),
    path(
        "/project",
        views.ProjectList.as_view(),
        name="index",
    ),
]
