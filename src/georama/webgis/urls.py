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

urlpatterns = [
    path("", views.home, name="home"),
    path("/themes.<str:format>", views.Themes.as_view(), name="themes"),
    path("/<str:folder_name>/", views.GeoGirafe.as_view(), name="geogirafe"),
    path("/<str:folder_name>/config.json", views.Config.as_view(), name="config"),
    path(
        "/publish_project/<int:project_id>",
        views.PublishProject.as_view(),
        name="publish_project",
    ),
    path("/maps", views.OgcServerWebgis.as_view(), name="webgis_ogc_entry"),
    path(
        "/publish_dataset_as/wms/<str:dataset_type>/<str:dataset_id>",
        views.admin_publish_dataset_as_wms,
        name="webgis_publish_dataset_as_wms",
    ),
    path(
        "/translations/de.json",
        views.translation_json,
        name="webis_translation_json",
    ),
]
