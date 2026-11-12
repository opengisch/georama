from dataclasses import asdict
from types import SimpleNamespace

import pytest
from qgis_server_light.interface.exporter.api import ExportResult
from qgis_server_light.interface.exporter.extract import (
    Exporter,
    ExportMessage,
    Project,
    ResultWithMessages,
)
from rest_framework import status
from rest_framework.test import APIClient
from xsdata.formats.dataclass.serializers import JsonSerializer

from georama.integration.api import view_sets
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
    project = ProjectFactory.create(organisation=organisation)
    yield project
    project.delete()


@pytest.fixture
def organisation_vector(organisation_project):
    vector = VectorFactory.create(project=organisation_project, fields=[])
    yield vector
    vector.delete()


@pytest.fixture
def organisation_vector_field(organisation_vector):
    field = FieldFactory.create(datasource=organisation_vector)
    yield field
    field.delete()


@pytest.fixture
def organisation_raster(organisation_project):
    raster = RasterFactory.create(project=organisation_project)
    yield raster
    raster.delete()


@pytest.fixture
def organisation_custom(organisation_project):
    custom = CustomFactory.create(project=organisation_project)
    yield custom
    custom.delete()


@pytest.fixture
def organisation_admin_client(admin_user, admin_user_name, admin_password):
    client = APIClient()
    client.login(username=admin_user_name, password=admin_password)
    yield client


def server_name(organisation):
    return f"{organisation.domain}.localhost"


def mock_export_result(monkeypatch, result):
    response = SimpleNamespace(status_code=status.HTTP_200_OK, json=lambda: asdict(result))

    async def call_exporter(project_path):
        return response

    monkeypatch.setattr(view_sets, "call_qsl_exporter", call_exporter)


@pytest.fixture
def non_integrated_project_file(settings, tmp_path, organisation):
    settings.DATA_INTEGRATION_ROOT = tmp_path
    organisation_folder = tmp_path / organisation.domain
    organisation_folder.mkdir()
    project_file = organisation_folder / "broken.qgz"
    project_file.touch()
    return project_file


@pytest.fixture
def export_failure():
    return ResultWithMessages(
        project=Project(version="3.44", name="Broken project"),
        exporter=Exporter(qgis_version="3.44"),
        messages=[
            ExportMessage(
                level=ExportMessage.Level.ERROR,
                message="The project version is not supported.",
                code=ExportMessage.Code.PROJECT_VERSION_UNSUPPORTED,
            ),
            ExportMessage(
                level=ExportMessage.Level.WARNING,
                message="The layer is empty.",
                code=ExportMessage.Code.LAYER_EMPTY,
                layer_id="empty-layer",
            ),
        ],
    )


ENDPOINTS = [
    # path, fixture of the listed instance, formats
    ("/integration/manage/projects", "organisation_project", MANAGER_FORMATS),
    ("/integration/manage/datasources", "organisation_vector", MANAGER_FORMATS),
    ("/integration/manage/vector_datasources", "organisation_vector", MANAGER_FORMATS),
    (
        "/integration/manage/vector_datasource_fields",
        "organisation_vector_field",
        ORGANISATIONAL_FORMATS,
    ),
    ("/integration/manage/raster_datasources", "organisation_raster", ORGANISATIONAL_FORMATS),
    ("/integration/manage/custom_datasources", "organisation_custom", ORGANISATIONAL_FORMATS),
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
        organisation_admin_client,
        path,
        instance_fixture,
        response_format,
    ):
        request.getfixturevalue(instance_fixture)
        response = organisation_admin_client.get(
            path, {"f": response_format}, SERVER_NAME=server_name(organisation)
        )
        assert response.status_code == status.HTTP_200_OK

    @pytest.mark.django_db
    def test_detail_renders(
        self,
        request,
        organisation,
        organisation_admin_client,
        path,
        instance_fixture,
        response_format,
    ):
        instance = request.getfixturevalue(instance_fixture)
        response = organisation_admin_client.get(
            f"{path}/{instance.pk}",
            {"f": response_format},
            SERVER_NAME=server_name(organisation),
        )
        assert response.status_code == status.HTTP_200_OK


class TestJsonRepresentation:
    @pytest.mark.django_db
    def test_project(self, organisation, organisation_admin_client, organisation_project):
        response = organisation_admin_client.get(
            f"/integration/manage/projects/{organisation_project.pk}",
            {"f": "json"},
            SERVER_NAME=server_name(organisation),
        )
        assert response.json()["organisation_id"] == str(organisation.pk)

    @pytest.mark.parametrize(
        "path,instance_fixture",
        [
            ("/integration/manage/datasources", "organisation_vector"),
            ("/integration/manage/vector_datasources", "organisation_vector"),
            ("/integration/manage/raster_datasources", "organisation_raster"),
            ("/integration/manage/custom_datasources", "organisation_custom"),
        ],
    )
    @pytest.mark.django_db
    def test_datasource(
        self,
        request,
        organisation,
        organisation_admin_client,
        organisation_project,
        path,
        instance_fixture,
    ):
        instance = request.getfixturevalue(instance_fixture)
        response = organisation_admin_client.get(
            f"{path}/{instance.pk}",
            {"f": "json"},
            SERVER_NAME=server_name(organisation),
        )
        data = response.json()
        assert data["organisation_id"] == str(organisation.pk)
        assert data["project_id"] == str(organisation_project.pk)

    @pytest.mark.django_db
    def test_vector_field(
        self,
        organisation,
        organisation_admin_client,
        organisation_project,
        organisation_vector,
        organisation_vector_field,
    ):
        response = organisation_admin_client.get(
            f"/integration/manage/vector_datasource_fields/{organisation_vector_field.pk}",
            {"f": "json"},
            SERVER_NAME=server_name(organisation),
        )
        data = response.json()
        assert data["organisation_id"] == str(organisation.pk)
        assert data["project_id"] == str(organisation_project.pk)
        assert data["datasource_id"] == str(organisation_vector.pk)


class TestExportMessages:
    @pytest.mark.django_db
    def test_failed_export_returns_structured_json(
        self,
        monkeypatch,
        organisation,
        organisation_admin_client,
        non_integrated_project_file,
        export_failure,
    ):
        mock_export_result(
            monkeypatch,
            ExportResult(successful=False, content=JsonSerializer().render(export_failure)),
        )

        response = organisation_admin_client.post(
            "/integration/manage/projects/non_integrated/",
            {"path": non_integrated_project_file.name},
            query_params={"f": "json"},
            SERVER_NAME=server_name(organisation),
        )

        assert response.status_code == status.HTTP_400_BAD_REQUEST
        assert response.json()["result"]["messages"] == [
            {
                "level": "error",
                "message": "The project version is not supported.",
                "code": "project_version_unsupported",
                "layer_id": None,
            },
            {
                "level": "warning",
                "message": "The layer is empty.",
                "code": "layer_empty",
                "layer_id": "empty-layer",
            },
        ]

    @pytest.mark.django_db
    def test_failed_export_renders_messages(
        self,
        monkeypatch,
        organisation,
        organisation_admin_client,
        non_integrated_project_file,
        export_failure,
    ):
        mock_export_result(
            monkeypatch,
            ExportResult(successful=False, content=JsonSerializer().render(export_failure)),
        )

        response = organisation_admin_client.post(
            "/integration/manage/projects/non_integrated/",
            {"path": non_integrated_project_file.name},
            SERVER_NAME=server_name(organisation),
        )
        content = response.text

        assert response.status_code == status.HTTP_400_BAD_REQUEST
        assert "The project could not be integrated." in content
        assert "The project version is not supported." in content
        assert "The layer is empty." in content
        assert "empty-layer" in content
        assert "Retry" in content

    @pytest.mark.django_db
    def test_project_detail_renders_export_warnings(
        self, organisation, organisation_admin_client, organisation_project
    ):
        organisation_project.config |= {
            "messages": [
                {
                    "level": "warning",
                    "message": "The layer is empty.",
                    "code": "layer_empty",
                    "layer_id": "empty-layer",
                }
            ]
        }
        organisation_project.save(update_fields=["config"])

        response = organisation_admin_client.get(
            f"/integration/manage/projects/{organisation_project.pk}/ashow/",
            SERVER_NAME=server_name(organisation),
        )
        content = response.text

        assert response.status_code == status.HTTP_200_OK
        assert "Empty layer" in content
        assert "The layer is empty." in content
        assert "empty-layer" in content
