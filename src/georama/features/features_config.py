from django.conf import settings


class Config:
    @property
    def path(self) -> str:
        return settings.DATA_INTEGRATION_ROOT

    @property
    def default_crs(self):
        return "https://www.opengis.net/def/crs/EPSG/0/2056"
