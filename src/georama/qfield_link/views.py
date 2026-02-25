from django.apps import apps
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.http import HttpRequest
from django.shortcuts import redirect
from django.views import View

from georama.core.menu import BreadCrumb
from georama.core.views.generic.list import GeoramaListView
from georama.core.views.generic.mixins import GeoramaLoginRequiredMixin
from georama.qfield_link.apps import central_app_label
from georama.qfield_link.services.qfield_cloud import ApiService


class ProjectDownloader(GeoramaLoginRequiredMixin, PermissionRequiredMixin, View):
    permission_required = f"{central_app_label}.can_use_app"

    def get(self, request: HttpRequest, qfield_cloud_project_id: str):
        qfc_api = ApiService()
        qfc_api.download_project(qfield_cloud_project_id)
        return redirect("data_integration:project-list")


class ProjectList(GeoramaLoginRequiredMixin, PermissionRequiredMixin, GeoramaListView):
    template_name = "qfield_link/index.html"
    permission_required = f"{central_app_label}.can_use_app"

    def get_queryset(self):
        qfc_api = ApiService()
        return qfc_api.get_project_list()

    def get_breadcrumbs(self):
        app_menu = apps.get_app_config(central_app_label).app_menu()
        return [
            BreadCrumb(app_menu.title),
        ]
