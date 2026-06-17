import pytest
from django.test import Client, RequestFactory

from georama.core.middleware.organisation import OrganisationMiddleware


class TestOrganisationMiddleware:
    @pytest.mark.django_db
    def test_organisation_global_request_attribute(self):
        def mock_get_response(request):
            return request

        rf = RequestFactory()
        request = rf.get("", SERVER_NAME="localhost")
        middleware = OrganisationMiddleware(mock_get_response)
        middleware(request)
        assert hasattr(request, "georama_organisation")
        assert request.georama_organisation is None

    @pytest.mark.django_db
    def test_organisation_request_attribute(self, organisation_public_access):
        def mock_get_response(request):
            return request

        rf = RequestFactory()
        request = rf.get("", SERVER_NAME=f"{organisation_public_access.domain}.localhost")
        middleware = OrganisationMiddleware(mock_get_response)
        middleware(request)
        assert hasattr(request, "georama_organisation")
        assert request.georama_organisation == organisation_public_access

    @pytest.mark.django_db
    def test_organisation_global_exists(self):
        client = Client()
        response = client.get("", SERVER_NAME="localhost")
        assert response.status_code == 200

    @pytest.mark.django_db
    def test_organisation_does_not_exists(self):
        client = Client()
        response = client.get("", SERVER_NAME="org.localhost")
        assert response.status_code == 404

    @pytest.mark.django_db
    def test_organisation_exists(self, organisation_public_access):
        client = Client()
        response = client.get("", SERVER_NAME=f"{organisation_public_access.domain}.localhost")
        assert response.status_code == 200

    @pytest.mark.parametrize(
        "value,expected",
        [
            ("www.localhost", "localhost"),
            ("www.localhost:4242", "localhost:4242"),
            ("www.example.com", "example.com"),
            ("www.test.example.com", "test.example.com"),
            ("www.sub.test.example.com", "sub.test.example.com"),
        ],
    )
    def test_middleware_remove_www(self, value, expected):
        assert OrganisationMiddleware.remove_www(value) == expected

    @pytest.mark.parametrize(
        "domain,hostname,expected",
        [
            ("localhost", "localhost", None),
            ("localhost", "localhost:4242", None),
            ("localhost", "test.localhost:4242", "test"),
            ("example.com", "example.com", None),
            ("example.com", "test.example.com", "test"),
            ("example.com", "sub.test.example.com", "sub.test"),
        ],
    )
    def test_middleware_derive_subdomain(self, domain, hostname, expected):
        assert OrganisationMiddleware.derive_subdomain(hostname, domain) == expected
