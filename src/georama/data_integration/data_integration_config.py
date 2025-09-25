from django.conf import settings


class Config:
    @property
    def path(self) -> str:
        return settings.DATA_INTEGRATION_ROOT

    @property
    def qgis_server_light_exporter_url(self) -> str:
        return settings.QSL_EXPORTER_URL

    @property
    def qgis_project_extensions(self) -> list[str]:
        return [".qgz", ".qgs"]
