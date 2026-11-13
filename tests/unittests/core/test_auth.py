import logging
from types import SimpleNamespace

import pytest
from django.test import Client
from django.urls import reverse
from rest_framework import status

from georama.core.adapters import SocialAccountAdapter
from georama.core.common.login_attempts import LoginAttempts


@pytest.fixture
def keycloak_provider():
    yield {
        "openid_connect": {
            "APPS": [
                {
                    "provider_id": "keycloak",
                    "name": "Keycloak",
                    "client_id": "georama-oidc",
                    "secret": "secret",
                    "settings": {
                        "server_url": "http://keycloak:7080/realms/ninjas/.well-known/openid-configuration"
                    },
                }
            ]
        }
    }


class TestLogin:
    @pytest.mark.django_db
    def test_local_form_and_provider_button_are_shown_when_enabled(
        self, settings, keycloak_provider
    ):
        # the default: the local form is enabled and keycloak is configured
        settings.LOGIN_LOCAL_FORM_ENABLED = True
        settings.SOCIALACCOUNT_PROVIDERS = keycloak_provider
        response = Client().get(reverse("core:login"), SERVER_NAME="localhost")
        assert response.status_code == status.HTTP_200_OK
        # we expect the local form ...
        assert 'name="password"' in response.text
        # ... and the button of the provider with the openid icon, a small POST form
        assert 'action="/accounts/oidc/keycloak/login/' in response.text
        assert '<i class="fa-brands fa-openid me-2"></i>Keycloak' in response.text

    @pytest.mark.django_db
    def test_only_provider_button_is_shown_when_disabled(self, settings, keycloak_provider):
        settings.LOGIN_LOCAL_FORM_ENABLED = False
        settings.SOCIALACCOUNT_PROVIDERS = keycloak_provider
        response = Client().get(reverse("core:login"), SERVER_NAME="localhost")
        assert response.status_code == status.HTTP_200_OK
        # the local form is gone, only the provider button is left
        assert 'name="password"' not in response.text
        assert 'action="/accounts/oidc/keycloak/login/' in response.text

    @pytest.mark.parametrize("login_local_form_enabled", [True, False])
    @pytest.mark.django_db
    def test_local_form_is_shown_without_provider(self, settings, login_local_form_enabled):
        # without any provider the local form is the only way in, so it's shown whatever
        # the setting says
        settings.LOGIN_LOCAL_FORM_ENABLED = login_local_form_enabled
        settings.SOCIALACCOUNT_PROVIDERS = {}
        response = Client().get(reverse("core:login"), SERVER_NAME="localhost")
        assert response.status_code == status.HTTP_200_OK
        assert 'name="password"' in response.text
        assert "/accounts/oidc/" not in response.text

    @pytest.mark.django_db
    def test_provider_button_keeps_next(self, settings, keycloak_provider):
        settings.LOGIN_LOCAL_FORM_ENABLED = False
        settings.SOCIALACCOUNT_PROVIDERS = keycloak_provider
        # the user was sent to the login page from the maps page
        response = Client().get(f"{reverse('core:login')}?next=/maps/", SERVER_NAME="localhost")
        # we expect the button to bring the user back there after the provider login
        assert "next=%2Fmaps%2F" in response.text

    @pytest.mark.django_db
    def test_post_is_not_allowed_when_local_form_is_hidden(
        self, settings, keycloak_provider, user, user_user_name, user_password
    ):
        settings.LOGIN_LOCAL_FORM_ENABLED = False
        settings.SOCIALACCOUNT_PROVIDERS = keycloak_provider
        client = Client()
        # a valid user tries to sign in with the hidden form anyway
        response = client.post(
            reverse("core:login"),
            {"username": user_user_name, "password": user_password},
            SERVER_NAME="localhost",
        )
        # the setting really disables the local login, it doesn't only hide it
        assert response.status_code == status.HTTP_405_METHOD_NOT_ALLOWED
        assert response.headers["Allow"] == "GET"
        assert "_auth_user_id" not in client.session

    @pytest.mark.parametrize("login_local_form_enabled", [True, False])
    @pytest.mark.django_db
    def test_post_logs_in_without_provider(
        self, settings, login_local_form_enabled, user, user_user_name, user_password
    ):
        # without provider the form is the fallback, so it has to work as well
        settings.LOGIN_LOCAL_FORM_ENABLED = login_local_form_enabled
        settings.SOCIALACCOUNT_PROVIDERS = {}
        client = Client()
        response = client.post(
            reverse("core:login"),
            {"username": user_user_name, "password": user_password},
            SERVER_NAME="localhost",
        )
        assert response.status_code == status.HTTP_302_FOUND
        assert client.session["_auth_user_id"] == str(user.pk)


class TestAdminLogin:
    @pytest.mark.django_db
    def test_redirects_to_login_page_when_local_form_is_hidden(self, settings, keycloak_provider):
        settings.LOGIN_LOCAL_FORM_ENABLED = False
        settings.SOCIALACCOUNT_PROVIDERS = keycloak_provider
        # an admin wants to open the user list and is sent to the admin login first
        response = Client().get("/admin/login/?next=/admin/core/user/", SERVER_NAME="localhost")
        # the admin password form is no way around the hidden local form, the admin
        # ends up on the login page of georama and keeps the way back to the user list
        assert response.status_code == status.HTTP_302_FOUND
        assert response.headers["Location"] == "/login/?next=/admin/core/user/"

    @pytest.mark.parametrize("login_local_form_enabled", [True, False])
    @pytest.mark.django_db
    def test_admin_form_is_shown_without_provider(self, settings, login_local_form_enabled):
        # without any provider the admin form stays, otherwise nobody gets in anymore
        settings.LOGIN_LOCAL_FORM_ENABLED = login_local_form_enabled
        settings.SOCIALACCOUNT_PROVIDERS = {}
        response = Client().get("/admin/login/", SERVER_NAME="localhost")
        assert response.status_code == status.HTTP_200_OK
        assert 'name="password"' in response.text


class TestLoginAttemptsOnLoginPages:
    """The counting itself is tested with `LoginAttempts`, here only that both pages
    which accept a password use it.
    """

    @pytest.mark.parametrize("path", ["/login/", "/admin/login/"])
    @pytest.mark.django_db
    def test_failed_login_is_counted(self, settings, rf, user, user_user_name, path):
        settings.LOGIN_ATTEMPTS_RATE = "1/300s/key"
        Client().post(
            path, {"username": user_user_name, "password": "wrong-guess"}, SERVER_NAME="localhost"
        )
        # one failure reaches the limit of one
        assert LoginAttempts.blocked(rf.get("/", SERVER_NAME="localhost"), user_user_name)

    @pytest.mark.parametrize("path", ["/login/", "/admin/login/"])
    @pytest.mark.django_db
    def test_blocked_username_gets_the_429_page(
        self, settings, rf, user, user_user_name, user_password, path
    ):
        settings.LOGIN_ATTEMPTS_RATE = "1/300s/key"
        LoginAttempts.count_failure(rf.get("/", SERVER_NAME="localhost"), user_user_name)
        client = Client()
        # even the right password is refused, with the page in georama's look
        response = client.post(
            path, {"username": user_user_name, "password": user_password}, SERVER_NAME="localhost"
        )
        assert response.status_code == status.HTTP_429_TOO_MANY_REQUESTS
        assert "429.html" in [used.name for used in response.templates]
        assert "_auth_user_id" not in client.session


class TestProviderLogin:
    @pytest.mark.django_db
    def test_provider_button_sends_the_csrf_token(self, settings, keycloak_provider):
        settings.LOGIN_LOCAL_FORM_ENABLED = False
        settings.SOCIALACCOUNT_PROVIDERS = keycloak_provider
        response = Client().get(reverse("core:login"), SERVER_NAME="localhost")
        # only georama's own pages can start the login at the provider
        assert 'method="post" action="/accounts/oidc/keycloak/login/' in response.text
        assert 'name="csrfmiddlewaretoken"' in response.text

    @pytest.mark.django_db
    def test_link_to_the_provider_asks_before_going_there(self, settings, keycloak_provider):
        settings.SOCIALACCOUNT_PROVIDERS = keycloak_provider
        # an old bookmark or a link on a foreign page opens the provider login with GET
        response = Client().get("/accounts/oidc/keycloak/login/", SERVER_NAME="localhost")
        # no redirect to keycloak, but allauth's page in georama's look with a button
        assert response.status_code == status.HTTP_200_OK
        assert "socialaccount/login.html" in [used.name for used in response.templates]
        assert "core/entrance.html" in [used.name for used in response.templates]
        assert "Sign In Via Keycloak" in response.text


class TestSignup:
    @pytest.mark.parametrize(
        "login_local_signup_enabled, template",
        [
            (False, "account/signup_closed.html"),
            (True, "account/signup.html"),
        ],
    )
    @pytest.mark.django_db
    def test_signup_page_follows_the_setting(self, settings, login_local_signup_enabled, template):
        settings.LOGIN_LOCAL_SIGNUP_ENABLED = login_local_signup_enabled
        response = Client().get(reverse("account_signup"), SERVER_NAME="localhost")
        # allauth shows its "closed" page instead of the form as long as signup is off
        assert response.status_code == status.HTTP_200_OK
        assert template in [used.name for used in response.templates]

    @pytest.mark.django_db
    def test_signup_page_leads_to_georamas_login(self, settings):
        settings.LOGIN_LOCAL_SIGNUP_ENABLED = True
        response = Client().get(reverse("account_signup"), SERVER_NAME="localhost")
        # georama's look, and the way back goes to georama's login, not allauth's
        assert "core/entrance.html" in [used.name for used in response.templates]
        assert f'<a href="{reverse("core:login")}">' in response.text

    def test_identity_provider_can_still_create_users(self, settings, rf):
        settings.LOGIN_LOCAL_SIGNUP_ENABLED = False
        # with local signup closed, the first login through keycloak must still create
        # the user, the identity provider decides who gets in
        assert SocialAccountAdapter().is_open_for_signup(rf.get("/"), sociallogin=None)


class TestProviderSignup:
    @pytest.mark.parametrize(
        "provider_email,logged",
        [
            # a local account uses the email already, allauth sends the user to the
            # signup form, the operator needs to know why
            ("limu@example.org", True),
            # a new email, allauth creates the user right away, nothing to tell
            ("someone.else@example.org", False),
        ],
    )
    @pytest.mark.django_db
    def test_email_conflict_is_logged(self, rf, caplog, user, provider_email, logged):
        # the first login of keycloak's user f3c1, as allauth hands it to the adapter
        sociallogin = SimpleNamespace(
            account=SimpleNamespace(provider="keycloak", uid="f3c1"),
            email_addresses=[SimpleNamespace(email=provider_email)],
        )
        with caplog.at_level(logging.WARNING, logger="georama.core.adapters"):
            SocialAccountAdapter().is_auto_signup_allowed(rf.get("/"), sociallogin)
        assert ("a local account already uses this email" in caplog.text) is logged
