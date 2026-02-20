import logging

from django.apps import apps
from django.contrib.admin.utils import NestedObjects
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.db import router, transaction
from django.http import HttpRequest, HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse, reverse_lazy
from django.utils.http import url_has_allowed_host_and_scheme
from django.views import View

from georama.core.menu import BreadCrumb
from georama.core.views.generic.mixins import (
    GeoramaAnyPermissionRequiredMixin,
    GeoramaLoginRequiredMixin,
)
from georama.core.views.multi_model.list import ChangeListView
from georama.data_integration.apps import central_app_label
from georama.data_integration.models import Project
from georama.data_integration.services.project import DBService, FSService
from georama.data_integration.services.qgis_server_light import ExporterService

log = logging.getLogger(__name__)


class RegisterQgisProject(GeoramaLoginRequiredMixin, GeoramaAnyPermissionRequiredMixin, View):
    permission_required = [
        Project.perm_change(),
        Project.perm_add(),
    ]

    @transaction.atomic
    def get(self, request: HttpRequest, folder_name: str, project_name: str, **kwargs):
        project = FSService().get(folder_name, project_name)
        if not project.has_config or not project:
            redirect(f"{central_app_label}:project-list")
        DBService().integrate_project(project, project.config, folder_name)

        next_url = request.GET.get("next")
        if next_url and url_has_allowed_host_and_scheme(
            next_url,
            allowed_hosts={request.get_host()},
        ):
            return redirect(next_url)
        return redirect(f"{central_app_label}:project-list")


class QgisServerLightExporter(
    GeoramaLoginRequiredMixin, GeoramaAnyPermissionRequiredMixin, View
):
    permission_required = [
        Project.perm_change(),
        Project.perm_add(),
    ]

    def get(self, request: HttpRequest, folder_name: str, project_name: str, **kwargs):
        try:
            ExporterService().execute_export(folder_name, project_name)
        except RuntimeError as e:
            logging.error(e)
            return HttpResponse("Ask the administer", status=500)
        next_url = request.GET.get("next")
        if next_url and url_has_allowed_host_and_scheme(
            next_url,
            allowed_hosts={request.get_host()},
        ):
            return redirect(
                f'{reverse("data_integration:project-register", kwargs={"folder_name": folder_name, "project_name":project_name})}?next={next_url}'  # noqa E501
            )
        return redirect("data_integration:project-register", folder_name, project_name)


class Index(GeoramaLoginRequiredMixin, GeoramaAnyPermissionRequiredMixin, View):
    permission_required = [
        Project.perm_view(),
        Project.perm_change(),
        Project.perm_add(),
        Project.perm_delete(),
    ]

    def get(self, request: HttpRequest):
        fss_project = FSService()
        dbs_project = DBService()
        app_menu = apps.get_app_config("data_integration").app_menu()
        context = {
            "app_menu": app_menu,
            "project_count": fss_project.count(),
            "project_db_count": dbs_project.count_db_projects(),
            "outdated_count": fss_project.count_out_dated(),
            "breadcrumbs": [BreadCrumb(app_menu.title)],
        }
        return render(request, "data_integration/index.html", context)


class ChangeListProject(
    GeoramaLoginRequiredMixin, GeoramaAnyPermissionRequiredMixin, ChangeListView
):
    service = FSService
    title = "Projects"
    name = "project-list"
    app_menu = apps.get_app_config("data_integration").app_menu()
    template = "data_integration/project/change_list.html"
    breadcrumbs = [
        BreadCrumb(app_menu.title, reverse_lazy(f"{app_menu.app_label}:index")),
        BreadCrumb(title),
    ]
    permission_required = [
        Project.perm_view(),
        Project.perm_change(),
        Project.perm_add(),
        Project.perm_delete(),
    ]


class DeleteProject(GeoramaLoginRequiredMixin, PermissionRequiredMixin, View):
    service = FSService
    permission_required = Project.perm_delete()

    def get(self, request, pk):
        service = self.service()
        obj = get_object_or_404(Project, pk=pk)
        qgis_project = service.get(obj.mandant.name, obj.name)
        app_menu = apps.get_app_config("data_integration").app_menu()
        using = router.db_for_write(obj.__class__)
        collector = NestedObjects(using=using)

        collector.collect([obj])

        context = {
            "object": obj,
            "related_objects": collector.nested(),
            "protected": collector.protected,
            "breadcrumbs": [
                BreadCrumb(app_menu.title, reverse(f"{app_menu.app_label}:index")),
                BreadCrumb(
                    ChangeListProject.title,
                    reverse(f"{app_menu.app_label}:{ChangeListProject.name}"),
                ),
                BreadCrumb(
                    f"{qgis_project.parent.name}/{qgis_project.name}.{qgis_project.suffix}"
                ),
            ],
        }

        return render(request, "core/delete_preview.html", context)

    def post(self, request, pk):
        Project.objects.filter(pk=pk).delete()
        return redirect("data_integration:project-list")


class ProjectDetail(GeoramaLoginRequiredMixin, PermissionRequiredMixin, View):
    permission_required = Project.perm_view()

    def get(self, request: HttpRequest, group_name, project_name):
        fss_project = FSService()
        qgis_project = fss_project.get(group_name, project_name)
        app_menu = apps.get_app_config("data_integration").app_menu()
        datasets = None
        if qgis_project.has_config:
            datasets = (
                qgis_project.config.datasets.vector
                + qgis_project.config.datasets.raster
                + qgis_project.config.datasets.custom
            )
        return render(
            request,
            "data_integration/project/detail.html",
            {
                "app_menu": app_menu,
                "change_list_page_title": "Project",
                "change_list_view_name": f"{app_menu.app_label}:{ChangeListProject.name}",
                "instance_title": qgis_project.name,
                "qgis_project": qgis_project,
                "qgis_project_config": qgis_project.config,
                "qgis_project_layers": datasets,
                "breadcrumbs": [
                    BreadCrumb(app_menu.title, reverse(f"{app_menu.app_label}:index")),
                    BreadCrumb(
                        ChangeListProject.title,
                        reverse(f"{app_menu.app_label}:{ChangeListProject.name}"),
                    ),
                    BreadCrumb(
                        f"{qgis_project.project_path_as_string}",
                    ),
                ],
            },
        )
