from unittest.mock import AsyncMock, patch, Mock

import pytest

from georama.webgis.models import PublishedAsLayerWms
from django.conf import settings

pytestmark = pytest.mark.django_db


class TestMapsViews:
    def test_publish_as_wms_view(
        self,
        client,
        integrated_project,
        admin_user_name,
        admin_password,
        empty_png_bytes_job_result,
        admin_user,
    ):
        mock_instance = AsyncMock()
        mock_instance.post.return_value = empty_png_bytes_job_result

        with patch(
            "qgis_server_light.interface.dispatcher.redis_asio.RedisQueue.create",
            new_callable=Mock,
        ) as mock_create:
            mock_create.return_value = mock_instance
            client.login(username=admin_user_name, password=admin_password)
            vector_dataset = integrated_project.vector_datasets.get(title="TestPointLayer")

            # Publish layer as WMS
            response = client.get(
                f"/webgis/publish_dataset_as/wms/vector/{vector_dataset.id}",
                follow=True,
            )

            assert response.status_code == 200
            assert b"TestPointLayer" in response.content
            assert PublishedAsLayerWms.objects.filter(title="TestPointLayer").exists()


class TestShortUrlViews:
    def test_shorten_url_create_and_get(self, client):
        url = f"{settings.WEBGISURL}/1234"
        response_create = client.post("/webgis/short/create", data={"url": url})

        assert response_create.status_code == 201, response_create.json()
        payload_create = response_create.json()
        assert "short_url" in payload_create

        short_id = payload_create["short_url"].rstrip("/").split("/")[-1]
        response_get = client.get(f"/webgis/short/get/{short_id}")

        assert response_get.status_code == 200, response_create.json()

        payload_get = response_get.json()
        assert payload_get["long_url"] == url

    def test_shorten_url_requires_webgis_url(self, client):
        response = client.post("/webgis/short/create", data={"url": "https://example.org/foobar"})

        assert response.status_code == 400
        assert response.json()["error"] == "Invalid URL."

    def test_get_long_url_not_found(self, client):
        response = client.get("/webgis/short/get/does-not-exist")

        assert response.status_code == 404
        assert response.json()["error"] == "Not found."
