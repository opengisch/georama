from georama.maps.views.ogc import OgcServer
from georama.webgis.apps import WebGisConfig
from georama.webgis.models import WmsLayer


class OgcServerWebGis(OgcServer):
    model = WmsLayer
    appname = WebGisConfig.get_simple_appname()
