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
    path("/clone-geoportal", views.RegisterThemesJson.as_view(), name="clone_geoportal"),
    path("/<str:mandant_name>/themes.<str:format>", views.Themes.as_view(), name="themes"),
    path("/<str:mandant_name>/", views.GeoGirafe.as_view(), name="geogirafe"),
    path("/<str:mandant_name>/config.json", views.Config.as_view(), name="config"),
    path(
        "/publish_project/<int:mandant_id>/<str:project_name>",
        views.PublishProject.as_view(),
        name="publish_project",
    ),
]
