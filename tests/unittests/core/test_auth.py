import pytest
from django.test import Client
from django.urls import reverse
from rest_framework import status


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
        # ... and the button of the provider with the openid icon
        assert 'href="/accounts/oidc/keycloak/login/' in response.text
        assert '<i class="fa-brands fa-openid me-2"></i>Keycloak' in response.text

    @pytest.mark.django_db
    def test_only_provider_button_is_shown_when_disabled(self, settings, keycloak_provider):
        settings.LOGIN_LOCAL_FORM_ENABLED = False
        settings.SOCIALACCOUNT_PROVIDERS = keycloak_provider
        response = Client().get(reverse("core:login"), SERVER_NAME="localhost")
        assert response.status_code == status.HTTP_200_OK
        # the local form is gone, only the provider button is left
        assert 'name="password"' not in response.text
        assert 'href="/accounts/oidc/keycloak/login/' in response.text

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
