"""Content of the public read-only endpoints: `AllowAny` lets every persona in, the object
permissions filter what each one sees. A public and a non public object are published, the
viewer has the view permission on the non public one.
"""

from collections.abc import Callable
from typing import NamedTuple

import pytest
from django.db.models import Model
from django.urls import reverse

from georama.features.models import FeatureLayer
from georama.maps.models import WmsLayer
from georama.webgis.models import Theme
from tests.api.routes import LAYER_JSON, VIEWERS
from tests.conftest import PERSONAS
from tests.fixtures.layers import (
    create_feature_layer,
    create_theme,
    create_wms_layer,
    with_geogirafe_json,
)


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


@pytest.fixture
def published(project_global_organisation, global_vector) -> dict[type[Model], tuple[Model, Model]]:
    """The public and the non public object of each model."""
    return {
        WmsLayer: tuple(
            create_wms_layer(global_vector, public, queryable=True) for public in (True, False)
        ),
        FeatureLayer: tuple(
            create_feature_layer(global_vector, public) for public in (True, False)
        ),
        Theme: tuple(
            with_geogirafe_json(create_theme(project_global_organisation, public))
            for public in (True, False)
        ),
    }


def cases():
    for name in ENDPOINTS:
        marks = [pytest.mark.xfail(strict=True, reason=LAYER_JSON)] if name in BROKEN else []
        for persona_name in PERSONAS:
            yield pytest.param(name, persona_name, marks=marks, id=f"{name}-{persona_name}")


@pytest.mark.django_db
@pytest.mark.parametrize("name, persona_name", list(cases()))
def test_persona_sees_public_and_permitted_objects(client_as, published, name, persona_name):
    endpoint = ENDPOINTS[name]
    public, non_public = published[endpoint.model]
    client = client_as(persona_name, objects=[non_public] if persona_name == "viewer" else ())
    expected = {public, non_public} if persona_name in VIEWERS else {public}
    response = client.get(
        reverse(endpoint.route, kwargs=endpoint.kwargs), HTTP_ACCEPT="application/json"
    )
    assert response.status_code == 200
    assert endpoint.ids(response.json()) == {str(obj.pk) for obj in expected}
