from unittest.mock import AsyncMock, patch

import pytest
from lxml import etree

from georama.maps.models import PublishedAsWms

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
            "qgis_server_light.interface.dispatcher.RedisQueue.create",
            new_callable=AsyncMock,
        ) as mock_create:
            mock_create.return_value = mock_instance

            client.login(username=admin_user_name, password=admin_password)
            vector_dataset = integrated_project.vector_datasets.get(title="TestPointLayer")

            # Publish layer as WMS
            response = client.get(
                f"/maps/layer/add/vector/{vector_dataset.id}",
                follow=True,
            )

            assert response.status_code == 200
            assert b"TestPointLayer" in response.content
            assert PublishedAsWms.objects.filter(title="TestPointLayer").exists()

            # Get WMS Capabilities document
            url = "/maps/ows?SERVICE=WMS&REQUEST=GETCAPABILITIES&VERSION=1.3.0"
            response = client.get(url)

            assert response.status_code == 200
            assert response["Content-Type"] == "text/xml"

            parser = etree.XMLParser(ns_clean=True)
            root = etree.fromstring(response.content, parser)

            NS = {
                "w": "http://www.opengis.net/wms",
                "x": "http://www.w3.org/1999/xlink",
            }

            def xp(el, path):
                nodes = el.xpath(path, namespaces=NS)
                if isinstance(nodes, list) and len(nodes) == 1:
                    return nodes[0]
                return nodes

            assert root.tag == "{http://www.opengis.net/wms}WMS_Capabilities"
            assert root.attrib["version"] == "1.3.0"

        # Service
        service = xp(root, "./w:Service")
        title = xp(service, "./w:Title/text()")
        abstract = xp(service, "./w:Abstract/text()")
        assert title == "QGIS Server light WMS"
        assert abstract == "This is the new approach."

        # Capability
        capability = xp(root, "./w:Capability")

        request = xp(capability, "./w:Request")
        get_capabilities = xp(request, "./w:GetCapabilities")
        formats = xp(get_capabilities, "./w:Format/text()")
        assert formats == ["text/xml", "application/json"]

        http_get = xp(get_capabilities, "./w:DCPType/w:HTTP/w:Get")
        href = xp(http_get, "./w:OnlineResource/@x:href")
        assert href == "http://testserver/maps/ows?"

        # Layers
        layers = xp(capability, "./w:Layer")
        name = xp(layers, "./w:Name/text()")
        title = xp(layers, "./w:Title/text()")
        abstract = xp(layers, "./w:Abstract/text()")

        assert name == "qgis_server_light"
        assert title == "QGIS Server light"
        assert abstract == "The lightning fast and scalable access to your raster data."

        layer = xp(layers, "./w:Layer")
        assert xp(layer, "./w:Title/text()") == "TestPointLayer"
        assert xp(layer, "./w:CRS/text()") == ["EPSG:4326", "CRS:84"]
