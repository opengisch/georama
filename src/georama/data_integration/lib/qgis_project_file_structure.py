import hashlib
import os
from dataclasses import dataclass, field
from pathlib import Path

from georama.data_integration.data_integration_config import Config
from georama.data_integration.models import Project


@dataclass
class QgisProject:
    parent: "QgisProjectGroup"
    name: str
    suffix: str
    database_representation: Project | None = None
    # TODO RU: Check which Config we actually need here!
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
    def project_path_as_string(self) -> str:
        return f"{self.parent.name}/{self.name}{self.suffix}"

    @property
    def has_config(self) -> bool:
        return os.path.isfile(self.config_path)

    @property
    def hash(self) -> str:
        if self.has_config:
            with open(self.config_path, mode="rb") as cf:
                return hashlib.md5(cf.read()).hexdigest()

    @property
    def icon(self) -> str:
        return "images/qgis.png" if self.database_representation else "images/qgis_grey.png"


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
