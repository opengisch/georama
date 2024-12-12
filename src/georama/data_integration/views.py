import logging

from django.http import HttpRequest
from django.shortcuts import redirect
from django.views import View
from qgis_server_light.interface.qgis import Config
from xsdata.formats.dataclass.parsers import JsonParser
from xsdata.formats.dataclass.serializers import DictEncoder

from georama.data_integration.admin import (
    QgisProject,
    QgisProjectFileStructure,
    QgisProjectGroup,
)
from georama.data_integration.data_integration_config import Config as QmeleonConfig
from georama.data_integration.models import (
    CustomDataSet,
    Field,
    Mandant,
    Project,
    RasterDataSet,
    VectorDataSet,
)

log = logging.getLogger(__name__)


class RegisterQgisProject(View):
    # TODO: generate Landing Page depending on the installed georama apps.

    def get(self, request: HttpRequest, group_name: str, project_name: str, **kwargs):
        config = QmeleonConfig()
        qpfs = QgisProjectFileStructure(config.path)
        qpfs.create_groups(config.qgis_project_extensions)
        group = qpfs.find_group_by_name(group_name)
        if not isinstance(group, QgisProjectGroup):
            redirect("admin:data_integration_project_changelist")
        project = group.find_project_by_name(project_name)
        if not isinstance(group, QgisProject):
            redirect("admin:data_integration_project_changelist")
        if not project.has_config:
            redirect("admin:data_integration_project_changelist")
        mandant_qs = Mandant.objects.filter(name=group_name)
        if not mandant_qs.exists():
            mandant_db = Mandant(name=group_name)
            mandant_db.save()
        else:
            # we can do so, because name is unique in DB
            mandant_db = mandant_qs.get()

        project_config = JsonParser().parse(project.config_path, Config)
        project_qs = Project.objects.filter(name=project_name, mandant=mandant_db)
        if not project_qs.exists():
            project_db = Project(
                mandant=mandant_db,
                name=project_name,
                hash=project.hash,
                title=project_config.project.name,
            )
            project_db.save()
            for layer in project_config.datasets.vector:
                vector_dataset = VectorDataSet(
                    project=project_db,
                    name=layer.name,
                    title=layer.title,
                    bbox=layer.bbox.to_string(),
                    bbox_wgs84=layer.bbox_wgs84.to_string(),
                    path=layer.path,
                    style=layer.style,
                    driver=layer.driver,
                    source=DictEncoder().encode(layer.source),
                    qgis_layer_id=layer.id,
                    crs=DictEncoder().encode(layer.crs),
                )
                vector_dataset.save()
                for field in layer.fields:
                    Field(
                        name=field.name, type=field.type, vector_dataset=vector_dataset
                    ).save()
            for layer in project_config.datasets.raster:
                RasterDataSet(
                    project=project_db,
                    name=layer.name,
                    title=layer.title,
                    bbox=layer.bbox.to_string(),
                    bbox_wgs84=layer.bbox_wgs84.to_string(),
                    path=layer.path,
                    style=layer.style,
                    driver=layer.driver,
                    source=DictEncoder().encode(layer.source),
                    qgis_layer_id=layer.id,
                    crs=DictEncoder().encode(layer.crs),
                ).save()
            for layer in project_config.datasets.custom:
                CustomDataSet(
                    project=project_db,
                    name=layer.name,
                    title=layer.title,
                    bbox=layer.bbox.to_string(),
                    bbox_wgs84=layer.bbox_wgs84.to_string(),
                    path=layer.path,
                    style=layer.style,
                    driver=layer.driver,
                    source=DictEncoder().encode(layer.source),
                    qgis_layer_id=layer.id,
                    crs=DictEncoder().encode(layer.crs),
                ).save()
            return redirect("admin:data_integration_project_changelist")

        else:
            # TODO: Handle update etc. of projects
            log.info(
                "Project existed. Updating process not implemented yet => delete the project and integrate it again!"
            )
            return redirect("admin:data_integration_project_changelist")
