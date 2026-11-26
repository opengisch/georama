from dataclasses import asdict
from types import SimpleNamespace

import pytest
from django.contrib.messages import get_messages
from qgis_server_light.interface.common import BBox, Crs
from qgis_server_light.interface.exporter.api import ExportResult
from qgis_server_light.interface.exporter.extract import (
    Config,
    Datasets,
    DataSource,
    Exporter,
    ExportMessage,
    MetaData,
    OgrSource,
    ResultWithMessages,
    Service,
    Tree,
    TreeGroup,
)
from qgis_server_light.interface.exporter.extract import Project as QslProject
from qgis_server_light.interface.exporter.extract import Vector as QslVector
from rest_framework import status
from rest_framework.test import APIClient
from xsdata.formats.dataclass.serializers import JsonSerializer

from georama.features.factories import FeatureLayerFactory
from georama.features.models import FeatureLayer
from georama.integration.api import view_sets
from georama.integration.factories import (
    CustomFactory,
    FieldFactory,
    ProjectFactory,
    RasterFactory,
    VectorFactory,
)
from georama.integration.models import Datasource, Project, Vector
from tests.api.common import perm

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
        project=QslProject(version="3.44", name="Broken project"),
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


@pytest.fixture
def rivers_export():
    return Config(
        project=QslProject(version="3.44", name="Rivers project"),
        exporter=Exporter(qgis_version="3.44"),
        meta_data=MetaData(service=Service(contact_organization=None, contact_mail=None)),
        tree=Tree(
            members=[
                TreeGroup(id="", name="", is_checked=True, children=["rivers"], is_expanded=True)
            ]
        ),
        datasets=Datasets(
            vector=[
                QslVector(
                    id="rivers",
                    name="rivers",
                    title="Rivers",
                    is_checked=True,
                    source=DataSource(ogr=OgrSource(path="rivers.gpkg")),
                    driver="ogr",
                    bbox=BBox.from_string("2457000,1075000,2862000,1296000"),
                    bbox_wgs84=BBox.from_string("5.9,45.8,10.5,47.8"),
                    crs=Crs(auth_id="EPSG:2056", postgis_srid=2056, axis_inverted=False),
                )
            ]
        ),
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


@pytest.mark.django_db
@pytest.mark.parametrize("htmx", [False, True])
def test_bulk_delete_confirmation(organisation, organisation_admin_client, htmx):
    deleted = ProjectFactory.create(organisation=organisation, name="bulk-match-delete")
    also_deleted = ProjectFactory.create(organisation=organisation, name="bulk-match-delete-too")
    datasource = VectorFactory.create(project=deleted, name="bulk-related-datasource", fields=[])
    remaining = ProjectFactory.create(organisation=organisation, name="bulk-match-keep")
    ProjectFactory.create(organisation=organisation, name="bulk-match-next")
    ProjectFactory.create(organisation=organisation, name="bulk-other")
    path = "/integration/manage/projects"
    params = "?search=bulk-match&ordering=name&limit=1"
    headers = {"HTTP_HX_REQUEST": "true"} if htmx else {}

    list_response = organisation_admin_client.get(
        path + params, SERVER_NAME=server_name(organisation), **headers
    )
    payload = {"action": "delete", "ids": [str(deleted.pk), str(also_deleted.pk)]}
    confirmation = organisation_admin_client.post(
        f"{path}/bulk_confirm{params}",
        payload,
        SERVER_NAME=server_name(organisation),
    )

    assert confirmation.status_code == status.HTTP_200_OK
    content = confirmation.content.decode()
    assert "bulk-match-delete" in content
    assert "bulk-related-datasource" in content
    assert "bulk-match-keep" not in content
    assert "Confirm deletion" in content
    assert "btn-outline-danger" in content
    assert 'type="hidden" name="action" value="delete"' in content
    for pk in payload["ids"]:
        assert f'type="hidden" name="ids" value="{pk}"' in content
    assert f'action="{path}/bulk"' in content
    assert f'href="{path}"' in content
    assert Project.objects.filter(pk__in=payload["ids"]).count() == 2
    assert Vector.objects.filter(pk=datasource.pk).exists()

    response = organisation_admin_client.post(
        f"{path}/bulk{params}",
        confirmation.data["bulk_action"],
        SERVER_NAME=server_name(organisation),
    )
    assert response.status_code == status.HTTP_302_FOUND
    assert response["Location"] == path
    assert "HX-Trigger" not in response
    assert not Project.objects.filter(pk__in=payload["ids"]).exists()
    assert not Vector.objects.filter(pk=datasource.pk).exists()

    response = organisation_admin_client.get(
        path + params, SERVER_NAME=server_name(organisation), **headers
    )
    assert response.status_code == status.HTTP_200_OK
    assert "Location" not in response
    assert response.template_name == (
        "core/drf/default/partials/list.html" if htmx else "core/drf/default/list.html"
    )
    content = response.content.decode()
    assert "bulk-match-keep" in content
    assert str(remaining.pk) in content
    assert "bulk-match-delete" not in content
    assert "bulk-other" not in content
    assert 'id="bulk-action-delete"' in content
    assert "bulkListUpdated" not in content
    assert f'hx-get="{path}?' in content
    assert f'hx-get="{path}/bulk' not in content
    assert f"{path}?" in response.data["next_url"]
    assert "/bulk/" not in response.data["next_url"]
    assert "offset=1" in response.data["next_url"]
    assert f'action="{path}/bulk_confirm"' in list_response.content.decode()


@pytest.mark.django_db
def test_bulk_make_public_confirmation(
    organisation, organisation_admin_client, organisation_vector
):
    field = FieldFactory.create(datasource=organisation_vector, name="bulk-related-field")
    selected = FeatureLayerFactory.create(
        datasource=organisation_vector, public=False, metadata__title="bulk-public-selected"
    )
    untouched = FeatureLayerFactory.create(
        datasource=organisation_vector, public=False, metadata__title="bulk-public-untouched"
    )
    path = "/features/manage/feature_layers"
    payload = {"action": "make-public", "ids": [str(selected.pk)]}

    confirmation = organisation_admin_client.post(
        f"{path}/bulk_confirm", payload, SERVER_NAME=server_name(organisation)
    )

    assert confirmation.status_code == status.HTTP_200_OK
    content = confirmation.content.decode()
    assert "Confirm making public" in content
    assert "publicly accessible" in content
    assert "btn-outline-warning" in content
    assert "bulk-public-selected" in content
    assert "bulk-public-untouched" not in content
    assert "bulk-related-field" not in content
    assert "Confirm deletion" not in content
    assert 'name="action" value="make-public"' in content
    assert confirmation.data["related_objects"] == [selected]
    assert not confirmation.data["protected"]
    selected.refresh_from_db()
    assert not selected.public

    response = organisation_admin_client.post(
        f"{path}/bulk", confirmation.data["bulk_action"], SERVER_NAME=server_name(organisation)
    )

    assert response.status_code == status.HTTP_302_FOUND
    assert response["Location"] == path
    selected.refresh_from_db()
    untouched.refresh_from_db()
    assert selected.public
    assert not untouched.public
    assert FeatureLayer.objects.filter(pk__in=[selected.pk, untouched.pk]).count() == 2
    assert selected.fields.filter(datasource_field=field).exists()


@pytest.mark.django_db
@pytest.mark.parametrize("endpoint", ["bulk_confirm", "bulk"])
@pytest.mark.parametrize(
    "action,required_permission", [("delete", "delete"), ("make-public", "change")]
)
@pytest.mark.parametrize("granted_permission", [None, "add", "change", "delete"])
def test_bulk_requires_action_permission(
    organisation,
    organisation_vector,
    user,
    endpoint,
    action,
    required_permission,
    granted_permission,
):
    organisation.public_access = True
    organisation.save(update_fields=["public_access"])
    selected = FeatureLayerFactory.create(datasource=organisation_vector, public=False)
    client = APIClient()
    if granted_permission:
        user.user_permissions.add(perm(FeatureLayer, granted_permission))
        client.force_login(user)

    response = client.post(
        f"/features/manage/feature_layers/{endpoint}",
        {"action": action, "ids": [str(selected.pk)]},
        SERVER_NAME=server_name(organisation),
    )

    allowed = granted_permission == required_permission
    expected_status = status.HTTP_403_FORBIDDEN
    if allowed:
        expected_status = (
            status.HTTP_200_OK if endpoint == "bulk_confirm" else status.HTTP_302_FOUND
        )
    assert response.status_code == expected_status
    deleted = allowed and endpoint == "bulk" and action == "delete"
    assert FeatureLayer.objects.filter(pk=selected.pk).exists() is not deleted
    if not deleted:
        selected.refresh_from_db()
        assert selected.public is (allowed and endpoint == "bulk" and action == "make-public")


@pytest.mark.django_db
@pytest.mark.parametrize("endpoint", ["bulk_confirm", "bulk"])
def test_bulk_rejects_invalid_action(
    organisation, organisation_admin_client, organisation_project, endpoint
):
    response = organisation_admin_client.post(
        f"/integration/manage/projects/{endpoint}?search=example",
        {"action": "unknown", "ids": [str(organisation_project.pk)]},
        SERVER_NAME=server_name(organisation),
    )

    assert response.status_code == status.HTTP_302_FOUND
    assert response["Location"] == "/integration/manage/projects"
    assert Project.objects.filter(pk=organisation_project.pk).exists()


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
            "/integration/manage/projects/non_integrated",
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
            "/integration/manage/projects/non_integrated",
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
            f"/integration/manage/projects/{organisation_project.pk}/ashow",
            SERVER_NAME=server_name(organisation),
        )
        content = response.text

        assert response.status_code == status.HTTP_200_OK
        assert "Empty layer" in content
        assert "The layer is empty." in content
        assert "empty-layer" in content


class TestPreviewFailureDuringIntegration:
    @pytest.mark.django_db
    def test_integration_finishes_with_warnings(
        self,
        monkeypatch,
        posted_jobs,
        failed_render_job_result,
        organisation,
        organisation_admin_client,
        non_integrated_project_file,
        rivers_export,
    ):
        mock_export_result(
            monkeypatch,
            ExportResult(successful=True, content=JsonSerializer().render(rivers_export)),
        )
        # QSL fails on every rendering, the datasource preview as the project preview
        posted_jobs.answer = failed_render_job_result

        response = organisation_admin_client.post(
            "/integration/manage/projects/non_integrated",
            {"path": non_integrated_project_file.name},
            SERVER_NAME=server_name(organisation),
        )

        # a missing preview does not stop the integration, we land on the project
        assert response.status_code == status.HTTP_302_FOUND
        assert len(posted_jobs) == 2
        rivers = Datasource.objects.get(qgis_layer_id="rivers")
        assert rivers.project.name == "Rivers project"
        assert not rivers.preview
        assert not rivers.project.preview
        # the user is told which previews are missing
        assert [str(message) for message in get_messages(response.wsgi_request)] == [
            "The preview of 'Rivers' could not be generated.",
            "The preview of 'Rivers project' could not be generated.",
            "The project was successfully integrated.",
        ]
