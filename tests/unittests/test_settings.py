import pytest
from django.core.exceptions import ImproperlyConfigured

from georama.settings import Dev, Prod, Test


class TestSocialAccountProviders:
    def test_provider_is_offered_with_server_url(self):
        configuration = Test()
        configuration.OIDC_SERVER_URL = (
            "http://keycloak:7080/realms/ninjas/.well-known/openid-configuration"
        )
        app = configuration.SOCIALACCOUNT_PROVIDERS["openid_connect"]["APP"]
        assert app["settings"]["server_url"] == (
            "http://keycloak:7080/realms/ninjas/.well-known/openid-configuration"
        )

    def test_provider_is_not_offered_without_server_url(self):
        # without a server url the provider can't work
        configuration = Test()
        configuration.OIDC_SERVER_URL = None
        assert configuration.SOCIALACCOUNT_PROVIDERS == {}

    def test_server_url_without_client_id_stops_georama(self):
        # a production setup names its own client, the dev realm's client is no default
        configuration = Prod()
        configuration.OIDC_SERVER_URL = "https://sso.example.org/.well-known/openid-configuration"
        configuration.OIDC_CLIENT_ID = None
        with pytest.raises(ImproperlyConfigured, match="GEORAMA_OIDC_CLIENT_ID is missing"):
            _ = configuration.SOCIALACCOUNT_PROVIDERS

    @pytest.mark.parametrize("email_authentication", [True, False])
    def test_email_authentication_is_set_on_the_provider(self, email_authentication):
        configuration = Test()
        configuration.OIDC_SERVER_URL = (
            "http://keycloak:7080/realms/ninjas/.well-known/openid-configuration"
        )
        configuration.OIDC_EMAIL_AUTHENTICATION = email_authentication
        # allauth reads it per provider app, globally it stays off
        app = configuration.SOCIALACCOUNT_PROVIDERS["openid_connect"]["APP"]
        assert app["settings"]["email_authentication"] is email_authentication
        assert configuration.SOCIALACCOUNT_EMAIL_AUTHENTICATION is False


class TestMiddleware:
    @pytest.mark.parametrize("basic_auth_enabled", [True, False])
    def test_basic_auth_middleware_is_only_loaded_when_enabled(self, basic_auth_enabled):
        configuration = Test()
        configuration.BASIC_AUTH_ENABLED = basic_auth_enabled
        configuration.OIDC_SERVER_URL = None
        assert (
            "georama.core.middleware.basic_auth.BasicAuthenticationMiddleware"
            in configuration.MIDDLEWARE
        ) is basic_auth_enabled

    @pytest.mark.parametrize(
        "oidc_server_url,loaded",
        [
            ("http://keycloak:7080/realms/ninjas/.well-known/openid-configuration", True),
            # without a provider a bearer token can't be checked at all
            (None, False),
        ],
    )
    def test_bearer_middleware_is_only_loaded_with_a_provider(self, oidc_server_url, loaded):
        configuration = Test()
        configuration.BASIC_AUTH_ENABLED = False
        configuration.OIDC_SERVER_URL = oidc_server_url
        assert (
            "georama.core.middleware.oidc.GeoGirafeAuthenticationMiddleware"
            in configuration.MIDDLEWARE
        ) is loaded

    def test_basic_auth_sits_right_after_django_authentication(self):
        configuration = Test()
        configuration.BASIC_AUTH_ENABLED = True
        configuration.OIDC_SERVER_URL = (
            "http://keycloak:7080/realms/ninjas/.well-known/openid-configuration"
        )
        middleware = configuration.MIDDLEWARE
        # both need the user of the session first and run before the organisation check
        assert (
            middleware.index("georama.core.middleware.basic_auth.BasicAuthenticationMiddleware")
            == middleware.index("django.contrib.auth.middleware.AuthenticationMiddleware") + 1
        )
        assert middleware.index(
            "georama.core.middleware.oidc.GeoGirafeAuthenticationMiddleware"
        ) < middleware.index("georama.core.middleware.organisation.OrganisationMiddleware")

    def test_prod_serves_static_files_first(self):
        configuration = Prod()
        configuration.BASIC_AUTH_ENABLED = False
        configuration.OIDC_SERVER_URL = None
        # right after the security middleware, before any session or auth handling
        assert configuration.MIDDLEWARE[:2] == [
            "django.middleware.security.SecurityMiddleware",
            "servestatic.middleware.ServeStaticMiddleware",
        ]

    def test_dev_profiles_requests(self):
        configuration = Dev()
        configuration.BASIC_AUTH_ENABLED = False
        configuration.OIDC_SERVER_URL = None
        assert configuration.MIDDLEWARE[-1] == "silk.middleware.SilkyMiddleware"


class TestRestFrameworkAuthentication:
    @pytest.mark.parametrize(
        "basic_auth_enabled,oidc_server_url,authentication_classes",
        [
            # nothing authenticates from a header, the session is the only way in
            (False, None, ["rest_framework.authentication.SessionAuthentication"]),
            # the user of a header middleware is taken over before the session asks for
            # a CSRF token
            (
                True,
                None,
                [
                    "georama.core.middleware.authentication.MiddlewareAuthentication",
                    "rest_framework.authentication.SessionAuthentication",
                ],
            ),
            (
                False,
                "http://keycloak:7080/realms/ninjas/.well-known/openid-configuration",
                [
                    "georama.core.middleware.authentication.MiddlewareAuthentication",
                    "rest_framework.authentication.SessionAuthentication",
                ],
            ),
        ],
    )
    def test_authentication_classes(
        self, basic_auth_enabled, oidc_server_url, authentication_classes
    ):
        configuration = Test()
        configuration.BASIC_AUTH_ENABLED = basic_auth_enabled
        configuration.OIDC_SERVER_URL = oidc_server_url
        assert (
            configuration.REST_FRAMEWORK["DEFAULT_AUTHENTICATION_CLASSES"] == authentication_classes
        )


class TestLoginAttemptsRate:
    def test_rate_follows_the_settings(self):
        configuration = Test()
        configuration.LOGIN_ATTEMPTS_LIMIT = 3
        configuration.LOGIN_ATTEMPTS_BLOCKED_MINUTES = 10
        # allauth's notation: attempts / window / counted per username
        assert configuration.LOGIN_ATTEMPTS_RATE == "3/600s/key"
        # allauth's own login page counts the same, its limit per ip stays its default
        assert configuration.ACCOUNT_RATE_LIMITS == {"login_failed": "10/m/ip,3/600s/key"}
