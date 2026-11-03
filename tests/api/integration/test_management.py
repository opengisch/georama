"""The manage endpoints of integration render the objects of alpha, in every format. The data
is `api_data`, see `tests/api/data.py`.
"""

import pytest
from rest_framework import status

from georama.integration.models import Custom, Project, Raster, Vector, VectorField
from tests.api.data import ALPHA

MANAGER_FORMATS = ["html", "json", "api"]
ORGANISATIONAL_FORMATS = ["json", "api"]

ENDPOINTS = [
    # path, model of the object rendered, formats
    ("/integration/manage/projects/", Project, MANAGER_FORMATS),
    ("/integration/manage/datasources/", Vector, MANAGER_FORMATS),
    ("/integration/manage/vector_datasources/", Vector, MANAGER_FORMATS),
    ("/integration/manage/vector_datasource_fields/", VectorField, ORGANISATIONAL_FORMATS),
    ("/integration/manage/raster_datasources/", Raster, ORGANISATIONAL_FORMATS),
    ("/integration/manage/custom_datasources/", Custom, ORGANISATIONAL_FORMATS),
]

ENDPOINT_FORMATS = [
    pytest.param(path, model, response_format, id=f"{path}?f={response_format}")
    for path, model, formats in ENDPOINTS
    for response_format in formats
]

DATASOURCES = [
    pytest.param(path, model, id=path)
    for path, model, _ in ENDPOINTS
    if model in (Vector, Raster, Custom)
]


@pytest.mark.django_db
@pytest.mark.parametrize("path, model, response_format", ENDPOINT_FORMATS)
def test_list_renders(api_data, path, model, response_format):
    response = api_data.client("superuser", ALPHA).get(path, {"f": response_format})
    assert response.status_code == status.HTTP_200_OK


@pytest.mark.django_db
@pytest.mark.parametrize("path, model, response_format", ENDPOINT_FORMATS)
def test_detail_renders(api_data, path, model, response_format):
    instance = api_data.objects[ALPHA][model]
    response = api_data.client("superuser", ALPHA).get(
        f"{path}{instance.pk}/", {"f": response_format}
    )
    assert response.status_code == status.HTTP_200_OK


@pytest.mark.django_db
def test_project_json(api_data):
    project = api_data.objects[ALPHA][Project]
    response = api_data.client("superuser", ALPHA).get(
        f"/integration/manage/projects/{project.pk}/", {"f": "json"}
    )
    assert response.json()["organisation_id"] == str(api_data.organisations[ALPHA].pk)


@pytest.mark.django_db
@pytest.mark.parametrize("path, model", DATASOURCES)
def test_datasource_json(api_data, path, model):
    instance = api_data.objects[ALPHA][model]
    data = api_data.client("superuser", ALPHA).get(f"{path}{instance.pk}/", {"f": "json"}).json()
    assert data["organisation_id"] == str(api_data.organisations[ALPHA].pk)
    assert data["project_id"] == str(api_data.objects[ALPHA][Project].pk)


@pytest.mark.django_db
def test_vector_field_json(api_data):
    field = api_data.objects[ALPHA][VectorField]
    response = api_data.client("superuser", ALPHA).get(
        f"/integration/manage/vector_datasource_fields/{field.pk}/", {"f": "json"}
    )
    data = response.json()
    assert data["organisation_id"] == str(api_data.organisations[ALPHA].pk)
    assert data["project_id"] == str(api_data.objects[ALPHA][Project].pk)
    assert data["datasource_id"] == str(api_data.objects[ALPHA][Vector].pk)
