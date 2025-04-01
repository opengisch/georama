import os


class Config:
    @property
    def path(self) -> str:
        return os.path.join(os.environ.get("GEORAMA_DATA_INTEGRATION_ROOT", "/io/data"))

    @property
    def default_crs(self):
        return "https://www.opengis.net/def/crs/EPSG/0/2056"
