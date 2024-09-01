import os


class Config:

    @property
    def path(self) -> str:
        return os.path.join('/home/kalle/projects/opengis/georama.test_data')

    @property
    def default_crs(self):
        return 'https://www.opengis.net/def/crs/EPSG/0/2056'
