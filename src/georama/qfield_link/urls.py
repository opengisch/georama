from django.urls import path

from georama.qfield_link import views

app_name = "georama.qfield_link"

urlpatterns = [
    path("", views.LinkProjects.as_view(), name="link_projects"),
    path(
        "download_qfield_cloud_project/<str:qfield_cloud_project_id>",
        views.QfieldCloudDownloader.as_view(),
        name="download_qfield_cloud_project",
    ),
]
