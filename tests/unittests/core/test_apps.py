import logging

import pytest

from georama.core.apps import CoreConfig


class TestCoreConfig:
    @pytest.mark.parametrize(
        "login_local_form_enabled,oidc_server_url,warned",
        [
            # the local form is shown, nothing to warn about
            (True, None, False),
            (True, "http://keycloak:7080/realms/ninjas/.well-known/openid-configuration", False),
            # the form is off and a provider is configured, as intended
            (False, "http://keycloak:7080/realms/ninjas/.well-known/openid-configuration", False),
            # the form is off but there is no provider, the login page falls back to the form
            (False, None, True),
        ],
    )
    def test_warns_about_login_without_provider(
        self, settings, caplog, login_local_form_enabled, oidc_server_url, warned
    ):
        settings.LOGIN_LOCAL_FORM_ENABLED = login_local_form_enabled
        settings.OIDC_SERVER_URL = oidc_server_url
        with caplog.at_level(logging.WARNING, logger="georama.core.apps"):
            CoreConfig.warn_about_login_without_provider()
        assert ("LOGIN_LOCAL_FORM_ENABLED is False" in caplog.text) is warned
