"""Content of the public read-only endpoints: `AllowAny` lets every persona in, the object
permissions filter what each one sees. A public and a non public object are published, the
viewer has the view permission on the non public one. The endpoints are declared in
`declarations.py`.
"""

import pytest
from django.db.models import Model
from django.urls import reverse

from georama.features.models import FeatureLayer
from georama.maps.models import WmsLayer
from georama.webgis.models import Theme
from tests.api.public_content.declarations import ENDPOINTS
from tests.api.routes.declarations import VIEWERS
from tests.fixtures.layers import (
    create_feature_layer,
    create_theme,
    create_wms_layer,
    with_geogirafe_json,
)
from tests.fixtures.personas import PERSONAS


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
        for persona_name in PERSONAS:
            yield pytest.param(name, persona_name, id=f"{name}-{persona_name}")


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
