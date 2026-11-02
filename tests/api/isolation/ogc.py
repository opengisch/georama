"""The requests of the isolation tests on the OGC services, see `Ogc` in `checks.py`."""

from collections.abc import Callable
from typing import NamedTuple

from django.db.models import Model

from georama.maps.services.wfs_2_0_0 import WfsOperation

WMS = {"SERVICE": "WMS", "VERSION": "1.3.0"}
WFS = {"SERVICE": "WFS", "VERSION": "2.0.0"}

CAPABILITIES = {
    "WMS": {**WMS, "REQUEST": "GetCapabilities"},
    "WFS": {**WFS, "REQUEST": "GetCapabilities"},
}


def type_name(layer: Model) -> str:
    return f"{WfsOperation.own_namespace}:{WfsOperation.encode_layer_name(layer.identifier)}"


class LayerRequest(NamedTuple):
    # the parameters of the request on the layer, but its REQUEST
    params: Callable[[Model], dict]
    # a QSL job is posted for the layer, else the layer is answered
    rendered: bool


# by REQUEST
LAYER_REQUESTS = {
    "GetMap": LayerRequest(
        lambda layer: {
            **WMS,
            "LAYERS": layer.identifier,
            "STYLES": "",
            "CRS": "EPSG:3857",
            "BBOX": "0,0,1,1",
            "WIDTH": "10",
            "HEIGHT": "10",
            "FORMAT": "image/png",
        },
        rendered=True,
    ),
    "GetLegendGraphic": LayerRequest(
        lambda layer: {**WMS, "LAYERS": layer.identifier, "FORMAT": "image/png"}, rendered=True
    ),
    "GetFeature": LayerRequest(lambda layer: {**WFS, "TYPENAMES": type_name(layer)}, rendered=True),
    "DescribeFeatureType": LayerRequest(
        lambda layer: {**WFS, "TYPENAME": type_name(layer)}, rendered=False
    ),
    "GetMetadata": LayerRequest(lambda layer: {"LAYER": layer.identifier}, rendered=False),
}


def layer_request(operation: str, layer: Model) -> dict:
    """The parameters of the request `operation` on `layer`."""
    return {"REQUEST": operation, **LAYER_REQUESTS[operation].params(layer)}
