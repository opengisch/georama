from unittest.mock import AsyncMock, patch, Mock

import pytest

from georama.webgis.models import PublishedAsLayerWms

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
