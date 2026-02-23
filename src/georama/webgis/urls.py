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

from georama.webgis import views
from georama.webgis.apps import central_app_label

app_name = central_app_label

urlpatterns = [
    path("", views.Index.as_view(), name="index"),
    path("/theme", views.ThemesListView.as_view(), name="theme-list"),
    path(
        "/theme/add/project/<str:pk>",
        views.PublishThemeFromProject.as_view(),
        name="theme-add",
    ),
    path(
        "/theme/add/project",
        views.PublishProjectListView.as_view(),
        name="theme-add-list",
    ),
    path(
        "/theme/<str:pk>",
        views.ThemeDetailView.as_view(),
        name="theme-detail",
    ),
    path(
        "/theme/<str:pk>/update",
        views.ThemeUpdateView.as_view(),
        name="theme-update",
    ),
    path(
        "/theme/<str:pk>/delete",
        views.ThemeDeleteView.as_view(),
        name="theme-delete",
    ),
    path(
        "/theme/<str:pk>/permission",
        views.PermissionView.as_view(),
        name="theme-permission-list",
    ),
    path(
        "/theme/<str:pk>/permission/user",
        views.UserListView.as_view(),
        name="theme-permission-user-list",
    ),
    path(
        "/theme/<str:pk>/permission/group",
        views.GroupListView.as_view(),
        name="theme-permission-group-list",
    ),
    path("/themes.<str:format>", views.Themes.as_view(), name="themes"),
    path("/<str:folder_name>/", views.GeoGirafe.as_view(), name="geogirafe"),
    path("/<str:folder_name>/config.json", views.Config.as_view(), name="config"),
    path("/maps", views.OgcServerWebgis.as_view(), name="ogc_entry"),
    path(
        "/publish_dataset_as/wms/<str:dataset_type>/<str:dataset_id>",
        views.admin_publish_dataset_as_wms,
        name="publish_dataset_as_wms",
    ),
    path(
        "/translations/de.json",
        views.translation_json,
        name="translation_json",
    ),
]
