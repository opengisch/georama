import hashlib
from dataclasses import dataclass
from pathlib import Path

from django.conf import settings


@dataclass
class QgisProject:
    path: Path
    organisation: str

    @property
    def config_format(self):
        return "json"

    @property
    def root_path(self) -> Path:
        return Path(settings.DATA_INTEGRATION_ROOT)

    @property
    def integration_root(self) -> Path:
        return self.root_path / self.organisation

    @property
    def project_path(self) -> Path:
        return self.root_path / self.path

    @property
    def path_from_root(self) -> Path:
        return self.project_path.relative_to(self.root_path)

    @property
    def path_from_orga(self) -> Path:
        return self.project_path.relative_to(self.integration_root)

    @property
    def config_path(self) -> Path:
        return Path(f"{self.project_path}.{self.config_format}")

    @property
    def config_path_from_root(self) -> Path:
        return self.config_path.relative_to(self.root_path)

    @property
    def config_path_from_orga(self) -> Path:
        return self.config_path.relative_to(self.integration_root)

    @property
    def has_config(self) -> bool:
        return self.config_path.exists()

    @property
    def hash(self) -> str | None:
        if self.has_config:
            with open(self.config_path, mode="rb") as cf:
                return hashlib.md5(cf.read()).hexdigest()
        return None


@dataclass
class QgisProjectCollection:
    organisation: str

    @property
    def glob_pattern(self) -> str:
        return "*.qg[sz]"

    def projects(self) -> list[QgisProject]:
        return self.projects_filtered()

    def projects_filtered(self, path_filter: set[Path] | None = None) -> list[QgisProject]:
        search_path = Path(settings.DATA_INTEGRATION_ROOT) / self.organisation
        if path_filter is None:
            path_filter = set()
        return [
            QgisProject(path=p, organisation=self.organisation)
            for p in search_path.rglob(self.glob_pattern)
            if p not in path_filter
        ]
