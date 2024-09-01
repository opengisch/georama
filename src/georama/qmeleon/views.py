import logging
from django.shortcuts import redirect
from django.views import View
from django.views.generic import TemplateView
from django.template import loader
from django.http import HttpResponse, HttpRequest
from xsdata.formats.dataclass.parsers import JsonParser
from xsdata.formats.dataclass.serializers import DictEncoder

from georama.qmeleon.models import Project, VectorDataSet, RasterDataSet, Field
from dataclasses import asdict
from georama.qmeleon.qmeleon_config import Config as QmeleonConfig
from georama.qmeleon.admin import QgisProjectFileStructure, QgisProjectGroup, QgisProject
from qgis_server_light.interface.qgis import Config

log = logging.getLogger(__name__)


class RegisterQgisProject(View):
    # TODO: generate Landing Page depending on the installed georama apps.

    def get(self, request: HttpRequest, group_name: str, project_name: str, **kwargs):
        config = QmeleonConfig()
        qpfs = QgisProjectFileStructure(config.path)
        qpfs.create_groups(config.qgis_project_extensions)
        group = qpfs.find_group_by_name(group_name)
        if not isinstance(group, QgisProjectGroup):
            redirect('admin:qmeleon_project_changelist')
        project = group.find_project_by_name(project_name)
        if not isinstance(group, QgisProject):
            redirect('admin:qmeleon_project_changelist')
        if not project.has_config:
            redirect('admin:qmeleon_project_changelist')

        project_config = JsonParser().parse(project.config_path, Config)
        projects_db = None
        try:
            projects_db = Project.objects.get(
                name=project_name,
                group=group_name,
                hash=project.hash
            )
        except Project.DoesNotExist as e:
            log.error(e)
        if projects_db is None:
            new_project = Project(
                group=group_name,
                name=project_name,
                hash=project.hash,
                title=project_config.project.name
            )
            new_project.save()
            for layer in project_config.datasets.vector:
                vector_dataset = VectorDataSet(
                    project=new_project,
                    name=layer.name,
                    title=layer.title,
                    bbox=layer.bbox.to_string(),
                    bbox_wgs84=layer.bbox_wgs84.to_string(),
                    path=layer.path,
                    style=layer.style,
                    driver=layer.driver,
                    source=DictEncoder().encode(layer.source),
                    qgis_layer_id=layer.id,
                    crs=DictEncoder().encode(layer.crs)
                )
                vector_dataset.save()
                for field in layer.fields:
                    Field(
                        name=field.name,
                        type=field.type,
                        vector_dataset=vector_dataset
                    ).save()
            for layer in project_config.datasets.raster:
                RasterDataSet(
                    project=new_project,
                    name=layer.name,
                    title=layer.title,
                    bbox=layer.bbox.to_string(),
                    bbox_wgs84=layer.bbox_wgs84.to_string(),
                    path=layer.path,
                    style=layer.style,
                    driver=layer.driver,
                    source=DictEncoder().encode(layer.source),
                    qgis_layer_id=layer.id,
                    crs=DictEncoder().encode(layer.crs)
                ).save()
            return redirect('admin:qmeleon_project_changelist')
        else:
            # TODO: Handle update etc. of projects
            log.info('Project existed. Updating process not implemented yet => delete the project and integrate it again!')
            return redirect('admin:qmeleon_project_changelist')


