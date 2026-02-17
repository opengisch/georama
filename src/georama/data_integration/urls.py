"""
URL configuration for core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path

from georama.data_integration import views
from georama.data_integration.apps import central_app_label

app_name = central_app_label

urlpatterns = [
    path(
        "/register_qgis_project/<str:folder_name>/<str:project_name>",
        views.RegisterQgisProject.as_view(),
        name="project-register",
    ),
    path(
        "/export_qgis_project/<str:folder_name>/<str:project_name>",
        views.QgisServerLightExporter.as_view(),
        name="project-export",
    ),
    path("/", views.Index.as_view(), name="index"),
    path(
        "/project",
        views.ChangeListProject.as_view(),
        name="project-list",
    ),
    path("/project/<str:pk>/delete", views.DeleteProject.as_view(), name="project-delete"),
    path(
        "/project/detail/<str:group_name>/<str:project_name>",
        views.ProjectDetail.as_view(),
        name="project-detail",
    ),
    path(
        "/manual_dataset/changelist",
        views.ChangeListManualDataset.as_view(),
        name=views.ChangeListManualDataset.name,
    ),
]
