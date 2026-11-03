"""The public read-only endpoints whose content is checked by `test_public_content.py`."""

from collections.abc import Callable
from typing import NamedTuple

from django.db.models import Model

from georama.features.models import FeatureLayer
from georama.maps.models import WmsLayer
from georama.webgis.models import Theme


class Endpoint(NamedTuple):
    model: type[Model]
    route: str
    # ids of the objects in the JSON answered
    ids: Callable[[dict], set[str]]
    kwargs: dict[str, str] = {}


def results(data: dict) -> set[str]:
    return {str(item["id"]) for item in data["results"]}


ENDPOINTS = {
    "maps-list": Endpoint(WmsLayer, "maps:maplayer-list", results),
    "features-list": Endpoint(FeatureLayer, "features:feature-list", results),
    "webgis-list": Endpoint(Theme, "webgis:theme-list", results),
    "webgis-geogirafe": Endpoint(
        Theme, "webgis:theme-geogirafe", lambda data: {str(theme["id"]) for theme in data["themes"]}
    ),
    "webgis-translation": Endpoint(
        Theme, "webgis:theme-translation", lambda data: set(data["en"]), {"lang": "en"}
    ),
}
# endpoints whose JSON cannot be rendered as soon as they list an object
BROKEN = {"maps-list", "features-list"}
