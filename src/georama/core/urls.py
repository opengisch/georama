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

from django.conf import settings as AppSettings
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import include, path

from georama.core.apps import central_app_label
from georama.core.views import auth, landing, settings
from georama.core.views.entities import permission_assign, permission_remove

app_name = central_app_label

urlpatterns = [
    path("i18n/", include("django.conf.urls.i18n")),
    path("", landing.GeoramaLanding.as_view(), name="landing"),
    path("login", auth.Login.as_view(), name="login"),
    path("logout", auth.Logout.as_view(), name="logout"),
    path("settings", settings.Settings.as_view(), name="settings"),
    path(
        "core/assign_permission_to_user_or_group",
        permission_assign.GeoramaAssignPermissionToUserOrGroup.as_view(),
        name="assign_permission_to_user_or_group",
    ),
    path(
        "core/remove_permission_from_user_or_group",
        permission_remove.GeoramaRemovePermissionToUserOrGroup.as_view(),
        name="remove_permission_from_user_or_group",
    ),
    path("features", include("georama.features.urls")),
    path("process", include("georama.process.urls")),
    path("data_integration", include("georama.data_integration.urls")),
    path("maps", include("georama.maps.urls")),
    path("webgis", include("georama.webgis.urls")),
    path("qfield_link", include("georama.qfield_link.urls")),
    path("accounts/", include("allauth.urls")),
    path("admin/", admin.site.urls),
]

if AppSettings.DEBUG:
    # in dev mode we directly serve static files so we don't need
    # to execute collectstatic everytime.
    urlpatterns += staticfiles_urlpatterns()
