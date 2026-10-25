import pytest
from rest_framework import status
from rest_framework.test import APIClient

from georama.webgis.models import UrlShortener

WEBGISURL = "https://webgis.example.org/"


@pytest.fixture
def webgis_url(settings):
    settings.WEBGISURL = WEBGISURL
    yield WEBGISURL


@pytest.fixture
def csrf_enforcing_client():
    """GeoGirafe is a separate application and never sends a CSRF token."""
    yield APIClient(enforce_csrf_checks=True)


class TestUrlShortenerCreate:
    path = "/webgis/short"

    @pytest.mark.django_db
    def test_anonymous_without_csrf_token(self, csrf_enforcing_client, webgis_url):
        response = csrf_enforcing_client.post(
            self.path, {"url": f"{webgis_url}?map_x=1"}, SERVER_NAME="localhost"
        )
        assert response.status_code == status.HTTP_201_CREATED
        assert UrlShortener.objects.filter(url=f"{webgis_url}?map_x=1").exists()

    @pytest.mark.django_db
    def test_logged_in_user_without_csrf_token(
        self, csrf_enforcing_client, webgis_url, user, user_user_name, user_password
    ):
        csrf_enforcing_client.login(username=user_user_name, password=user_password)
        response = csrf_enforcing_client.post(
            self.path, {"url": f"{webgis_url}?map_x=1"}, SERVER_NAME="localhost"
        )
        assert response.status_code == status.HTTP_201_CREATED
        assert UrlShortener.objects.filter(url=f"{webgis_url}?map_x=1").exists()

    @pytest.mark.django_db
    def test_returns_short_url(self, csrf_enforcing_client, webgis_url):
        response = csrf_enforcing_client.post(
            self.path, {"url": webgis_url}, SERVER_NAME="localhost"
        )
        short = UrlShortener.objects.get(url=webgis_url)
        assert response.json() == {"short_url": f"{self.path}/{short.id}"}

    @pytest.mark.django_db
    def test_rejects_foreign_url(self, csrf_enforcing_client, webgis_url):
        response = csrf_enforcing_client.post(
            self.path, {"url": "https://evil.example.org/"}, SERVER_NAME="localhost"
        )
        assert response.status_code == status.HTTP_400_BAD_REQUEST
        assert not UrlShortener.objects.exists()


class TestUrlShortenerRetrieve:
    @pytest.mark.django_db
    def test_returns_long_url(self, csrf_enforcing_client, webgis_url):
        UrlShortener.objects.create(id="abc123", url=webgis_url)
        response = csrf_enforcing_client.get("/webgis/short/abc123", SERVER_NAME="localhost")
        assert response.status_code == status.HTTP_200_OK
        assert response.json() == {"long_url": webgis_url}
