import os


class Config:
    @property
    def path(self) -> str:
        # return os.path.join('/home/kalle/projects/opengis/georama.test_data')
        return os.path.join(os.environ.get("GEORAMA_QMELEON_DATA_MOUNT", "/io/data"))

    @property
    def qgis_project_extensions(self) -> list[str]:
        return [".qgz", ".qgs"]
