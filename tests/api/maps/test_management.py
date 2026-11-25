import pytest
from rest_framework import status
from rest_framework.test import APIClient

from georama.integration.factories import ProjectFactory, VectorFactory
from georama.maps.factories import WmsLayerFactory


@pytest.fixture
def organisation_admin_client(admin_user, admin_user_name, admin_password):
    client = APIClient()
    client.login(username=admin_user_name, password=admin_password)
    yield client


@pytest.fixture
def server_name(organisation):
    yield f"{organisation.domain}.localhost"


@pytest.fixture
def rivers_wms_layer(organisation):
    project = ProjectFactory.create(organisation=organisation)
    datasource = VectorFactory.create(
        project=project, name="rivers", source={"ogr": {"path": "rivers.gpkg"}}, fields=[]
    )
    wms_layer = WmsLayerFactory.create(
        datasource=datasource,
        metadata__title="Rivers",
        extent="2457000,1075000,2862000,1296000",
        preview=b"old preview",
    )
    yield wms_layer
    wms_layer.delete()
    project.delete()


class TestGeneratePreviewImage:
    @pytest.mark.django_db
    def test_preview_is_stored(
        self,
        posted_jobs,
        render_job_result,
        organisation_admin_client,
        server_name,
        rivers_wms_layer,
    ):
        posted_jobs.answer = render_job_result

        response = organisation_admin_client.post(
            f"/maps/manage/map_layers/{rivers_wms_layer.pk}/generate_preview_image",
            query_params={"f": "json"},
            SERVER_NAME=server_name,
        )

        assert response.status_code == status.HTTP_201_CREATED
        assert response.json() == {"layer_id": str(rivers_wms_layer.pk)}
        rivers_wms_layer.refresh_from_db()
        assert bytes(rivers_wms_layer.preview) == b"png"

    @pytest.mark.django_db
    def test_failure_is_shown_in_the_gui(
        self,
        posted_jobs,
        failed_render_job_result,
        organisation_admin_client,
        server_name,
        rivers_wms_layer,
    ):
        posted_jobs.answer = failed_render_job_result

        # the button in the list swaps in the preview partial through htmx
        response = organisation_admin_client.post(
            f"/maps/manage/map_layers/{rivers_wms_layer.pk}/generate_preview_image",
            query_params={"f": "html"},
            SERVER_NAME=server_name,
        )

        # the partial still comes back, with the warning as toast next to it
        assert response.status_code == status.HTTP_200_OK
        assert f'id="preview-{rivers_wms_layer.pk}"' in response.text
        assert "The preview of &#x27;Rivers&#x27; could not be generated." in response.text
        # the preview the layer had before survives the failed rendering
        rivers_wms_layer.refresh_from_db()
        assert bytes(rivers_wms_layer.preview) == b"old preview"

    @pytest.mark.django_db
    def test_failure_is_reported_through_the_api(
        self,
        posted_jobs,
        failed_render_job_result,
        organisation_admin_client,
        server_name,
        rivers_wms_layer,
    ):
        posted_jobs.answer = failed_render_job_result

        response = organisation_admin_client.post(
            f"/maps/manage/map_layers/{rivers_wms_layer.pk}/generate_preview_image",
            query_params={"f": "json"},
            SERVER_NAME=server_name,
        )

        # QSL is the upstream which failed, nothing was created
        assert response.status_code == status.HTTP_502_BAD_GATEWAY
        assert response.json() == {"error": "The preview could not be generated."}
        rivers_wms_layer.refresh_from_db()
        assert bytes(rivers_wms_layer.preview) == b"old preview"


class TestGeneratePreviewImageBulk:
    @pytest.mark.django_db
    def test_previews_are_stored(
        self,
        posted_jobs,
        render_job_result,
        organisation_admin_client,
        server_name,
        rivers_wms_layer,
    ):
        posted_jobs.answer = render_job_result

        response = organisation_admin_client.post(
            "/maps/manage/map_layers/generate_preview_image_bulk",
            {"layer_ids": [str(rivers_wms_layer.pk)]},
            format="json",
            SERVER_NAME=server_name,
        )

        assert response.status_code == status.HTTP_201_CREATED
        assert response.json() == {
            "results": [{"layer_id": str(rivers_wms_layer.pk)}],
            "failed": [],
        }
        rivers_wms_layer.refresh_from_db()
        assert bytes(rivers_wms_layer.preview) == b"png"

    @pytest.mark.django_db
    def test_failed_layers_are_reported(
        self,
        posted_jobs,
        failed_render_job_result,
        organisation_admin_client,
        server_name,
        rivers_wms_layer,
    ):
        posted_jobs.answer = failed_render_job_result

        response = organisation_admin_client.post(
            "/maps/manage/map_layers/generate_preview_image_bulk",
            {"layer_ids": [str(rivers_wms_layer.pk)]},
            format="json",
            SERVER_NAME=server_name,
        )

        # the request itself went through, the layer QSL failed on is listed as failed
        assert response.status_code == status.HTTP_201_CREATED
        assert response.json() == {
            "results": [],
            "failed": [{"layer_id": str(rivers_wms_layer.pk)}],
        }
        rivers_wms_layer.refresh_from_db()
        assert bytes(rivers_wms_layer.preview) == b"old preview"
