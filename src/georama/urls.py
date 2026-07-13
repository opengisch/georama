"""
URL configuration for app project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
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

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("georama.core.urls")),
    path("integration/", include("georama.integration.urls")),
    path("features/", include("georama.features.urls")),
    path("maps/", include("georama.maps.urls")),
    path("webgis/", include("georama.webgis.urls")),
    path("accounts/", include("allauth.urls")),
]

if AppSettings.DEBUG:
    # in dev mode we directly serve static files so we don't need
    # to execute collectstatic everytime.
    urlpatterns += staticfiles_urlpatterns()
    urlpatterns += [path("silk/", include("silk.urls", namespace="silk"))]
