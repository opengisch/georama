from georama.settings import Test


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
