import logging

from django.conf import settings
from django.utils.translation import gettext_lazy as _

from georama.core.common.apps import GeoramaAbstractConfig

logger = logging.getLogger(__name__)


class CoreConfig(GeoramaAbstractConfig):
    label = "core"
    verbose_name = "Core"
    name = "georama.core"
    description = _("The master app.")

    def ready(self):
        # We don't want to register a menu for Core on the Page
        self.warn_about_login_without_provider()

    @staticmethod
    def warn_about_login_without_provider():
        # we can only see the identity provider from the settings here, SocialApps from
        # the database are not available while the apps are loaded
        if settings.LOGIN_LOCAL_FORM_ENABLED or settings.OIDC_SERVER_URL:
            return
        logger.warning(
            "LOGIN_LOCAL_FORM_ENABLED is False but OIDC_SERVER_URL is not set. Set "
            "GEORAMA_OIDC_SERVER_URL or add a SocialApp in the admin. As long as no "
            "identity provider exists, the login page keeps the local form."
        )
