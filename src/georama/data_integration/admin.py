import hashlib
import os
from dataclasses import dataclass, field
from pathlib import Path
from typing import Type

from django.contrib import admin

from django.http import HttpRequest
from django.template.response import TemplateResponse
from django.urls import path
from django.utils.safestring import mark_safe
from django.utils.translation import gettext_lazy as _

from georama.data_integration.apps import DataintegrationConfig
from georama.data_integration.data_integration_config import Config
from georama.data_integration.models import (
    CustomDataSet,
    Mandant,
    Project,
    RasterDataSet,
    VectorDataSet,
)


class DataSetList:
    query_classes = [VectorDataSet, RasterDataSet, CustomDataSet]

    def query_dataset(
        self, query_class: Type[VectorDataSet] | Type[RasterDataSet] | Type[CustomDataSet]
    ):
        query = query_class.objects
        return query

    def get(
        self, project_pk: int | None = None
    ) -> list[VectorDataSet | RasterDataSet | CustomDataSet]:
        datasets = []
        for query_class in self.query_classes:
            query = self.query_dataset(query_class)
            if project_pk is None:
                query = query.filter(project__isnull=True)
            else:
                query = query.filter(
                    **{
                        query_class._meta.get_field("project").name: Project.objects.get(
                            pk=project_pk
                        )
                    }
                )
            datasets = datasets + list(query.all())
        return datasets


@dataclass
class QgisProject:
    parent: "QgisProjectGroup"
    name: str
    suffix: str

    @property
    def qualified_config_name(self) -> str:
        return f"{self.name}.json"

    @property
    def qualified_project_name(self) -> str:
        return f"{self.name}{self.suffix}"

    @property
    def config_path(self) -> str:
        return os.path.join(
            self.parent.parent.path, self.parent.name, self.qualified_config_name
        )

    @property
    def project_path(self) -> str:
        return os.path.join(
            self.parent.parent.path, self.parent.name, self.qualified_project_name
        )

    @property
    def has_config(self) -> bool:
        return os.path.isfile(self.config_path)

    @property
    def hash(self) -> str:
        if self.has_config:
            with open(self.config_path, mode="rb") as cf:
                return hashlib.md5(cf.read()).hexdigest()
        return ""


@dataclass
class QgisProjectGroup:
    parent: "QgisProjectFileStructure"
    name: str
    projects: list[QgisProject] = field(default_factory=list)

    @property
    def project_paths(self) -> list[str]:
        return [project.project_path for project in self.projects]

    @property
    def config_paths(self) -> list[str]:
        return [project.config_path for project in self.projects]

    @property
    def path(self) -> str:
        return os.path.join(self.parent.path, self.name)

    def is_file(self, name) -> bool:
        return os.path.isfile(os.path.join(self.path, name))

    def create_projects(self, allowed_extensions: list[str]):
        for name in os.listdir(self.path):
            if self.is_file(name):
                project_file_name = Path(name).stem
                project_file_suffix = name.replace(project_file_name, "")
                if project_file_suffix in allowed_extensions:
                    project = QgisProject(
                        parent=self, name=project_file_name, suffix=project_file_suffix
                    )
                    self.projects.append(project)

    def find_project_by_name(self, name) -> QgisProject | None:
        for project in self.projects:
            if project.name == name:
                return project
        return None


@dataclass
class QgisProjectFileStructure:
    path: str
    groups: list[QgisProjectGroup] = field(default_factory=list)

    def is_dir(self, name) -> bool:
        return os.path.isdir(os.path.join(self.path, name))

    def dirs(self) -> list[str]:
        dirs = []
        for name in os.listdir(self.path):
            dir_path = os.path.join(self.path, name)
            if os.path.isdir(dir_path):
                dirs.append(name)
            else:
                pass
        return dirs

    def create_groups(self, allowed_extensions: list[str]):
        for name in self.dirs():
            group = QgisProjectGroup(parent=self, name=name)
            group.create_projects(allowed_extensions=allowed_extensions)
            self.groups.append(group)

    def find_group_by_name(self, name) -> QgisProjectGroup | None:
        for group in self.groups:
            if group.name == name:
                return group
        return None


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    add_form_template = "admin/data_integration/project/qgis_projects.html"

    exclude = ["name", "title"]

    readonly_fields = [
        "mandant",
        "version",
        "hash",
        "modification_date",
        "integration_date",
    ]

    extra_actions = ["dataset_list"]

    def has_change_permission(self, request, obj=None):
        # Deactivate change action, projects can only be changed by integrating a QGIS project
        return False

    def add_view(self, request, form_url="", extra_context=None):
        config = Config()
        qgis_project_file_structure = QgisProjectFileStructure(os.path.join(config.path))
        qgis_project_file_structure.create_groups(config.qgis_project_extensions)

        extra_context = extra_context or {}
        extra_context.update(
            dict(
                # Include common variables for rendering the admin template.
                self.admin_site.each_context(request),
                # Anything else you want in the context...
                qgis_project_file_structure=qgis_project_file_structure,
                model_name=self.model._meta.verbose_name_plural,
                app_label=DataintegrationConfig.get_simple_appname(),
                app_verbose_name=DataintegrationConfig.verbose_name,
            )
        )
        return super().add_view(
            request,
            form_url,
            extra_context=extra_context,
        )

    def get_urls(self):
        urls = super().get_urls()
        my_urls = [
            path(
                "dataset_list/<str:project_pk>",
                self.admin_site.admin_view(self.dataset_list),
                name="data_integration_dataset_list",
            ),
        ]
        return my_urls + urls

    def dataset_list(
        self, request: HttpRequest, project_pk: int | None = None, extra_context=None, **kwargs
    ):
        ds = DataSetList()
        page_title = _("Manual datasets")

        if project_pk:
            page_title = _(
                "Datasets in Project «{project}»".format(
                    project=Project.objects.get(pk=project_pk)
                )
            )
        datasets = ds.get(project_pk)

        extra_context = extra_context or {}
        extra_context.update(
            dict(
                # Include common variables for rendering the admin template
                self.admin_site.each_context(request),
                datasets=datasets,
                model_name=Project._meta.verbose_name_plural,
                app_label=DataintegrationConfig.get_simple_appname(),
                app_verbose_name=DataintegrationConfig.verbose_name,
                page_title=page_title,
            )
        )

        return TemplateResponse(
            request,
            "data_integration/dataset_list.html",
            context=extra_context,
        )

    dataset_list.short_description = _("Show list of datasets")


class DataSetAdmin(admin.ModelAdmin):
    list_display = ["name"]
    fields = [
        "name",
        "title",
        "bbox",
        "minimum_scale",
        "maximum_scale",
        "source_detail",
        "crs_detail",
        "path",
        "driver",
    ]

    readonly_fields = [
        "name",
        "title",
        "bbox",
        "source_detail",
        "crs_detail",
        "path",
        "driver",
    ]

    def source_detail(self, obj):
        snippet_parts = ["<ul>"]
        for key in obj.source:
            snippet_parts.append(
                f'<li><label>{key}</label> → <span class="badge badge-secondary">{obj.source[key]}</span></li>'
            )
        snippet_parts.append("</ul>")
        return mark_safe("".join(snippet_parts))

    source_detail.short_description = "Source"

    def crs_detail(self, obj):
        snippet_parts = ["<ul>"]
        for key in obj.crs:
            snippet_parts.append(
                f'<li><label>{key}</label> → <span class="badge badge-secondary">{obj.crs[key]}</span></li>'
            )
        snippet_parts.append("</ul>")
        return mark_safe("".join(snippet_parts))

    crs_detail.short_description = "Crs"


@admin.register(RasterDataSet)
class RasterDataSetAdmin(DataSetAdmin):
    pass


@admin.register(CustomDataSet)
class CustomDataSetAdmin(DataSetAdmin):
    pass


@admin.register(VectorDataSet)
class VectorDataSetAdmin(DataSetAdmin):
    list_display = ["name", "mandant_name", "project_name", "field_count"]
    fields = DataSetAdmin.fields + ["fields_detail"]
    readonly_fields = DataSetAdmin.fields + ["fields_detail"]

    def mandant_name(self, obj: VectorDataSet):
        return obj.project.mandant.name

    def project_name(self, obj: VectorDataSet):
        return obj.project.name

    def fields_detail(self, obj: VectorDataSet):
        snippet_parts = ["<ul>"]
        for field in obj.fields.all():
            snippet_parts.append(
                f'<li><label>{field.name}</label> → <span class="badge badge-secondary">{field.type}</span></li>'
            )
        snippet_parts.append("</ul>")
        return mark_safe("".join(snippet_parts))

    fields_detail.short_description = "Fields"

    def field_count(self, obj):
        return mark_safe(
            '<span class="badge badge-secondary">{}</span>'.format(obj.fields.count())
        )

    field_count.admin_order_field = "field_count"
    field_count.short_description = "Fields"


@admin.register(Mandant)
class MandantAdmin(admin.ModelAdmin):
    pass
