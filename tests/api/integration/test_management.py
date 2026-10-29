import pytest
from rest_framework import status

from georama.integration.factories import (
    CustomFactory,
    FieldFactory,
    ProjectFactory,
    RasterFactory,
    VectorFactory,
)

MANAGER_FORMATS = ["html", "json", "api"]
ORGANISATIONAL_FORMATS = ["json", "api"]


@pytest.fixture
def organisation_project(organisation):
    return ProjectFactory.create(organisation=organisation)


@pytest.fixture
def organisation_vector(organisation_project):
    return VectorFactory.create(project=organisation_project, fields=[])


@pytest.fixture
def organisation_vector_field(organisation_vector):
    return FieldFactory.create(datasource=organisation_vector)


@pytest.fixture
def organisation_raster(organisation_project):
    return RasterFactory.create(project=organisation_project)


@pytest.fixture
def organisation_custom(organisation_project):
    return CustomFactory.create(project=organisation_project)


@pytest.fixture
def superuser_client(client_as, organisation):
    return client_as("superuser", organisation)


ENDPOINTS = [
    # path, fixture of the listed instance, formats
    ("/integration/manage/projects/", "organisation_project", MANAGER_FORMATS),
    ("/integration/manage/datasources/", "organisation_vector", MANAGER_FORMATS),
    ("/integration/manage/vector_datasources/", "organisation_vector", MANAGER_FORMATS),
    (
        "/integration/manage/vector_datasource_fields/",
        "organisation_vector_field",
        ORGANISATIONAL_FORMATS,
    ),
    ("/integration/manage/raster_datasources/", "organisation_raster", ORGANISATIONAL_FORMATS),
    ("/integration/manage/custom_datasources/", "organisation_custom", ORGANISATIONAL_FORMATS),
]

ENDPOINT_FORMATS = [
    pytest.param(path, instance_fixture, response_format, id=f"{path}?f={response_format}")
    for path, instance_fixture, formats in ENDPOINTS
    for response_format in formats
]


@pytest.mark.parametrize("path,instance_fixture,response_format", ENDPOINT_FORMATS)
class TestRendering:
    @pytest.mark.django_db
    def test_list_renders(
        self,
        request,
        organisation,
        superuser_client,
        path,
        instance_fixture,
        response_format,
    ):
        request.getfixturevalue(instance_fixture)
        response = superuser_client.get(path, {"f": response_format})
        assert response.status_code == status.HTTP_200_OK

    @pytest.mark.django_db
    def test_detail_renders(
        self,
        request,
        organisation,
        superuser_client,
        path,
        instance_fixture,
        response_format,
    ):
        instance = request.getfixturevalue(instance_fixture)
        response = superuser_client.get(f"{path}{instance.pk}/", {"f": response_format})
        assert response.status_code == status.HTTP_200_OK


class TestJsonRepresentation:
    @pytest.mark.django_db
    def test_project(self, organisation, superuser_client, organisation_project):
        response = superuser_client.get(
            f"/integration/manage/projects/{organisation_project.pk}/", {"f": "json"}
        )
        assert response.json()["organisation_id"] == str(organisation.pk)

    @pytest.mark.parametrize(
        "path,instance_fixture",
        [
            ("/integration/manage/datasources/", "organisation_vector"),
            ("/integration/manage/vector_datasources/", "organisation_vector"),
            ("/integration/manage/raster_datasources/", "organisation_raster"),
            ("/integration/manage/custom_datasources/", "organisation_custom"),
        ],
    )
    @pytest.mark.django_db
    def test_datasource(
        self,
        request,
        organisation,
        superuser_client,
        organisation_project,
        path,
        instance_fixture,
    ):
        instance = request.getfixturevalue(instance_fixture)
        response = superuser_client.get(f"{path}{instance.pk}/", {"f": "json"})
        data = response.json()
        assert data["organisation_id"] == str(organisation.pk)
        assert data["project_id"] == str(organisation_project.pk)

    @pytest.mark.django_db
    def test_vector_field(
        self,
        organisation,
        superuser_client,
        organisation_project,
        organisation_vector,
        organisation_vector_field,
    ):
        response = superuser_client.get(
            f"/integration/manage/vector_datasource_fields/{organisation_vector_field.pk}/",
            {"f": "json"},
        )
        data = response.json()
        assert data["organisation_id"] == str(organisation.pk)
        assert data["project_id"] == str(organisation_project.pk)
        assert data["datasource_id"] == str(organisation_vector.pk)
