import pytest
from django.conf import settings
from django.test import Client, RequestFactory
from django.urls import reverse
from rest_framework import status

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

    @pytest.mark.django_db
    def test_middleware_redirects_unauthenticated_user_on_non_public_organisation(
        self, organisation_non_public_access
    ):
        client = Client()
        response = client.get("", SERVER_NAME=f"{organisation_non_public_access.domain}.localhost")
        assert response.status_code == status.HTTP_302_FOUND
        assert response.headers["Location"] == reverse(
            settings.ORGANISATION_NOT_AUTHENTICATED_TARGET
        )

    @pytest.mark.django_db
    def test_middleware_denies_access_authenticated_non_member_user_on_non_public_organisation(
        self,
        organisation_non_public_access,
        user,
        user_user_name,
        user_password,
    ):
        client = Client()
        client.login(username=user_user_name, password=user_password)
        response = client.get("", SERVER_NAME=f"{organisation_non_public_access.domain}.localhost")
        assert response.status_code == status.HTTP_403_FORBIDDEN

    @pytest.mark.django_db
    def test_middleware_allows_access_authenticated_member_user_on_non_public_organisation(
        self,
        organisation_non_public_access,
        user_with_dedicated_membership_non_public,
        user_user_name,
        user_password,
    ):
        client = Client()
        client.login(username=user_user_name, password=user_password)
        response = client.get("", SERVER_NAME=f"{organisation_non_public_access.domain}.localhost")
        assert response.status_code == status.HTTP_200_OK

    @pytest.mark.django_db
    def test_middleware_allows_access_superuser_on_all_organisations(
        self,
        admin_user,
        admin_user_name,
        admin_password,
        organisation_public_access,
        organisation_non_public_access,
    ):
        client = Client()
        client.login(username=admin_user_name, password=admin_password)
        response = client.get("", SERVER_NAME="localhost")
        assert response.status_code == status.HTTP_200_OK
        response = client.get("", SERVER_NAME=f"{organisation_public_access.domain}.localhost")
        assert response.status_code == status.HTTP_200_OK
        response = client.get("", SERVER_NAME=f"{organisation_non_public_access.domain}.localhost")
        assert response.status_code == status.HTTP_200_OK

    @pytest.mark.django_db
    def test_middleware_allows_access_unauthenticated_user_to_public_organisation(
        self,
        organisation_public_access,
    ):
        client = Client()
        response = client.get("", SERVER_NAME=f"{organisation_public_access.domain}.localhost")
        assert response.status_code == status.HTTP_200_OK

    @pytest.mark.django_db
    def test_middleware_allows_everyone_access_configured_not_authenticated_target(
        self,
        organisation_public_access,
        organisation_non_public_access,
    ):
        path = reverse(settings.ORGANISATION_NOT_AUTHENTICATED_TARGET)
        client = Client()
        response = client.get(path, SERVER_NAME="localhost")
        assert response.status_code == status.HTTP_200_OK
        response = client.get(path, SERVER_NAME=f"{organisation_public_access.domain}.localhost")
        assert response.status_code == status.HTTP_200_OK
        response = client.get(
            path, SERVER_NAME=f"{organisation_non_public_access.domain}.localhost"
        )
        assert response.status_code == status.HTTP_200_OK

    @pytest.mark.django_db
    def test_middleware_allows_everyone_access_configured_bypass(
        self,
        organisation_public_access,
        organisation_non_public_access,
    ):
        accessible_view_name = "core:index"
        settings.ORGANISATION_GLOBAL_PUBLIC_ACCESS_BYPASS_TARGETS = [
            accessible_view_name,
        ]
        path = reverse(accessible_view_name)
        client = Client()
        response = client.get(path, SERVER_NAME="localhost")
        assert response.status_code == status.HTTP_200_OK
        response = client.get(path, SERVER_NAME=f"{organisation_public_access.domain}.localhost")
        assert response.status_code == status.HTTP_200_OK
        response = client.get(
            path, SERVER_NAME=f"{organisation_non_public_access.domain}.localhost"
        )
        assert response.status_code == status.HTTP_200_OK
