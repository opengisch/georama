import logging

from django.conf import settings
from django.utils.translation import gettext_lazy as _

from georama.core.common.apps import GeoramaAbstractConfig

logger = logging.getLogger(__name__)


class CoreConfig(GeoramaAbstractConfig):
    label = "core"
    verbose_name = _("Core")
    name = "georama.core"
    description = _("The master app.")

    def ready(self):
        from georama.core.common.health import DatabaseHealthCheck, register_health_check

        # We don't want to register a menu for Core on the Page
        self.warn_about_login_without_provider()
        register_health_check(DatabaseHealthCheck())

    @staticmethod
    def warn_about_login_without_provider():
        """Warns at start when the local login form is switched off but no identity
        provider is configured. The login page then shows the local form anyway, the
        operator should know that the setting has no effect.

        Since Georama runs with uvicorn/gunicorn, the django system checks (which only
        run with manage.py commands) wouldn't be seen, so this is a plain log warning.
        """
        # we can only see the identity provider from the settings here, SocialApps from
        # the database are not available while the apps are loaded
        if settings.LOGIN_LOCAL_FORM_ENABLED or settings.OIDC_SERVER_URL:
            return
        logger.warning(
            "LOGIN_LOCAL_FORM_ENABLED is False but OIDC_SERVER_URL is not set. Set "
            "GEORAMA_OIDC_SERVER_URL or add a SocialApp in the admin. As long as no "
            "identity provider exists, the login page keeps the local form."
        )
