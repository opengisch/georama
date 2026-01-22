import hashlib
import logging
import os
from dataclasses import dataclass, field
from pathlib import Path

from django.contrib import admin
from django.http import HttpRequest
from django.template.response import TemplateResponse
from django.urls import path, reverse
from django.utils.safestring import mark_safe

from georama.data_integration.data_integration_config import Config
from georama.data_integration.models import (
    CustomDataSet,
    Mandant,
    Project,
    RasterDataSet,
    VectorDataSet,
)


@dataclass
class QgisProject:
    parent: "QgisProjectGroup"
    name: str
    suffix: str
    database_representation: Project | None = None
    config: Config | None = None

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


class ProjectAdmin(admin.ModelAdmin):
    list_display = [
        "name",
        "mandant_name",
        "vector_dataset_count",
        "raster_dataset_count",
        "custom_dataset_count",
        "project_file_uptodate",
    ]

    def vector_dataset_count(self, obj):
        return obj.vector_datasets.count()

    vector_dataset_count.admin_order_field = "vector_dataset_count"
    vector_dataset_count.short_description = "Vector Datasets"

    def raster_dataset_count(self, obj):
        return obj.raster_datasets.count()

    raster_dataset_count.admin_order_field = "raster_dataset_count"
    raster_dataset_count.short_description = "Raster Datasets"

    def custom_dataset_count(self, obj):
        return obj.custom_datasets.count()

    custom_dataset_count.admin_order_field = "custom_dataset_count"
    custom_dataset_count.short_description = "Custom Datasets"

    def project_file_uptodate(self, obj: Project):
        try:
            config = Config()
            qpfs = QgisProjectFileStructure(config.path)
            qpfs.create_groups(config.qgis_project_extensions)
            group = qpfs.find_group_by_name(obj.mandant.name)
            project = group.find_project_by_name(obj.name)
            export_url = reverse(
                "georama.data_integration:export_qgis_project",
                kwargs={
                    "mandant_name": obj.mandant.name,
                    "project_name": obj.name,
                },
            )
            integrate_url = reverse(
                "georama.data_integration:register_qgis_project",
                kwargs={
                    "mandant_name": obj.mandant.name,
                    "project_name": obj.name,
                },
            )
            if obj.hash == project.hash:
                return mark_safe(
                    "".join(
                        [
                            '<div class="d-flex flex-nowrap">',
                            f'<a onclick="showWaitModalOverlay()" href="{export_url}" class="btn btn-high btn-success mr-2"><i class="fa fa-file-alt"></i> extract</a>',  # noqa: E501
                            '<a class="btn btn-high btn-success" style="pointer-events: none"><i class="fa fa-check-circle" aria-hidden="true"></i> integrated</a>',  # noqa: E501
                            "</div>",
                        ]
                    )
                )
            else:
                return mark_safe(
                    "".join(
                        [
                            '<div class="d-flex flex-nowrap">',
                            f'<a onclick="showWaitModalOverlay()" href="{export_url}" class="btn btn-high btn-success mr-2"><i class="fa fa-file-alt"></i> extract</a>',  # noqa: E501
                            f'<a href="{integrate_url}" class="btn btn-high btn-success"><i class="fa fa-arrow-alt-circle-up" aria-hidden="true"></i> integrate</a>',  # noqa: E501
                            "</div>",
                        ]
                    )
                )
        except Exception as e:
            logging.error(f"Could not check project status. Original Error: {e}")
            return ""

    project_file_uptodate.admin_order_field = "project_file_uptodate"
    project_file_uptodate.short_description = "Project File Status"

    def mandant_name(self, obj: Project):
        # TODO: make this a link to the dedicated mandant instance details
        return obj.mandant.name

    mandant_name.admin_order_field = "project_mandant_name"
    mandant_name.short_description = "Project Mandant Name"

    def get_urls(self):
        urls = super().get_urls()
        my_urls = [
            path(
                "qgis_projects/",
                self.admin_site.admin_view(self.qgis_projects),
                name="data_integration_qgis_projects",
            )
        ]
        return my_urls + urls

    def qgis_projects(self, request: HttpRequest, extra_context=None):
        config = Config()
        qgis_project_file_structure = QgisProjectFileStructure(os.path.join(config.path))
        qgis_project_file_structure.create_groups(config.qgis_project_extensions)

        context = dict(
            # Include common variables for rendering the admin template.
            self.admin_site.each_context(request),
            # Anything else you want in the context...
            qgis_project_file_structure=qgis_project_file_structure,
        )
        return TemplateResponse(
            request, "admin/data_integration/project/qgis_projects.html", context
        )

    def get_readonly_fields(self, request, obj=None):
        return ["integration_date", "hash"]


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
                f'<li><label>{key}</label> → <span class="badge badge-secondary">{obj.source[key]}</span></li>'  # noqa: E501
            )
        snippet_parts.append("</ul>")
        return mark_safe("".join(snippet_parts))

    source_detail.short_description = "Source"

    def crs_detail(self, obj):
        snippet_parts = ["<ul>"]
        for key in obj.crs:
            snippet_parts.append(
                f'<li><label>{key}</label> → <span class="badge badge-secondary">{obj.crs[key]}</span></li>'  # noqa: E501
            )
        snippet_parts.append("</ul>")
        return mark_safe("".join(snippet_parts))

    crs_detail.short_description = "Crs"


class RasterDataSetAdmin(DataSetAdmin):

    pass


class CustomDataSetAdmin(DataSetAdmin):
    pass


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
        for obj_field in obj.fields.all():
            snippet_parts.append(
                f'<li><label>{obj_field.name}</label> → <span class="badge badge-secondary">{obj_field.type}</span></li>'  # noqa: E501
            )
        snippet_parts.append("</ul>")
        return mark_safe("".join(snippet_parts))

    fields_detail.short_description = "Fields"

    def field_count(self, obj):
        return mark_safe(f'<span class="badge badge-secondary">{obj.fields.count()}</span>')

    field_count.admin_order_field = "field_count"
    field_count.short_description = "Fields"


class MandantAdmin(admin.ModelAdmin):
    pass


# Register your models here.
admin.site.register(Project, ProjectAdmin)
admin.site.register(Mandant, MandantAdmin)
admin.site.register(VectorDataSet, VectorDataSetAdmin)
admin.site.register(RasterDataSet, RasterDataSetAdmin)
admin.site.register(CustomDataSet, CustomDataSetAdmin)
