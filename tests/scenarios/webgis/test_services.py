import pytest


class TestWebGisOgcService:
    """Test basic endpoint availability for the WebGIS OGC service."""

    @pytest.mark.django_db
    def test_capabilities_wms(self, client):
        response = client.get("/webgis/ows/?SERVICE=WMS&REQUEST=GETCAPABILITIES")
        assert response.status_code == 200

    @pytest.mark.django_db
    def test_capabilities_wfs(self, client):
        response = client.get("/webgis/ows/?SERVICE=WFS&REQUEST=GETCAPABILITIES")
        assert response.status_code == 200

    @pytest.mark.django_db
    def test_ows_without_trailing_slash_wms(self, client):
        response = client.get("/webgis/ows?SERVICE=WMS&REQUEST=GETCAPABILITIES")
        assert response.status_code == 200

    @pytest.mark.django_db
    def test_ows_without_trailing_slash_wfs(self, client):
        response = client.get("/webgis/ows?SERVICE=WFS&REQUEST=GETCAPABILITIES")
        assert response.status_code == 200
