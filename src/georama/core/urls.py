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

from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

from georama.core import views
from georama.core.apps import central_app_label

app_name = central_app_label

urlpatterns = [
    path("i18n/", include("django.conf.urls.i18n")),
    path("", views.GeoramaLanding.as_view(), name="landing"),
    path("login", views.Login.as_view(), name="login"),
    path("logout", views.Logout.as_view(), name="logout"),
    path(
        "core/assign_permission_to_user_or_group",
        views.AssignPermissionToUserOrGroup.as_view(),
        name="assign_permission_to_user_or_group",
    ),
    path(
        "core/remove_permission_from_user_or_group",
        views.RemovePermissionToUserOrGroup.as_view(),
        name="remove_permission_from_user_or_group",
    ),
    path("settings", views.Settings.as_view(), name="settings"),
    path("features", include("georama.features.urls")),
    path("data_integration", include("georama.data_integration.urls")),
    path("maps", include("georama.maps.urls")),
    path("webgis", include("georama.webgis.urls")),
    path("qfield_link", include("georama.qfield_link.urls")),
    path("accounts/", include("allauth.urls")),
    path("admin/", admin.site.urls, {"extra_context": {"DEBUG": settings.DEBUG}}),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
