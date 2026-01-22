import logging
import os

from qgis_server_light.interface.qgis import Config as QslConfig
from xsdata.formats.dataclass.parsers import JsonParser
from xsdata.formats.dataclass.parsers.config import ParserConfig

from georama.core.services import Service
from georama.data_integration.admin import (
    QgisProject,
    QgisProjectFileStructure,
    QgisProjectGroup,
)
from georama.data_integration.data_integration_config import Config
from georama.data_integration.models import (
    CustomDataSet,
    Project,
    RasterDataSet,
    VectorDataSet,
)


class ProjectService(Service):
    models = [Project]
    name = "project"

    def __init__(self):
        self.config = Config()
        self.qgis_project_file_structure = QgisProjectFileStructure(
            os.path.join(self.config.path)
        )
        self.qgis_project_file_structure.create_groups(self.config.qgis_project_extensions)

    def count(self) -> int:
        count = 0
        for group in self.qgis_project_file_structure.groups:
            count += len(group.projects)
        return count

    def get(self, group_name=None, project_name=None, **kwargs) -> list[QgisProject]:
        if group_name is None or project_name is None:
            raise KeyError(
                f"To get a project from FileSystem we need both: "
                f"GroupName AND ProjectName but got group_name={group_name} "
                f"project_name={project_name}"
            )
        found_group = self.qgis_project_file_structure.find_group_by_name(group_name)
        found_project = found_group.find_project_by_name(project_name)
        return [found_project]

    def get_list(self) -> list[QgisProjectGroup]:
        integrated_projects = Project.objects.all()
        for integrated_project in integrated_projects:
            found_group = self.qgis_project_file_structure.find_group_by_name(
                integrated_project.mandant.name
            )
            found_project = found_group.find_project_by_name(integrated_project.name)
            found_project.database_representation = integrated_project
        for group in self.qgis_project_file_structure.groups:
            for project in group.projects:
                project.config = self.load_project_config(project)
        return self.qgis_project_file_structure.groups

    def get_list_page(self, start=0, offset=100) -> list[QgisProjectGroup]:
        return self.get_list()

    def load_project_config(self, project: QgisProject) -> QslConfig | None:
        parser_config = ParserConfig(
            fail_on_unknown_properties=False, fail_on_unknown_attributes=False
        )
        parser = JsonParser(parser_config)
        if project.has_config:
            try:
                project_config = parser.parse(project.config_path, QslConfig)
                return project_config
            except Exception as e:
                logging.info(project.name)
                logging.error(e)
        return None


class ProjectDatasetsService(Service):
    models = [VectorDataSet, RasterDataSet, CustomDataSet]
    name = "project_dataset"

    def filter(self, query, **kwargs):
        return query.filter(project__pk=kwargs["pk"])


class ManualDatasetService(Service):
    models = [VectorDataSet, RasterDataSet, CustomDataSet]
    name = "manual_dataset"

    def filter(self, query, **kwargs):
        return query.filter(project__isnull=True)
