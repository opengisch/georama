from django.apps import apps
from django.http import HttpRequest
from django.shortcuts import redirect
from django.views import View

from georama.core.menu import BreadCrumb
from georama.core.views.generic.list import GeoramaListView
from georama.qfield_link.apps import central_app_label
from georama.qfield_link.services.qfield_cloud import ApiService


class ProjectDownloader(View):

    def get(self, request: HttpRequest, qfield_cloud_project_id: str):
        qfc_api = ApiService()
        qfc_api.download_project(qfield_cloud_project_id)
        return redirect("data_integration:project-list")


class ProjectList(GeoramaListView):
    template_name = "qfield_link/index.html"

    def get_queryset(self):
        qfc_api = ApiService()
        return qfc_api.get_project_list()

    def get_breadcrumbs(self):
        app_menu = apps.get_app_config(central_app_label).app_menu()
        return [
            BreadCrumb(app_menu.title),
        ]
