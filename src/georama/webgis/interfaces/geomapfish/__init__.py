import json
import logging

import requests
from xsdata.formats.dataclass.parsers.config import ParserConfig

from georama.webgis.interfaces.geomapfish.themes_json_2_8.dataclasses import (
    Attribute,
    LinkedLayer,
    OgcServer,
    Themes,
    ThemesJson,
)
from georama.webgis.interfaces.geomapfish.themes_json_2_8.parsers import (
    CustomDictDecoder,
)

d = {
    "id": 1608,
    "name": "Accidents avec la part. de piétons",
    "metadata": {
        "legend": True,
        "legendImage": "https://api3.geo.admin.ch/static/images/legends/ch.astra.unfaelle-personenschaeden_fussgaenger_fr.png",
        "metadataUrl": "https://www.geocat.ch/geonetwork/srv/ger/md.viewer#/full_view/578457c1-debb-41b9-8f2c-18d33148cfa5",
        "ogcServer": "source for http://wms.geo.admin.ch/ image/png",
        "queryLayers": "ch.astra.unfaelle-personenschaeden_fussgaenger",
    },
    "dimensions": {},
    "type": "WMTS",
    "url": "https://wmts.geo.admin.ch/EPSG/2056/1.0.0/WMTSCapabilities.xml",
    "matrixSet": "2056",
    "layer": "ch.astra.unfaelle-personenschaeden_fussgaenger",
    "imageType": "image/png",
}


def load_geoportal_config(themes_json_dict: dict) -> ThemesJson | None:
    config = ParserConfig(fail_on_unknown_properties=False)
    decoder = CustomDictDecoder(config)

    themes_json = ThemesJson()
    for ogc_key in themes_json_dict["ogcServers"]:
        ogc_server = decoder.decode(themes_json_dict["ogcServers"][ogc_key], OgcServer)
        ogc_server.name = ogc_key
        if isinstance(themes_json_dict["ogcServers"][ogc_key]["attributes"], dict):
            for linked_layer_key in themes_json_dict["ogcServers"][ogc_key]["attributes"]:
                linked_layer = LinkedLayer(name=linked_layer_key)
                for attr_key in themes_json_dict["ogcServers"][ogc_key]["attributes"][
                    linked_layer_key
                ]:
                    attribute = decoder.decode(
                        themes_json_dict["ogcServers"][ogc_key]["attributes"][linked_layer_key][
                            attr_key
                        ],
                        Attribute,
                    )
                    attribute.name = attr_key
                    linked_layer.attributes.append(attribute)
                ogc_server.attributes.append(linked_layer)

        themes_json.ogc_servers.append(ogc_server)
    themes = decoder.decode({"themes": themes_json_dict["themes"]}, Themes)
    themes_json.themes = themes.themes
    return themes_json


def load_geoportal_config_from_url(url: str) -> ThemesJson | None:
    try:
        response = requests.get(url)
        response_dict = response.json()
    except Exception as e:
        logging.info(f"Could not load themes json from url. Error was {e}")
        return None
    return load_geoportal_config(response_dict)


def load_geoportal_config_from_path(path: str) -> ThemesJson | None:
    with open(path, mode="rb") as f:
        return load_geoportal_config(json.load(f))
