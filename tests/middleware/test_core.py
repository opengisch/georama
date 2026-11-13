import base64
import logging

import pytest
from django.conf import settings
from django.contrib.auth.models import AnonymousUser
from django.http import HttpResponse
from django.test import Client, RequestFactory
from django.urls import reverse
from rest_framework import status
from rest_framework.request import Request
from rest_framework.settings import api_settings

from georama.core.middleware.basic_auth import BasicAuthenticationMiddleware
from georama.core.middleware.organisation import OrganisationMiddleware


class TestBasicAuthMiddleware:
    @pytest.mark.django_db
    def test_basic_auth_authenticates_user(self, user, user_user_name, user_password):
        credentials = base64.b64encode(f"{user_user_name}:{user_password}".encode()).decode()
        request = RequestFactory().get("/", HTTP_AUTHORIZATION=f"Basic {credentials}")
        request.user = AnonymousUser()
        middleware = BasicAuthenticationMiddleware(lambda _: HttpResponse("hello"))
        response = middleware(request)
        assert response.text == "hello"
        assert request.user == user

    @pytest.mark.django_db
    def test_basic_auth_authenticates_user_access_non_public_organisation(
        self,
        organisation_non_public_access,
        user_with_dedicated_membership_non_public,
        user_user_name,
        user_password,
    ):
        credentials = base64.b64encode(f"{user_user_name}:{user_password}".encode()).decode()
        client = Client()
        response = client.get(
            "",
            SERVER_NAME=f"{organisation_non_public_access.domain}.localhost",
            HTTP_AUTHORIZATION=f"Basic {credentials}",
        )
        assert response.status_code == status.HTTP_200_OK

    @pytest.mark.django_db
    def test_basic_auth_refuses_superuser(self, admin_user, admin_user_name, admin_password):
        middleware = BasicAuthenticationMiddleware(lambda _: HttpResponse("hello"))
        # the superuser sends the right password
        credentials = base64.b64encode(f"{admin_user_name}:{admin_password}".encode()).decode()
        request = RequestFactory().get("/", HTTP_AUTHORIZATION=f"Basic {credentials}")
        request.user = AnonymousUser()
        right_password_response = middleware(request)
        # we expect the superuser is not logged in
        assert right_password_response.status_code == status.HTTP_401_UNAUTHORIZED
        assert request.user.is_anonymous

        # someone guesses the password of the superuser and fails
        credentials = base64.b64encode(f"{admin_user_name}:wrong-guess".encode()).decode()
        request = RequestFactory().get("/", HTTP_AUTHORIZATION=f"Basic {credentials}")
        request.user = AnonymousUser()
        wrong_password_response = middleware(request)
        # both answers are the same, so the guesser can't tell when the password was right
        assert wrong_password_response.status_code == right_password_response.status_code
        assert wrong_password_response.text == right_password_response.text

    @pytest.mark.parametrize(
        "site_title,challenge",
        [
            ("Georama", 'Basic realm="Georama"'),
            # quotes in the title must not end the realm early
            ('My "Geo"', 'Basic realm="My \\"Geo\\""'),
        ],
    )
    @pytest.mark.django_db
    def test_unauthorized_answer_asks_for_credentials(self, settings, site_title, challenge):
        settings.SITE_TITLE = site_title
        middleware = BasicAuthenticationMiddleware(lambda _: HttpResponse("hello"))
        credentials = base64.b64encode(b"nobody:wrong-guess").decode()
        request = RequestFactory().get("/", HTTP_AUTHORIZATION=f"Basic {credentials}")
        request.user = AnonymousUser()
        response = middleware(request)
        # without the challenge browsers and QGIS wouldn't ask for credentials again
        assert response.status_code == status.HTTP_401_UNAUTHORIZED
        assert response.headers["WWW-Authenticate"] == challenge

    @pytest.mark.django_db
    def test_too_many_failed_attempts_block_the_username(
        self, settings, user, user_user_name, user_password
    ):
        # 2 trys, then block for 300s
        settings.LOGIN_ATTEMPTS_RATE = "2/300s/key"
        middleware = BasicAuthenticationMiddleware(lambda _: HttpResponse("hello"))
        wrong = base64.b64encode(f"{user_user_name}:wrong-guess".encode()).decode()
        right = base64.b64encode(f"{user_user_name}:{user_password}".encode()).decode()

        # someone guesses twice and fails
        for _ in range(2):
            request = RequestFactory().get("/", HTTP_AUTHORIZATION=f"Basic {wrong}")
            request.user = AnonymousUser()
            assert middleware(request).status_code == status.HTTP_401_UNAUTHORIZED

        # now even the right password is refused, the password isn't checked anymore
        request = RequestFactory().get("/", HTTP_AUTHORIZATION=f"Basic {right}")
        request.user = AnonymousUser()
        assert middleware(request).status_code == status.HTTP_429_TOO_MANY_REQUESTS
        assert request.user.is_anonymous

    @pytest.mark.django_db
    def test_successful_logins_are_not_counted(self, settings, user, user_user_name, user_password):
        settings.LOGIN_ATTEMPTS_RATE = "2/300s/key"
        middleware = BasicAuthenticationMiddleware(lambda _: HttpResponse("hello"))
        right = base64.b64encode(f"{user_user_name}:{user_password}".encode()).decode()
        # QGIS sends the credentials with every tile, far more often than the limit
        for _ in range(5):
            request = RequestFactory().get("/", HTTP_AUTHORIZATION=f"Basic {right}")
            request.user = AnonymousUser()
            assert middleware(request).status_code == status.HTTP_200_OK

    @pytest.mark.django_db
    def test_superuser_is_counted_like_a_wrong_password(
        self, settings, caplog, admin_user, admin_user_name, admin_password
    ):
        settings.LOGIN_ATTEMPTS_RATE = "2/300s/key"
        middleware = BasicAuthenticationMiddleware(lambda _: HttpResponse("hello"))
        right = base64.b64encode(f"{admin_user_name}:{admin_password}".encode()).decode()
        with caplog.at_level(logging.WARNING, logger="georama.core.middleware.basic_auth"):
            for _ in range(2):
                request = RequestFactory().get("/", HTTP_AUTHORIZATION=f"Basic {right}")
                request.user = AnonymousUser()
                assert middleware(request).status_code == status.HTTP_401_UNAUTHORIZED
        # the operator learns why, the client doesn't
        assert (
            f"Superuser {admin_user_name} tried basic authentication, use a non superuser "
            f"account." in caplog.messages
        )
        # the right password counted like a wrong one, a guesser can't tell the difference
        request = RequestFactory().get("/", HTTP_AUTHORIZATION=f"Basic {right}")
        request.user = AnonymousUser()
        assert middleware(request).status_code == status.HTTP_429_TOO_MANY_REQUESTS

    @pytest.mark.django_db
    def test_rest_framework_takes_the_user_over_without_csrf_token(
        self, user, user_user_name, user_password
    ):
        middleware = BasicAuthenticationMiddleware(lambda _: HttpResponse("hello"))
        credentials = base64.b64encode(f"{user_user_name}:{user_password}".encode()).decode()
        # QGIS writes a feature, it never has a CSRF token
        request = RequestFactory().post("/", HTTP_AUTHORIZATION=f"Basic {credentials}")
        request.user = AnonymousUser()
        middleware(request)
        # the REST framework asks its configured authentication classes in order, the
        # session authentication would refuse the POST for the missing CSRF token
        drf_request = Request(
            request,
            authenticators=[
                authentication() for authentication in api_settings.DEFAULT_AUTHENTICATION_CLASSES
            ],
        )
        assert drf_request.user == user


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
    def test_middleware_allows_everyone_access_admin_login(
        self,
        settings,
        organisation_non_public_access,
    ):
        # the admin login is reachable for everyone, also on organisations which are
        # not public, otherwise nobody could log in there in the first place
        settings.ORGANISATION_GLOBAL_PUBLIC_ACCESS = False
        path = reverse("admin:login")
        client = Client()
        response = client.get(path, SERVER_NAME="localhost")
        assert response.status_code == status.HTTP_200_OK
        response = client.get(
            path, SERVER_NAME=f"{organisation_non_public_access.domain}.localhost"
        )
        assert response.status_code == status.HTTP_200_OK

    @pytest.mark.django_db
    def test_middleware_allows_everyone_access_configured_bypass(
        self,
        settings,
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
