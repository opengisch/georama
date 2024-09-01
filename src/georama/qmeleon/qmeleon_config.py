import os


class Config:
    @property
    def path(self) -> str:
        return os.path.join('/home/kalle/projects/opengis/georama.test_data')

    @property
    def qgis_project_extensions(self) -> list[str]:
        return ['.qgz', '.qgs']
