import logging
from typing import Tuple

from django.http import HttpRequest
from django.shortcuts import redirect
from django.views import View
from qgis_server_light.interface.qgis import Config, Vector
from xsdata.formats.dataclass.parsers import JsonParser
from xsdata.formats.dataclass.parsers.config import ParserConfig
from xsdata.formats.dataclass.serializers import DictEncoder

from georama.data_integration.admin import (
    QgisProject,
    QgisProjectFileStructure,
    QgisProjectGroup,
)
from georama.data_integration.data_integration_config import (
    Config as DataintgrationConfig,
)
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
    def get_vector_dataset_by_id(self, id: str):
        vector_dataset_qs = VectorDataSet.objects.filter(qgis_layer_id=id)
        if vector_dataset_qs.exists():
            return vector_dataset_qs.get()
        else:
            return None

    @staticmethod
    def find_config_vector_dataset_field_by_name(vector_dataset: Vector, name: str):
        for field in vector_dataset.fields:
            if field.name == name:
                return field

    @staticmethod
    def find_config_vector_dataset_by_id(vector_datasets: list[Vector], id: str):
        for vector_dataset in vector_datasets:
            if vector_dataset.id == id:
                return vector_dataset

    @staticmethod
    def load_project_config(
        mandant_name: str, project_name: str
    ) -> Tuple[QgisProject, Config] | Tuple[None, None] | Tuple[QgisProject, None]:
        config = DataintgrationConfig()
        qpfs = QgisProjectFileStructure(config.path)
        qpfs.create_groups(config.qgis_project_extensions)
        group = qpfs.find_group_by_name(mandant_name)
        if not isinstance(group, QgisProjectGroup):
            return None, None
        project = group.find_project_by_name(project_name)
        if not isinstance(project, QgisProject):
            return None, None
        if not project.has_config:
            return project, None
        parser_config = ParserConfig(
            fail_on_unknown_properties=False, fail_on_unknown_attributes=False
        )
        parser = JsonParser(parser_config)
        project_config = parser.parse(project.config_path, Config)
        return project, project_config

    def get(self, request: HttpRequest, mandant_name: str, project_name: str, **kwargs):
        project, project_config = self.load_project_config(mandant_name, project_name)
        if not project_config or not project:
            redirect("admin:data_integration_project_changelist")
        mandant_qs = Mandant.objects.filter(name=mandant_name)
        if not mandant_qs.exists():
            mandant_db = Mandant(name=mandant_name)
            mandant_db.save()
        else:
            # we can do so, because name is unique in DB
            mandant_db = mandant_qs.get()
        project_qs = Project.objects.filter(name=project_name, mandant=mandant_db)
        if not project_qs.exists():
            log.error("Project does not exists, we first create a new DB object.")
            project_db = Project(
                mandant=mandant_db,
                name=project_name,
                hash=project.hash,
                title=project_config.project.name,
            )
            project_db.save()
        else:
            log.error("Project exists, we proceed with the DB object.")
            project_db = project_qs.get()
            if project_db.hash == project.hash:
                log.error("HASH of config and in DB was the same. No further work necessary.")
                return redirect("admin:data_integration_project_changelist")
        for layer in project_config.datasets.vector:
            vector_dataset = self.get_vector_dataset_by_id(layer.id)
            if vector_dataset is None:
                # there was no dataset with the corresponding qgis layer id, so we creare one
                vector_dataset = VectorDataSet(
                    project=project_db,
                    name=layer.name,
                    title=layer.title,
                    bbox=layer.bbox.to_string(),
                    bbox_wgs84=layer.bbox_wgs84.to_string(),
                    path=layer.path,
                    styles=DictEncoder().encode(layer.styles),
                    driver=layer.driver,
                    source=DictEncoder().encode(layer.source),
                    qgis_layer_id=layer.id,
                    crs=DictEncoder().encode(layer.crs),
                    minimum_scale=layer.minimum_scale,
                    maximum_scale=layer.maximum_scale,
                )
            else:
                # we found the dataset in the database and we update it
                vector_dataset.update(
                    project=project_db,
                    name=layer.name,
                    title=layer.title,
                    bbox=layer.bbox.to_string(),
                    bbox_wgs84=layer.bbox_wgs84.to_string(),
                    path=layer.path,
                    styles=DictEncoder().encode(layer.styles),
                    driver=layer.driver,
                    source=DictEncoder().encode(layer.source),
                    crs=DictEncoder().encode(layer.crs),
                    minimum_scale=layer.minimum_scale,
                    maximum_scale=layer.maximum_scale,
                )
            vector_dataset.save()
            for field in layer.fields:
                # loop through all fields in config
                field_qs = Field.objects.filter(
                    name=field.name, type=field.type, vector_dataset=vector_dataset
                )
                if not field_qs.exists():
                    # assure field does not exist in db
                    Field(
                        name=field.name, type=field.type, vector_dataset=vector_dataset
                    ).save()
            # finally get rid of old objects in the database which are not in the config anymore
            for field_db in Field.objects.filter(vector_dataset=vector_dataset).all():
                field_match = self.find_config_vector_dataset_field_by_name(
                    layer, field_db.name
                )
                if field_match is None:
                    # there is a fild in the db which does not exist in the config anymore
                    field_db.delete()
            for vector_dataset_db in VectorDataSet.objects.filter(project=project_db).all():
                vector_dataset_match = self.find_config_vector_dataset_by_id(
                    project_config.datasets.vector, vector_dataset_db.qgis_layer_id
                )
                if vector_dataset_match is None:
                    # there is a fild in the db which does not exist in the config anymore
                    vector_dataset_db.delete()
        for layer in project_config.datasets.raster:
            RasterDataSet(
                project=project_db,
                name=layer.name,
                title=layer.title,
                bbox=layer.bbox.to_string(),
                bbox_wgs84=layer.bbox_wgs84.to_string(),
                path=layer.path,
                styles=DictEncoder().encode(layer.styles),
                driver=layer.driver,
                source=DictEncoder().encode(layer.source),
                qgis_layer_id=layer.id,
                crs=DictEncoder().encode(layer.crs),
                minimum_scale=layer.minimum_scale,
                maximum_scale=layer.maximum_scale,
            ).save()
        for layer in project_config.datasets.custom:
            CustomDataSet(
                project=project_db,
                name=layer.name,
                title=layer.title,
                bbox=layer.bbox.to_string(),
                bbox_wgs84=layer.bbox_wgs84.to_string(),
                path=layer.path,
                styles=DictEncoder().encode(layer.styles),
                driver=layer.driver,
                source=DictEncoder().encode(layer.source),
                qgis_layer_id=layer.id,
                crs=DictEncoder().encode(layer.crs),
                minimum_scale=layer.minimum_scale,
                maximum_scale=layer.maximum_scale,
            ).save()
        return redirect("admin:data_integration_project_changelist")
