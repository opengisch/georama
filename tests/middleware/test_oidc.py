import logging

import pytest
import requests
from allauth.socialaccount.models import SocialAccount
from django.contrib.auth import get_user_model
from django.contrib.auth.models import AnonymousUser
from django.contrib.sessions.backends.db import SessionStore
from django.core.exceptions import ImproperlyConfigured
from django.http import HttpResponse
from django.test import RequestFactory

from georama.core.middleware.oidc import GeoGirafeAuthenticationMiddleware


@pytest.fixture
def keycloak(settings):
    settings.OIDC_SERVER_URL = "http://keycloak:7080/realms/ninjas/.well-known/openid-configuration"
    settings.OIDC_PROVIDER_ID = "keycloak"
    yield settings.OIDC_SERVER_URL


@pytest.fixture
def token_payload():
    # what keycloak puts into the token of fred, already decoded and verified
    yield {
        "sub": "f3c1e0a2-fred",
        "preferred_username": "fred.flintstone",
        "email": "fred.flintstone@example.org",
        "given_name": "Fred",
        "family_name": "Flintstone",
    }


@pytest.fixture
def middleware(keycloak, token_payload, monkeypatch):
    middleware = GeoGirafeAuthenticationMiddleware(lambda _: HttpResponse("hello"))
    # the provider is reachable and the token is valid, how that is checked is jwt's
    # business and not part of these tests
    monkeypatch.setattr(middleware, "load_provider", lambda: True)
    monkeypatch.setattr(middleware, "verify_token", lambda token: token_payload)
    yield middleware


@pytest.fixture
def bearer_request():
    request = RequestFactory().get("/", HTTP_AUTHORIZATION="Bearer a.token.of-geogirafe")
    request.user = AnonymousUser()
    request.session = SessionStore()
    yield request


@pytest.fixture
def fred(token_payload):
    # fred signed in through keycloak before, so his provider account exists
    fred = get_user_model().objects.create(username="fred.flintstone")
    SocialAccount.objects.create(user=fred, provider="keycloak", uid=token_payload["sub"])
    yield fred
    fred.delete()


class TestProviderAvailability:
    def test_nothing_is_fetched_at_start(self, keycloak, monkeypatch):
        # georama must start even when the provider is down
        monkeypatch.setattr(
            requests, "get", lambda *args, **kwargs: pytest.fail("fetched at start")
        )
        GeoGirafeAuthenticationMiddleware(lambda _: HttpResponse("hello"))

    @pytest.mark.django_db
    def test_unreachable_provider_is_asked_again_only_after_a_while(
        self, settings, keycloak, bearer_request, caplog, monkeypatch
    ):
        settings.OIDC_TIMEOUT_SECONDS = 2
        settings.OIDC_RETRY_SECONDS = 60
        timeouts = []

        def provider_down(url, timeout):
            timeouts.append(timeout)
            raise requests.ConnectionError("no route to host")

        monkeypatch.setattr(requests, "get", provider_down)
        middleware = GeoGirafeAuthenticationMiddleware(lambda _: HttpResponse("hello"))

        with caplog.at_level(logging.WARNING, logger="georama.core.middleware.oidc"):
            response = middleware(bearer_request)
        # the request goes on as anonymous, the operator finds the reason in the log
        assert response.text == "hello"
        assert bearer_request.user.is_anonymous
        assert "bearer tokens are refused for the next 60 seconds" in caplog.text

        # the next request doesn't wait for the provider again
        middleware(bearer_request)
        assert timeouts == [2]


class TestTokenUser:
    @pytest.mark.django_db
    def test_user_is_set_for_the_request_only(self, middleware, bearer_request, fred):
        middleware(bearer_request)
        assert bearer_request.user == fred
        # no session: the next request brings its token again
        assert "_auth_user_id" not in bearer_request.session

    @pytest.mark.django_db
    def test_deactivated_user_is_refused(self, middleware, bearer_request, fred):
        fred.is_active = False
        fred.save()
        middleware(bearer_request)
        assert bearer_request.user.is_anonymous

    @pytest.mark.parametrize("geogirafe_superuser_enabled", [True, False])
    @pytest.mark.django_db
    def test_superuser_follows_the_setting(
        self, settings, middleware, bearer_request, fred, geogirafe_superuser_enabled
    ):
        settings.GEOGIRAFE_SUPERUSER_ENABLED = geogirafe_superuser_enabled
        fred.is_superuser = True
        fred.save()
        middleware(bearer_request)
        assert (bearer_request.user == fred) is geogirafe_superuser_enabled

    @pytest.mark.django_db
    def test_unknown_user_is_created(self, middleware, bearer_request, token_payload):
        middleware(bearer_request)
        # fred never signed in before, the token brings him in
        created = get_user_model().objects.get(socialaccount__uid=token_payload["sub"])
        assert bearer_request.user == created
        assert created.username == "fred.flintstone"
        assert created.email == "fred.flintstone@example.org"


class TestUsernameConflict:
    @pytest.fixture
    def local_fred(self):
        # a local account with fred's username exists, created in georama long ago
        local_fred = get_user_model().objects.create(username="fred.flintstone")
        yield local_fred
        local_fred.delete()

    @pytest.mark.django_db
    def test_suffix_creates_a_new_user(
        self, settings, middleware, bearer_request, local_fred, token_payload
    ):
        settings.OIDC_USERNAME_CONFLICT = "suffix"
        middleware(bearer_request)
        # the token gets its own account, the local one stays untouched
        assert bearer_request.user != local_fred
        assert bearer_request.user.username.startswith("fred.flintstone")
        assert not local_fred.socialaccount_set.exists()

    @pytest.mark.django_db
    def test_connect_links_the_local_account(
        self, settings, middleware, bearer_request, local_fred, token_payload
    ):
        settings.OIDC_USERNAME_CONFLICT = "connect"
        middleware(bearer_request)
        # the provider's username is trusted, the token signs in the local account
        assert bearer_request.user == local_fred
        assert local_fred.socialaccount_set.get().uid == token_payload["sub"]

    def test_unknown_mode_stops_georama(self, settings, keycloak):
        settings.OIDC_USERNAME_CONFLICT = "merge"
        with pytest.raises(ImproperlyConfigured, match="suffix, connect"):
            GeoGirafeAuthenticationMiddleware(lambda _: HttpResponse("hello"))
