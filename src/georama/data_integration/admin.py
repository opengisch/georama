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
    DataSet,
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
    fields = [
        "name",
        "title",
        "bbox",
        "minimum_scale",
        "maximum_scale",
        "source_detail",
        "crs_detail",
        "path_detail",
        "driver",
    ]

    def get_readonly_fields(self, request, obj=None):
        # TODO PI: What should not be editable when it's a manual dataset?
        readonly_fields = [
            "name",
            "qgis_layer_id",
            "bbox",
            "source_detail",
            "crs_detail",
            "path_detail",
            "driver",
        ]
        if self.belongs_to_a_project(obj):
            return readonly_fields + ["title"]
        else:
            return readonly_fields

    @staticmethod
    def belongs_to_a_project(obj):
        return obj and obj.project is not None

    @admin.display(description=DataSet._meta.get_field("source").verbose_name)
    def source_detail(self, obj):
        for key in obj.source:
            if obj.source[key] is not None:
                return mark_safe(f"{key}<pre><code>{obj.source[key]}</code></pre>")
        return "-"

    @admin.display(description=DataSet._meta.get_field("crs").verbose_name)
    def crs_detail(self, obj):
        return obj.crs["AuthId"]

    @admin.display(description=DataSet._meta.get_field("path").verbose_name)
    def path_detail(self, obj):
        return mark_safe(f"<pre><code>{obj.path}</code></pre>")

    def get_form(self, request, obj=None, **kwargs):
        # Overwrite form to add help_text from the model
        help_texts = {
            "source_detail": DataSet._meta.get_field("source").help_text,
            "crs_detail": DataSet._meta.get_field("crs").help_text,
            "path_detail": DataSet._meta.get_field("path").help_text,
        }
        kwargs.update({"help_texts": help_texts})
        return super().get_form(request, obj, **kwargs)

    def change_view(self, request, object_id=None, form_url="", extra_context=None):
        extra_context = extra_context or {}
        extra_context["show_save_and_add_another"] = False
        extra_context["parent_page_title"] = "TODO"
        return super().change_view(
            request,
            object_id,
            form_url,
            extra_context=extra_context,
        )


@admin.register(RasterDataSet)
class RasterDataSetAdmin(DataSetAdmin):
    pass


@admin.register(CustomDataSet)
class CustomDataSetAdmin(DataSetAdmin):
    pass


@admin.register(VectorDataSet)
class VectorDataSetAdmin(DataSetAdmin):

    fields = DataSetAdmin.fields + ["fields_detail"]

    def get_readonly_fields(self, request, obj=None):
        return DataSetAdmin.get_readonly_fields(self, request, obj) + ["fields_detail"]

    def mandant_name(self, obj: VectorDataSet):
        return obj.project.mandant.name

    def project_name(self, obj: VectorDataSet):
        return obj.project.name

    @admin.display(description=_("Fields"))
    def fields_detail(self, obj: VectorDataSet):
        if obj and obj.fields.count() == 0:
            return _("No fields defined")

        total = _("Dataset contains {count} fields".format(count=obj.fields.count()))
        snippet_parts = [f"<span>{total}:</span>" '<ul class="list-group list-group-flush">']
        for f in obj.fields.all():
            snippet_parts.append(
                f'<li class="list-group-item"><code>{f.name} [{f.type}]</code></li>'
            )
        snippet_parts.append("</ul>")
        return mark_safe("".join(snippet_parts))


@admin.register(Mandant)
class MandantAdmin(admin.ModelAdmin):
    pass
